#!/usr/bin/env python
#-*-coding:utf-8-*-

import datetime

def nameFunc(a):
    return "I'm named function with param %s"% a

def call_Func(func,param):
    print(datetime.datetime.now())
    print(func(param))
    print("")

if __name__ == "__main__":
    call_Func(nameFunc,'hello')
    call_Func(lambda x:x*2,9)
    call_Func(lambda y:y*y,-4)

    
