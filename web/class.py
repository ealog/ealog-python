#!/usr/bin/env python
#-*-coding:utf-8-*-

class MyClass(object):

    message="hello, developer!"
    def show(self):
        print(self.message)
        print("Here is %s in %s!" % (self.name,self.color))

    @staticmethod
    def printMessage():
        print("printMessage is called")
        print(MyClass.message)

    @classmethod
    def createObj(cls,name,color):
        print("Object will be created: %s(%s, %s)"% (cls.__name__,name,color))
        return cls()

    def __init__ (self,name="unset",color="black"):
        print("Constructor is called with param: ",name," ",color)
        self.name = name
        self.color = color

    def __del__(self):
        print("Destructor is called for %s!"%self.name)


MyClass.printMessage()

inst = MyClass.createObj("Toby","Red")
print(inst.message)
del inst


"""inst = MyClass()
inst.show()

inst2 = MyClass("Divad")
inst2.show()

inst3 = MyClass("Lisa","Yellow")
inst3.show()

inst4 = MyClass(color="Green")
inst4.show()"""