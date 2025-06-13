# def fib(n):    #打印小于n的斐波那契数列
#     """Print a Fibonacci series less than n"""
#     a,b=0,1
#     while a < n:
#         print(a,end=' ')
#         a,b = (b,a+b)
# # 现在调用我们刚才定义的函数：
# fib(2000)
# print('\n')
# print(fib.__doc__)

# f=fib
# f(99)
# fib(0)
# print(fib(0))

def fib2(n):
    a,b=0,1
    result=[]
    # return fiblist
    while a<n:
        a,b=b,a+b
        result.append(a)
    return result

print(fib2(1000))

print(fib2(0))

zezeze = [99,99,80,44]
zezeze = zezeze + [90]
print(zezeze)

