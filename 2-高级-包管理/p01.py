#-*- coding:UTF-8 -*-
# 可以在新建模板中写入

# 包含一个学生类
# 一个sayHello函数
# 一个打印语句


class Student():
     def __init__(self,name='NoName',age=18):
         self.name = name
         self.age = age
     def say(self):
         print('My name is {0}，I am {1} years old.'.format(self.name,self.age))

def sayHello(chenghu):
    print('Hi,你好{0}，欢迎您的光临'.format(chenghu))

# 当前代码作为主进程执行时。
# 当前代码被当做‘模块’，被别处调用的时候不执行后面的内容。
if __name__ == '__main__':
    print('我是模块01！！！！！！！')