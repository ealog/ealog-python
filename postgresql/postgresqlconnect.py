#!/usr/bin/env
#coding:utf-8

import traceback,pymysql

SQL = "insert into meters_data (meter_value,get_date,get_date_time,get_date_stamp,meter_addr) value (100,curdate(),now(),now(),'X001')"


def main():
    try:
        conn = pymysql.connect(host="192.168.3.31",port=3306,charset="UTF8",user="root",password="windows12",database="prod_energy")
        print("MySql connection success, current version is %s"% conn.get_server_info())
        print("MySql connection success, commit is %s"% conn.get_autocommit())
        cmd = conn.cursor()
        cmd.execute(SQL)
        conn.commit()
        print("data effect row is %s"%cmd.rowcount)
        print("last times data Id is %s"%cmd.lastrowid)
    except Exception:
        print(traceback.format_exc())
    finally:
        conn.close()
    
if __name__ == "__main__":
    main()




