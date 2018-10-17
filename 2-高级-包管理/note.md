# 1.模块

### 要点
   - 模块：一个.py文件
   - 用import导入使用(全部倒入、选择性导入from)
   - * 通常代表所有内容
   - if __name__ == '__main__'



- 一个模块就是一个包含python代码的文件，后缀名是.py就行。模块就是一个Python文件。
- 为什么用模块
  - 程序太大需要拆分
  - 模块可以增加代码复用
  - 当做命名空间，避免命名冲突
- 如何定义模块
  - 模块就是一个普通文件，任何代码可以直接书写
  - 遵守模块书写规范
    - 函数（单一功能）
    - 类（相似功能的组合，或者类似业务模块）
    - 测试代码

- 如何使用模块
 - 模块直接导入：import module_name
 - 以数字开头模块名：需要借助importtlib帮助
   - 语法
   -     import module_name
         module_name.function_name
         module_name.class_name
         
 - 案例:  01.py, 02.py, p01.py, p02.py
     
 - 别名导入： import 模块 as 别名
   - 导入的同时各模块起一个别名
   - 其余用法跟第一种相同
   - 案例：  p03.py
  
  
  
 - 用什么就导入什么：form ... import ..., ...
   - form module_name import func_name, class_name
   - 按照上述方法有选择性的导入，使用时不用模块名
   - 案例p04
   
 - 导入模块内所有内容（可以不加前缀直接调用）：form module_name import *
   - 这个写法比较无聊，* 代表所有,戴氏可以不用前缀，但是会命名污染
   - 案例p05
   
 - if __name__ == '__main__':的使用
   - 当前代码作为主进程执行时。
   - 可以有效地避免模块代码被导入的时候被动执行问题
   - 建议所有模块的入口都用此代码为入口
 
# 2.模块的搜索路径和存储
### 要点
   - 模块搜索路径
   - import sys 和  sys.path
   - 模块加载顺序


 - 什么是模块的搜索路径
   - 加载模块的时候，系统会在哪些地方寻找此模块
 - 系统默认的模块搜索路径
        
        import sys
        sys.path  #该属性可以获得路径列表
        # 案例p06.py
        
  - 添加搜索路径：可以用sys.path.append(dir)添加新的搜索路径
        
        sys.path.append(dir)
  
  - 模块加载顺序
    1.先搜索内存中已经加载好的模块
    2.搜索python的内置模块
    3.搜索sys.path路径
    
# 包：
### 要点
   - 文件夹结构
   - 必须包含__init__.py
   - 导入包
     - import package 
     - import package as p
   - 导入包里的模块
     - import package.module
     - import package.module as pm
   - 从包里导入指定的多个模块 
     - from package import [module1,module2,module3, ...]
   - 从包里导入__all__指定的多个模块  
     - from package import *
     - __all__ = ['module1','module2','package1', ...]
     - all在__init__.py中指定，否则第一行只包含__init__.py的内容
   - 从包里制定模块，导入其全部内容  
     - form package.module import *
   
   
 - 包是一种组织管理代码的方法，包里面存放的是模块
   - 用于将模块包含在一起的文件夹就是包
 - 自定义包的结构
   - 包
     - __init__.py 包的标志文件
     - 模块1.py
     - 模块2.py
     - ...
     - 子包
       __init__.py 
       - 模块1.py
       - 模块2.py
       - ...
 - 包的导入操作
   - import package_name
     - 直接导入一个包，可以使用__init__.py中的内容
     - 使用方法：
     
             package_name.func_name
             package_name.class_name.func)name()
             
     - 此种方式的访问内容是
     - 案例pkg01, p07.py
   - import package_name as p
     - 具体用法跟作用方式，跟上述简单导入一致
     - 注意：此种方法是默认对__init__.py内容的导入
     
     
   - import package.module
     - 导入包中某一个具体模块
     - 使用方法： 
            
                 package.module.func_name
                 package.module.class.fun()
                 pageage.module.class.var
            
     - 案例p08.py
     - import package.module as pm
   
   - from ... import 导入
      - from package import [module1,module2,module3, ...]
      - 此种导入方法不执行__init__的内容
      
                from pkg01 import p01
                p01.sayHello()
      
      - from package import *
        - 导入当前包__init__.py文件中所有的函数和类
        - 使用方法
                
                fun_name()
                class_name.func_name()
                class_name.var
                
        - 案例p09.py,注意此种导入具体内容，只包括__init__内的内容
   
   - form package.module import *
     - 导入包中指定的模块的所有内容
     - 使用方法
     
                 func_name()
                 class_name.func_name()
   
   - 在开发环境中经常会使用其他模块，可以在当前包中直接导入其他模块中的内容
     -           import 完整的包或者模块的路径
   - '__all__'的用法
     - 在使用from package import * 的时候， * 可以导入的内容。
     - '__init__'.py中如果文件为空，或者没有'__all__',那么只可以吧'__init__'中的内容导入
     - 如果设置了all的内容，那么则按照all指定的包或者模块进行导入，此时则不会导入init的内容
     -      __all__ = ['module1','module2','package1', ...]

# 命名空间 
  - 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
  - 作用是防止命名冲突
              
              setName()
              Stu.setName()
              Dog.setName()
              
  
      
      
     
     