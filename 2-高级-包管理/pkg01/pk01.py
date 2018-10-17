#-*- coding:UTF-8 -*-

class Student():
     def __init__(self,name='NoName',age=18):
         self.name = name
         self.age = age
     def say(self):
         print('My name is {0}，I am {1} years old.'.format(self.name,self.age))

def sayHello(chenghu):
    print('Hi,你好{0}，欢迎您的光临'.format(chenghu))

