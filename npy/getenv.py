import platform
import sys
import os

def showENV():
    s = platform.platform()
    print("Current System is: ",s)
    p = sys.path
    print("Current installed path is: ",p)
    op = os.getcwd()
    print("Current software install path is: ",op)
    print("Python version is: ",sys.version_info)

print("Hello World!")
if __name__ == '__main__':
    showENV()