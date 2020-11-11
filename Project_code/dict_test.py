#!/usr/env/bin python

#coding=utf-8

def dic_re():


    list_1 =[1,2,3,"22"]

    dict1={1:list_1}

    return dict1

dict2={2:6,1:7}
print(dict2)

dict2.update(dic_re())

print(dict2)




