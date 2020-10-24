#! /usr/bin/env

# coding:utf-8


import sys
import serial
import threading
from time import sleep

class Uart(object):
    def __init__(self,port,baud):
        self.err = 0
        # open serial
        try:
            self.serial = serial.Serial(port,baud)
            print("open serial success.")
        except:
            print("open serial error!")
            self.err = -1

    def uart_recv_thread(self):
        print("start uart_recv_thread.")

        while(True):
            try:
                recv_data_raw = self.serial.readline()
                data = "DEVICE------>PC:" + recv_data_raw.decode()
                print(data)
            except:
                print("recv data error!")
                break

    def start_recv_thread(self):
        thread = threading.Thread(target=self.uart_recv_thread,daemon=True)
        thread.start()

    def send_uart_data(self,data):
        self.serial.write(data.encode())

    def uart_close(self):
        self.serial.close()

if __name__ == "__main__":
    myuart = Uart("/dev/pts/2",9600)
    if (0 == myuart.err):
        print("Init uart success.")
    # if uart init success.run threading ,receive data
    myuart.start_recv_thread()


    while(True):
        input_data = input("Please enter data...")
        if (input_data == "quit"):
            #exit
            myuart.uart_close()
            break
        else:
            #send data to device
            myuart.send_uart_data(input_data)
            sleep(0.01) 

    print("exit.")
