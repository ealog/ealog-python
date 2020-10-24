#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
class MyErr(Exception):
    def __str__(self):
        return "I'm a self-defined Error!"

def main():
    try:
        print("***********Start of Main()**************")
        if len(sys.argv) == 1:
            raise MyErr()
        print("***********End of Main()**************")
    except MyErr as e:
        print(e)

    
if __name__ == "__main__":
    main()