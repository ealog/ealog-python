# coding:utf-8

import sys
import threading
from time import sleep

from uart import Uart

class Tool(object):
    def __init__(self,parent):
        self.err = 0
        self.parent = parent
        print("Tool start.....")
        self.uart = Uart(self.parent.uart_port,self.parent.config_uart_baud)
        self.start_listen_uart()

    def start_listen_uart(self):
        threading.Thread(target=self.listen_uart_data_thread,daemon=True).start()

    def listen_uart_data_thread(self):
        print("start listen_uart_data_thread.")
        while(True):
            # print("listening....")
            # sleep(1)
            if not self.uart.is_queue_recv_empty():
                recv_data = self.uart.get_queue_recv()

                # 调用自定义信号
                self.parent.signal_recv_data.emit(recv_data)

