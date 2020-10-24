#!/usr/bin/env python

#coding:utf-8
import time

from ctypes import *

import minimalmodbus

def convert(s):
    i = int(s,16)
    cp = pointer(c_int(i))
    fp = cast(cp, POINTER(c_float))
    return fp.contents.value

SEC = 0.1
inst = minimalmodbus.Instrument('COM2',1)

inst.serial.baudrate=9600

inst.serial.timeout=1
while True:
    temp=inst.read_float(8192,3,2,byteorder=0)
    time.sleep(SEC)
    temp2=inst.read_float(8194,3,2,byteorder=0)
    time.sleep(SEC)
    temp3=inst.read_float(8196,3,2,byteorder=0)
    time.sleep(SEC)
    temp4=inst.read_float(8198,3,2,byteorder=0)
    time.sleep(SEC)
    temp5=inst.read_float(8200,3,2,byteorder=0)
    time.sleep(SEC)
    temp6=inst.read_float(8202,3,2,byteorder=0)
    time.sleep(SEC)
    temp7=inst.read_float(8204,3,2,byteorder=0)
    time.sleep(SEC)
    temp8=inst.read_float(8206,3,2,byteorder=0)
    time.sleep(SEC)
    temp9=inst.read_float(8208,3,2,byteorder=0)
    time.sleep(SEC)
    temp10=inst.read_float(8210,3,2,byteorder=0)
    time.sleep(SEC)
    temp11=inst.read_float(8212,3,2,byteorder=0)
    time.sleep(SEC)
    temp12=inst.read_float(8214,3,2,byteorder=0)
    time.sleep(SEC)
    temp13=inst.read_float(8216,3,2,byteorder=0)
    time.sleep(SEC)
    temp14=inst.read_float(8218,3,2,byteorder=0)
    time.sleep(SEC)
    temp15=inst.read_float(8220,3,2,byteorder=0)
    time.sleep(SEC)
    temp16=inst.read_float(8222,3,2,byteorder=0)
    time.sleep(SEC)
    temp17=inst.read_float(8224,3,2,byteorder=0)
    time.sleep(SEC)
    temp18=inst.read_float(8234,3,2,byteorder=0)
    time.sleep(SEC)
    temp19=inst.read_float(8236,3,2,byteorder=0)
    time.sleep(SEC)
    temp20=inst.read_float(8238,3,2,byteorder=0)
    time.sleep(SEC)
    temp21=inst.read_float(8240,3,2,byteorder=0)
    time.sleep(SEC)
    temp22=inst.read_float(8260,3,2,byteorder=0)
    time.sleep(SEC)
    temp23=inst.read_float(4126,3,2,byteorder=0)
    time.sleep(SEC)
    temp24=inst.read_float(4136,3,2,byteorder=0)
    time.sleep(SEC)
    temp25=inst.read_float(4146,3,2,byteorder=0)
    time.sleep(SEC)
    temp26=inst.read_float(4156,3,2,byteorder=0)
    time.sleep(SEC)
    temp27=inst.read_float(4166,3,2,byteorder=0)
    time.sleep(SEC)
    temp28=inst.read_float(4176,3,2,byteorder=0)
    time.sleep(SEC)
    print("v is :"+str(temp))
    print("v is :"+str(temp2))
    print("v is :"+str(temp3))
    print("v is :"+str(temp4))
    print("v is :"+str(temp5))
    print("v is :"+str(temp6))
    print("v is :"+str(temp7))
    print("v is :"+str(temp8))
    print("v is :"+str(temp9))
    print("v is :"+str(temp10))
    print("v is :"+str(temp11))
    print("v is :"+str(temp12))
    print("v is :"+str(temp13))
    print("v is :"+str(temp14))
    print("v is :"+str(temp15))
    print("v is :"+str(temp16))
    print("v is :"+str(temp17))
    print("v is :"+str(temp18))
    print("v is :"+str(temp19))
    print("v is :"+str(temp20))
    print("v is :"+str(temp21))
    print("v is :"+str(temp22))
    print("v is :"+str(temp23))
    print("v is :"+str(temp24))
    print("v is :"+str(temp25))
    print("v is :"+str(temp26))
    print("v is :"+str(temp27))
    print("v is :"+str(temp28))
