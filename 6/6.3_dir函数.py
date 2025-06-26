#
# print(dir())

# import fibo
# print(dir())

# print(dir(fibo))       # 可以换着运行

# import sys
# print(dir(sys))





# 🔍 先理解什么是“名称”
# 在 Python 里，
# 你创建的变量、导入的模块、定义的函数，
# 都会在“当前环境”里占一个名字，这叫“名称”。
#
a = 10
b = [1, 2, 3]
def hello():
    print('hi')
print(dir())

print('------------------')

# ✅ 带参数的 dir(某个东西) 
# —— 看看它里面有啥
#
import sys
print(dir(sys))

print('------------------')
# 可以调用这些功能
print(sys.version)


print('------------------')

# ✅ 看看内置的东西（Python 默认给你的函数）
# 有些东西是你一开始就能用的，
# 比如 print()，但你又没自己写，那它来自哪里？
#
import builtins
print(dir(builtins))
# 说明这些函数是 Python 默认自带的，所以你可以直接用，不需要 import。



##
a = 123
b = 'hello'
def greet():
    print("hi")


import sys
import builtins
import fibo

print(dir())          # 看你写了哪些东西
print("\n" + "-" * 50 + "\n")
print(dir(sys))       # 看sys里面有什么功能
print("\n" + "-" * 50 + "\n")
print(dir(builtins))  # 看python自带了哪些东西
print("\n" + "-" * 50 + "\n")
print(dir(fibo))      # 看fibo里面有什么
print("\n" + "-" * 50 + "\n")




