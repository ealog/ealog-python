#!/usr/bin/env python

# list = [num*num for num in range(1,11)]
# print(list)

# list1 = [num*num for num in range(1,11) if num%2 == 0]

# print(list1)


# list2 = [char+num for char in ['a','b','c'] for num in['1','2','3']]

# print(list2)


# list3 = (num*num for num in range(1,6))

# print(list3)

# for li in list3:
#     print(li)




# def square(input):
#     list = []

#     for num in range(input):
#         list.append(num*num)
#         print(list)
#     return list

# for num in square(1000):
#     print(num)


# def square(input):
#     for num in range(input):
#         print('before yield')
#         yield num*num
#         print('after yield')

# for num in square(5):
#     print(num)


# import time
# def timeTest():
#     print('timeTest start')
#     print('sleep 1 second...')
#     time.sleep(1)
#     print('timeTest end')

# timeTest()


# def hi(name="yasoob"):
#     print("now you are inside the hi() function")
 
#     def greet():
#         print("now you are in the greet() function")
 
#     def welcome():
#         print("now you are in the welcome() function")
 
   
#     print("now you are back in the hi() function")
 
# hi()


# def a_new_decorator(a_func):
 
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
 
#         a_func()
 
#         print("I am doing some boring work after executing a_func()")
 
#     return wrapTheFunction
 
# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell")
 
# a_function_requiring_decoration()
# #outputs: "I am the function which needs some decoration to remove my foul smell"
 
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# #now a_function_requiring_decoration is wrapped by wrapTheFunction()
 
# a_function_requiring_decoration()
# #outputs:I am doing some boring work before executing a_func()
# #        I am the function which needs some decoration to remove my foul smell
# #        I am doing some boring work after executing a_func()




# def use_logging(func):

#     def wrapper():
#         print("%s is running" % func.__name__)
#         return func()
#     return wrapper

# @use_logging
# def foo():
#     print("i am foo")

# foo()

# print(foo)


# def int2(num,base=2):
#     return int(num,base)

# print(int2('1010'))


# import struct
# s = '459C3800'
# print(s)
# #<是小端，>是大端，f代表浮点数
# print(struct.unpack('<f', bytes.fromhex(s))[0])#小端
# #输出：120.40420532226562
# s = float('6.55563714424545E-10')
# print(struct.pack('<f', s).hex())#小端
# #输出：32333430
# print(struct.pack('>f', s).hex())#大端
# #输出：30343332


# import struct

# print(struct.unpack('!f','459C3800'.decode('hex')))



# from ctypes import *

# def convert(s):
#     i = int(s,16)
#     cp = pointer(c_int(i))
#     fp = cast(cp, POINTER(c_float))
#     return fp.contents.value

# print(convert('45151000'))


import datetime
import time

cur_time_minute = datetime.datetime.now().minute
cur_time_second = datetime.datetime.now().second

if cur_time_minute == 0 or cur_time_minute == 30:
    sleep_time=0
elif cur_time_minute < 30:
    sleep_time = (30-cur_time_minute)*60 - cur_time_second
elif cur_time_minute > 30:
    sleep_time = (60-cur_time_minute)*60 - cur_time_second
print(sleep_time)
time.sleep(sleep_time)



while True:
    hour_now=datetime.datetime.now().hour
    minute_now=datetime.datetime.now().minute
    print(hour_now)
    print(minute_now)
    
    minute_now=datetime.datetime.now().minute
    second_now=datetime.datetime.now().second
    
    if sleep_time == 0 and minute_now == 1 or minute_now == 31:
        time.sleep(3600-second_now-60)
    else:
        time.sleep(3600-second_now)

    







