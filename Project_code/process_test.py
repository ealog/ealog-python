import time
import os

import multiprocessing

#sing function

def sing(num,name):
    print("sing pid :",os.getpid())
    print("main,sing pid :",os.getppid())
    for i in range(num):
        print(name)
        print("sing....",i)
        time.sleep(1)

#dance function

def dance(num,name):
    print("dance pid :",os.getpid())
    print("main,dance pid :",os.getppid())
    for i in range(num):
        print(name)
        print("Dance....",i)
        time.sleep(1)

def main():
    sing_process = multiprocessing.Process(target=sing,args=(10,"LiuYang"))
    dance_process = multiprocessing.Process(target=dance,kwargs={"num":7,"name":"LiXiaofeng"})

    sing_process.start()
    sing_process.join()
    dance_process.start()
    
    time.sleep(2)
    print("main done...")
   
if __name__ == "__main__":
    print("main pid :",os.getpid())
    print("main,main pid :",os.getppid())
    main()



