#!/usr/bin/env
#coding:utf-8

import traceback,pymysql,dbutils.pooled_db

import time

import minimalmodbus

import datetime

import threading

import json

import configparser

import smtplib

from email.mime.text import MIMEText

from email.header import Header

conf=configparser.ConfigParser()

conf.read('config.ini',encoding='utf-8')

config_dic = conf._sections


json_file = 'lt_impep.json'

# 初始睡眠时间
sleep_time = 0

# 定义MODBUS设备链接串口及设备地址\baudrate\timeout， key 代表COM口，values 代表设备地址

modbus_set = config_dic['METER_PORT_ADDR']

baudrate = conf.getint('METER_INIT','baudrate')

timeout = conf.getint('METER_INIT','timeout')

# 定义发生读取错误时，发送邮件至那个邮箱地址

mail_host=conf.get('EMAIL_CONFIG','email_smtp') #设置服务器
mail_user=conf.get('EMAIL_CONFIG','email_sender') #用户名
mail_pass=conf.get('EMAIL_CONFIG','email_pwd') #口令 
sender = conf.get('EMAIL_CONFIG','email_sender')
receivers = conf.get('EMAIL_CONFIG','email_receiver') 

# 此条定义无意义，使用字典，定义每个设备的上次数据 key 代表设备地址 values 存储设备上次数据uart_inst
lt_impep={}

# 使用字典，存储设备返回数据
uart_data={}

# 定义暂停间隔
SEC = 0.1

# 定义峰，谷，平区间列表
F=[8,9,10,11,16,17,18,19,20,21]
G=[23,0,1,2,3,4,5]
P=[6,7,12,13,14,15,22]

# 定义SQL语句常量
SQL = "insert into meters_data (meter_addr,get_date_time,get_date,year_quarter,week_count,day_week,cur_year,cur_month,cur_day,cur_hour,cur_minute,H_L_M,Ua,Ub,Uc,Ia,Ib,Ic,Pt,Pa,Pb,Pc,PFt,PFa,PFb,PFc,Freq,ImpEp,ImpEp_increase,ExpEp,Q1Eq,Q2Eq,Q3Eq,Q4Eq,time_stamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
SQL1 = "select ImpEp from meters_data order by get_date_time desc limit 1"
# 定义数据库IP地址
ip_addr =conf.get('DATABASE_IP','ip_addr')

# 定义读取/写入json参数文件，当第一启动读取JSON文件内的，
def json_rw(rw):
    global lt_impep
    if rw == 'r':
        try:
            with open(json_file,'r') as f:
                lt_impep = json.loads(f.read())
                print(lt_impep)
        except Exception:
            print("File not found.")
    else:
        try:
            with open(json_file,'w') as f:
                f.write(json.dumps(lt_impep))
        except Exception:
            print("Write error!")
# 重新封装threading类，添加return方法，获得返回值。

class MyThread(threading.Thread):
    def __init__(self,func,args):
        super(MyThread,self).__init__()
        self.func = func
        self.args = args
        
    def run(self):
        self.result = self.func(*self.args)
    
    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


# 判断当前时间峰谷平区间函数，并返回峰谷平
def f_g_p1(hour,minute):
    time_quantum=""
    for feng in F:
        if hour==feng:
            if hour==11 and (minute > 30):
                time_quantum="平"
                break
            else:
                time_quantum="峰"
                break
    for gu in G:
        if hour==gu:
            time_quantum="谷"
            break
    for ping in P:
        if hour==ping:
            if hour==7 and minute >30:
                time_quantum="峰"
                break
            else:
                time_quantum="平"
                break
    return time_quantum

# 建立串口连接对象
def connect_uart(modbus_set,baudrate=9600,timeout=1):
    # RS485连接重试功能和连接超时功能的UART连接
    conn_status = True
    max_retries_count = 10  # 设置最大重试次数
    conn_retries_count = 0  # 初始重试次数
    conn_timeout = 3  # 连接超时时间为3秒
    i = 0
    inst = []
    while conn_status and conn_retries_count <= max_retries_count:
        try:
            print("连接RS485设备中..",modbus_set)
            
            
            for key,value in modbus_set.items():
                inst.append(minimalmodbus.Instrument(key,int(value)))
                print("inst is :",inst[i])
                inst[i].serial.baudrate = baudrate

                inst[i].serial.timeout = timeout
                
                # lt_impep[value]=(inst[i].read_float(4126,3,2,byteorder=0))*120
                # print(lt_impep)
                i = i+1
            print("已连接设备为： ",inst)
            conn_status = False  # 如果RS485连接成功则conn_status为设置为False则退出循环，返回inst列表连接对象
            return inst
            
        except:
            conn_retries_count += 1
            print(conn_retries_count)
            print('connect uart is error!!')
            time.sleep(conn_timeout) # test result!
        continue

# 设备数据读取，并返回字典，key 为设备 ，value 为 返回数据列表
def data_read(inst):
    try:    
        # 重复执行数据读取写入'
        

        cur_year=datetime.datetime.now().year
        cur_month=datetime.datetime.now().month
        cur_day=datetime.datetime.now().day
        cur_hour=datetime.datetime.now().hour
        cur_minute=datetime.datetime.now().minute
        time_now=datetime.datetime.now()
        cur_date=datetime.date.today()
        # 读取季度 格式为：2020Q1-2020Q4
        quarter = (cur_date.month-1) // 3 + 1
        year_quarter='{}Q{}'.format(cur_date.year, quarter)
        
        day_week = datetime.datetime.now().isoweekday()
        week_count=datetime.datetime.now().isocalendar()[1]
        
        meter_addr=inst.read_register(46,0,3,signed=False)
        # Uab=(inst.read_float(8192,3,2,byteorder=0))*0.1
        # time.sleep(SEC)
        # Ubc=(inst.read_float(8194,3,2,byteorder=0))*0.1
        # time.sleep(SEC)
        # Uca=(inst.read_float(8196,3,2,byteorder=0))*0.1
        # time.sleep(SEC)
        Ua=(inst.read_float(8198,3,2,byteorder=0))*0.1
        # time.sleep(SEC)
        Ub=(inst.read_float(8200,3,2,byteorder=0))*0.1
        # time.sleep(SEC)
        Uc=(inst.read_float(8202,3,2,byteorder=0))*0.1
        # time.sleep(SEC)
        Ia=(inst.read_float(8204,3,2,byteorder=0))*0.001*120
        # time.sleep(SEC)
        Ib=(inst.read_float(8206,3,2,byteorder=0))*0.001*120
        # time.sleep(SEC)
        Ic=(inst.read_float(8208,3,2,byteorder=0))*0.001*120
        # time.sleep(SEC)
        Pt=(inst.read_float(8210,3,2,byteorder=0))*0.1*120/1000
        # time.sleep(SEC)
        Pa=(inst.read_float(8212,3,2,byteorder=0))*0.1*120/1000
        # time.sleep(SEC)
        Pb=(inst.read_float(8214,3,2,byteorder=0))*0.1*120/1000
        # time.sleep(SEC)
        Pc=(inst.read_float(8216,3,2,byteorder=0))*0.1*120/1000
        # time.sleep(SEC)
        # Qt=(inst.read_float(8218,3,2,byteorder=0))*0.1
        # time.sleep(SEC)
        # Qa=(inst.read_float(8220,3,2,byteorder=0))*0.1
        # time.sleep(SEC)
        # Qb=(inst.read_float(8222,3,2,byteorder=0))*0.1
        # time.sleep(SEC)
        # Qc=(inst.read_float(8224,3,2,byteorder=0))*0.1
        # time.sleep(SEC)
        PFt=(inst.read_float(8234,3,2,byteorder=0))*0.001
        # time.sleep(SEC)
        PFa=(inst.read_float(8236,3,2,byteorder=0))*0.001
        # time.sleep(SEC)
        PFb=(inst.read_float(8238,3,2,byteorder=0))*0.001
        # time.sleep(SEC)
        PFc=(inst.read_float(8240,3,2,byteorder=0))*0.001
        # time.sleep(SEC)
        Freq=(inst.read_float(8260,3,2,byteorder=0))*0.01
        # time.sleep(SEC)
        ImpEp=inst.read_float(4126,3,2,byteorder=0)*120
        # time.sleep(SEC)
        ExpEp=inst.read_float(4136,3,2,byteorder=0)*120
        # time.sleep(SEC)
        Q1Eq=inst.read_float(4146,3,2,byteorder=0)*120
        # time.sleep(SEC)
        Q2Eq=inst.read_float(4156,3,2,byteorder=0)*120
        # time.sleep(SEC)
        Q3Eq=inst.read_float(4166,3,2,byteorder=0)*120
        # time.sleep(SEC)
        Q4Eq=inst.read_float(4176,3,2,byteorder=0)*120
        # time.sleep(SEC)
        # print("v is :"+str(Uab))
        # print("v is :"+str(Ubc))
        # print("v is :"+str(Uca))
        print("Ua is :"+str(Ua))
        print("Ub is :"+str(Ub))
        print("Uc is :"+str(Uc))
        print("Ia is :"+str(Ia))
        print("Ib is :"+str(Ib))
        print("Ic is :"+str(Ic))
        print("Pt is :"+str(Pt))
        print("Pa is :"+str(Pa))
        print("Pb is :"+str(Pb))
        print("Pc is :"+str(Pc))
        # print("v is :"+str(Qt))
        # print("v is :"+str(Qadatabase_instreq))
        print("ImpEp is :"+str(ImpEp))
        print("ExpEp is :"+str(ExpEp))
        print("Q1Eq is :"+str(Q1Eq))
        print("Q2Eq is :"+str(Q2Eq))
        print("Q3Eq is :"+str(Q3Eq))
        print("Q4Eq is :"+str(Q4Eq))
        print("Meter_addr is :"+str(meter_addr))
        print('lt_impep',lt_impep[str(meter_addr)])
        print('ImpEp:',ImpEp)
        ImpEp_increase = ImpEp - lt_impep[str(meter_addr)]
        print('ImpEp_increase:',ImpEp_increase)
        # 写入数据库字段值列表
        data_list = []
        
        H_L_M=f_g_p1(cur_hour,cur_minute)
        
        data_list.append((meter_addr,time_now,cur_date,year_quarter,week_count,day_week,cur_year,cur_month,cur_day,cur_hour,cur_minute,H_L_M,Ua,Ub,Uc,Ia,Ib,Ic,Pt,Pa,Pb,Pc,PFt,PFa,PFb,PFc,Freq,ImpEp,ImpEp_increase,ExpEp,Q1Eq,Q2Eq,Q3Eq,Q4Eq))

        # 更新lt_impep[meter_addr]数量为最后一次电量数，为算增加电量数据做准备
        

        meter_data = {meter_addr:data_list}
        print("线程数据为： ",meter_data)

        return meter_data
    except:
        message = MIMEText(inst, 'plain', 'utf-8')
        message['From'] = Header("菜鸟教程", 'utf-8')
        message['To'] =  Header("测试", 'utf-8')
        
        subject = '设备读取错误！'
        message['Subject'] = Header(subject, 'utf-8')
        
        
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass)  
            smtpObj.sendmail(sender, receivers, message.as_string())
            print ("邮件发送成功")
        except smtplib.SMTPException:
            print ("Error: 无法发送邮件")
def data_write(database_inst,uart_data):
    print(lt_impep)
    try:    

        for key,value in uart_data.items():
            
            print("database is value:",value)
            
            database_inst['cmd'].executemany(query=SQL,args=uart_data[key])
            
            database_inst['conn'].commit()
            
            print("uart_data values :",uart_data)
            lt_impep[str(key)] = uart_data[key][0][27]
            print(lt_impep[str(key)])

        # 写完数据后，休眠时间。
        time_now=datetime.datetime.now()
        minute_now=datetime.datetime.now().minute
        second_now=datetime.datetime.now().second

        # 调用json_rw()函数进行写入lt_impep数据。

        json_rw('w')

        # 判断当前程序运行时间，是否为整点或5的倍数，如果是则用301-当前系统时间秒-60 为下次开始读取数据时间，否则用301-当前系统时间秒为下次读取数据时间。
        if sleep_time == 0 and (minute_now % 5 == 1):
            a = 301-second_now-60
            print("Data get time is:%s" % time_now)
            print("sleep2",a)
            # time.sleep(a)
            return a

        else:
            b = 301-second_now
            print("Data get time is:%s" % time_now)
            print("sleep3",b)
            # time.sleep(b)
            return b


    except Exception:
        print(traceback.format_exc())
    finally:
        database_inst['conn'].close



# 数据库连接,并判断第一次执行时间
def connect_database():

    try:
        pool = dbutils.pooled_db.PooledDB(
            creator=pymysql,
            mincached=2,
            maxcached=5,
            maxconnections=50,
            blocking=True,
            host=ip_addr,
            port=3306,
            charset="UTF8",
            user="root",
            password="windows12",
            database="prod_energy"
        )
        conn = pool.connection()
        cmd = conn.cursor()
        database_inst = {'conn':conn,'cmd':cmd}
        print("database dic :",database_inst)
        return database_inst
    except Exception:
        print(traceback.format_exc())
    finally:
        # 读取时间间隔列表
        minute_lists = [0,5,10,15,20,25,30,35,40,45,50,55]
        cur_time_minute = datetime.datetime.now().minute
        cur_time_second = datetime.datetime.now().second

        # 当程序执行时，判断第一次数据读取时间
        for minute_list in minute_lists:

            if cur_time_minute % 5 == 0:
                sleep_time=0

            elif cur_time_minute < minute_list and minute_list - cur_time_minute < 5:
                sleep_time = (minute_list-cur_time_minute)*60 - cur_time_second

            elif cur_time_minute > 55:
                sleep_time = (60-cur_time_minute)*60 - cur_time_second
                
        print(sleep_time)
        time.sleep(sleep_time)        
    
def main():
    global uart_data
    json_rw('r')
    print(lt_impep)
    uart_inst = connect_uart(modbus_set)
    # print("实例数量为： ",len(uart_inst))
    database_inst = connect_database()
    while True:
        threads = []

        threads_len = range(len(uart_inst))

        print("threads_len values are:",threads_len)
        
        for i in threads_len:
            t = MyThread(data_read,args=(uart_inst[i],))
            threads.append(t)

        for i in threads_len:
            threads[i].start()
        
        for i in threads_len:
            threads[i].join()

        for i in threads_len:
            uart_data.update(threads[i].get_result())

        print("最终电表数据为： ",uart_data)
        sleep_time = data_write(database_inst,uart_data)
        time.sleep(sleep_time)


if __name__ == "__main__":
    main()

