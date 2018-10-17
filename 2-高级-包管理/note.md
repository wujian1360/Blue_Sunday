# 1.模块
- 一个模块就是一个包含python代码的文件，后缀名是.py就行。模块就是一个Python文件。


- 如何使用模块
 - 模块直接导入
   - 加入模块名称直接以数字开头，需要借助importtlib帮助
 - 语法
     import module_name
     module_name.function_name
     module_name.class_name
     
 - import 模块 as 别名
   - 导入的同时各模块起一个别名
   - 其余用法跟第一种相同
  
 - 用什么就导入什么
   - form module_name import func_name, class_name
   - 按照上述方法有选择性的导入，使用时不用模块名
   - 案例p04
   
   - form module_name import *
   - 这个写法比较无聊，*代表所有,戴氏可以不用前缀，但是会命名污染