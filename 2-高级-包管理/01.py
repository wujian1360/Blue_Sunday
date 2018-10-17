# _*_ coding:UTF-8 _*_
# 包含一个学生类
# 一个sayHello函数
# 一个打印语句


class Student():
     def __init__(self,name='NoName',age=18):
         self.name = name
         self.age = age
     def say(self):
         print('My name is {0}，I am {0} years old.'.format(self.name,self.age))

def sayHello(chenghu):
    print('Hi,你好{0}，欢迎您的光临'.format(chenghu))

print('我是模块01！！！！！！！')