# 导入模块运行
import fibo
fibo.fib(1000)
print(fibo.fib2(100))
print(fibo.fib3(30))


#  如果经常使用某个函数，可以把它赋值给局部变量：
fib = fibo.fib
fib(10)

fib2=fibo.fib2
print(fib2(10))

fib3=fibo.fib3
print(fib3(10))