#!/usr/bin/env
#coding:utf-8

import traceback,pymysql,dbutils.pooled_db

import time

import minimalmodbus

import datetime



# 使用字典，定义每个设备的上次数据 key 代表设备地址 values 存储设备上次数据
lt_impep={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0}
# 定义暂停间隔
SEC = 0.1
# 定义峰，谷，平区间列表
F=[8,9,10,11,16,17,18,19,20,21]
G=[23,0,1,2,3,4,5]
P=[6,7,12,13,14,15,22]
# 定义SQL语句常量
SQL = "insert into meters_data (meter_addr,get_date_time,get_date,year_quarter,week_count,day_week,cur_year,cur_month,cur_day,cur_hour,cur_minute,H_L_M,Ua,Ub,Uc,Ia,Ib,Ic,Pt,Pa,Pb,Pc,PFt,PFa,PFb,PFc,Freq,ImpEp,ImpEp_increase,ExpEp,Q1Eq,Q2Eq,Q3Eq,Q4Eq,time_stamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
# 定义数据库IP地址
ip_addr ="192.168.3.55"
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


def connect_uart():

    try:
        inst = minimalmodbus.Instrument('COM4',1)

        inst.serial.baudrate=9600

        inst.serial.timeout=1
        
        lt_impep[1]=inst.read_float(4126,3,2,byteorder=0)
        
        # inst = minimalmodbus.Instrument('COM6',2)

        # inst.serial.baudrate=9600

        # inst.serial.timeout=1
        
        # lt_impep[2]=inst.read_float(4126,3,2,byteorder=0)

        # inst = minimalmodbus.Instrument('COM7',3)

        # inst.serial.baudrate=9600

        # inst.serial.timeout=1
        
        # lt_impep[3]=inst.read_float(4126,3,2,byteorder=0)
        
        # inst = minimalmodbus.Instrument('COM8',4)

        # inst.serial.baudrate=9600

        # inst.serial.timeout=1
        
        # lt_impep[4]=inst.read_float(4126,3,2,byteorder=0)

        # inst = minimalmodbus.Instrument('COM9',5)

        # inst.serial.baudrate=9600

        # inst.serial.timeout=1
        
        # lt_impep[5]=inst.read_float(4126,3,2,byteorder=0)
        
        # inst = minimalmodbus.Instrument('COM10',6)

        # inst.serial.baudrate=9600

        # inst.serial.timeout=1
        
        # lt_impep[6]=inst.read_float(4126,3,2,byteorder=0)

        # inst = minimalmodbus.Instrument('COM11',7)

        # inst.serial.baudrate=9600

        # inst.serial.timeout=1
        
        # lt_impep[7]=inst.read_float(4126,3,2,byteorder=0)
        
        # inst = minimalmodbus.Instrument('COM12',8)

        # inst.serial.baudrate=9600

        # inst.serial.timeout=1
        
        # lt_impep[8]=inst.read_float(4126,3,2,byteorder=0)

        # inst = minimalmodbus.Instrument('COM13',9)

        # inst.serial.baudrate=9600

        # inst.serial.timeout=1
        
        # lt_impep[9]=inst.read_float(4126,3,2,byteorder=0)
        
        # inst = minimalmodbus.Instrument('COM14',10)

        # inst.serial.baudrate=9600

        # inst.serial.timeout=1
        
        # lt_impep[10]=inst.read_float(4126,3,2,byteorder=0)




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
        # print("MySql connection success, current version is %s"% conn.get_server_info())
        # print("MySql connection success, commit is %s"% conn.get_autocommit())
        cmd = conn.cursor()
        data_list = []
        minute_lists = [0,5,10,15,20,25,30,35,40,45,50,55]
        cur_time_minute = datetime.datetime.now().minute
        cur_time_second = datetime.datetime.now().second

        for minute_list in minute_lists:

            if cur_time_minute % 5 == 0:
                sleep_time=0

            elif cur_time_minute < minute_list and minute_list - cur_time_minute < 5:
                sleep_time = (minute_list-cur_time_minute)*60 - cur_time_second

            elif cur_time_minute > 55:
                sleep_time = (60-cur_time_minute)*60 - cur_time_second

                print(sleep_time)
        print(sleep_time)
        time.sleep(sleep_time)        
        cur_time_minute = datetime.datetime.now().minute
        


        while True:


            cur_year=datetime.datetime.now().year
            cur_month=datetime.datetime.now().month
            cur_day=datetime.datetime.now().day
            cur_hour=datetime.datetime.now().hour
            cur_minute=datetime.datetime.now().minute
            time_now=datetime.datetime.now()
            cur_date=datetime.date.today()
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
            Ia=(inst.read_float(8204,3,2,byteorder=0))*0.001
            # time.sleep(SEC)
            Ib=(inst.read_float(8206,3,2,byteorder=0))*0.001
            # time.sleep(SEC)
            Ic=(inst.read_float(8208,3,2,byteorder=0))*0.001
            # time.sleep(SEC)
            Pt=(inst.read_float(8210,3,2,byteorder=0))*0.1
            # time.sleep(SEC)
            Pa=(inst.read_float(8212,3,2,byteorder=0))*0.1
            # time.sleep(SEC)
            Pb=(inst.read_float(8214,3,2,byteorder=0))*0.1
            # time.sleep(SEC)
            Pc=(inst.read_float(8216,3,2,byteorder=0))*0.1
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
            ImpEp=inst.read_float(4126,3,2,byteorder=0)
            # time.sleep(SEC)
            ExpEp=inst.read_float(4136,3,2,byteorder=0)
            # time.sleep(SEC)
            Q1Eq=inst.read_float(4146,3,2,byteorder=0)
            # time.sleep(SEC)
            Q2Eq=inst.read_float(4156,3,2,byteorder=0)
            # time.sleep(SEC)
            Q3Eq=inst.read_float(4166,3,2,byteorder=0)
            # time.sleep(SEC)
            Q4Eq=inst.read_float(4176,3,2,byteorder=0)
            # time.sleep(SEC)
            # print("v is :"+str(Uab))
            # print("v is :"+str(Ubc))
            # print("v is :"+str(Uca))
            # print("v is :"+str(Ua))
            # print("v is :"+str(Ub))
            # print("v is :"+str(Uc))
            # print("v is :"+str(Ia))
            # print("v is :"+str(Ib))
            # print("v is :"+str(Ic))
            # print("v is :"+str(Pt))
            # print("v is :"+str(Pa))
            # print("v is :"+str(Pb))
            # print("v is :"+str(Pc))
            # print("v is :"+str(Qt))
            # print("v is :"+str(Qa))
            # print("v is :"+str(Qb))
            # print("v is :"+str(Qc))
            # print("v is :"+str(PFt))
            # print("v is :"+str(PFa))
            # print("v is :"+str(PFb))
            # print("v is :"+str(PFc))
            # print("v is :"+str(Freq))
            # print("v is :"+str(ImpEp))
            # print("v is :"+str(ExpEp))
            # print("v is :"+str(Q1Eq))
            # print("v is :"+str(Q2Eq))
            # print("v is :"+str(Q3Eq))
            # print("v is :"+str(Q4Eq))
            # print("v is :"+str(meter_addr))

            ImpEp_increase = ImpEp - lt_impep[meter_addr]
         
            
            H_L_M=f_g_p1(cur_hour,cur_minute)
            data_list.append((meter_addr,time_now,cur_date,year_quarter,week_count,day_week,cur_year,cur_month,cur_day,cur_hour,cur_minute,H_L_M,Ua,Ub,Uc,Ia,Ib,Ic,Pt,Pa,Pb,Pc,PFt,PFa,PFb,PFc,Freq,ImpEp,ImpEp_increase,ExpEp,Q1Eq,Q2Eq,Q3Eq,Q4Eq))
            
            cmd.executemany(query=SQL,args=data_list)
            data_list.clear()
            
            conn.commit()
            

            lt_impep[meter_addr] = ImpEp
            
            print("sleep1",lt_impep[meter_addr])
            minute_now=datetime.datetime.now().minute
            second_now=datetime.datetime.now().second

            if sleep_time == 0 and (minute_now % 5 == 1):
                a = 301-second_now-60
                print("Data get time is:%s" % time_now)
                print("sleep2",a)
                time.sleep(a+1)

            else:
                b = 301-second_now
                print("Data get time is:%s" % time_now)
                print("sleep3",b)
                time.sleep(b+1)

    except Exception:
        print(traceback.format_exc())
    finally:
        conn.close()




def main():
    pass
    
if __name__ == "__main__":
    main()

