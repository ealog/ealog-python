#!/usr/bin/env

# coding:utf-8

import time


def func_a():
    time.sleep(1)
    print("A")
    
def func_b():
    print("B")
    time.sleep(1)

func_a()
func_b()