#!/usr/env/bin python

#coding:utf-8

import socket

HOST = '127.0.0.1'
PORT = 3434

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))

print("Connect %s:%d"%(HOST,PORT))

data = s.recv(1024)

print("Received: ",data)

s.close