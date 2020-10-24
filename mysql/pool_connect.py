#!/usr/bin/env
#coding:utf-8

import traceback,pymysql,dbutils.pooled_db

from ctypes import *

import minimalmodbus

import datetime

meter_value = 6000
meter_addr = 'X003'

SQL = "insert into meters_data (meter_value,get_date,get_date_time,get_date_stamp,meter_addr) values (%s,%s,%s,%s,%s)"







ip_addr ="192.168.3.51"

def main():
    try:
        pool = dbutils.pooled_db.PooledDB(
            creator=pymysql,
            mincached=2,
            maxcached=5,
            maxconnections=20,
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
        for num in range(110):
            time_now=datetime.datetime.now()
            data_list.append((meter_value,time_now,time_now,time_now,meter_addr))
            if num % 20 == 0:
                time_now=datetime.datetime.now()
                cmd.executemany(query=SQL,args=data_list)
                data_list.clear()
        # cmd.execute(query=SQL,args=[meter_value,meter_addr])
        conn.commit()
        # print("data effect row is %s"%cmd.rowcount)
        # print("last times data Id is %s"%cmd.lastrowid)
    except Exception:
        print(traceback.format_exc())
    finally:
        conn.close()
    
if __name__ == "__main__":
    main()

