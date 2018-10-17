# _*_ coding:UTF-8 _*_
import sys

print (type(sys.path))
print(sys.path)

for i in sys.path:
    print(i)

# 可以用sys.path.append(dir)添加新的搜索路径