#!/usr/bin/env
#coding:utf-8



import traceback,pymysql
keywords = "%002"
current_page = 1
line_size = 6


SQL = "select auto_id,meter_value,get_date,get_date_time,get_date_stamp,meter_addr from meters_data where meter_addr like %s limit %s,%s"

tuple1 = (15, 100, (2020, 10, 4), (2020, 10, 4, 14, 9, 34),(2020, 10, 4, 14, 9, 34), 'X001')

print(tuple1[0])
def main():
    try:
        conn = pymysql.connect(host="192.168.3.31",port=3306,charset="UTF8",user="root",password="windows12",database="prod_energy")
        print("MySql connection success, current version is %s"% conn.get_server_info())
        print("MySql connection success, commit is %s"% conn.get_autocommit())
        cmd = conn.cursor()
        cmd.execute(query=SQL,args=[keywords,(current_page-1) * line_size,line_size])
        for meters_data in cmd.fetchall():
            print(meters_data)
        
        # conn.commit()
        # print("data effect row is %s"%cmd.rowcount)
        # print("last times data Id is %s"%cmd.lastrowid)
    except Exception:
        print(traceback.format_exc())
    finally:
        conn.close()
    
if __name__ == "__main__":
    main()
