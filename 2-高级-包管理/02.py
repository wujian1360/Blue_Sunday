# _*_ coding:UTF-8 _*_

# 借助importlib,相当于倒入一个叫01的模块，并把它赋值给myModule
import importlib
myModule = importlib.import_module('01')

stu = myModule.Student('wujian',80)

stu.say()