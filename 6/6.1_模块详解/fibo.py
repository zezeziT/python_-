#  f(n) 输出小于n的项
def fib(n):
    a, b = 0, 1
    while (a < n):
        print(a, end = ' ')
        a, b = b, a + b
    print()



# 输出小于n的项组成的列表
def fib2(n):
    a, b =0, 1
    L = []
    while(a < n):
        L.append(a)
        a, b = b, a+b
    return L
    


# f（n） 输出前n项
def fib3(n):
    a, b = 0, 1
    L1 =[]
    for _ in range(n):
        L1.append(a)
        a, b = b, a+b
    return L1  
    # 把结果返回出去  如果没有 print（fib3（n）就是None


# fib(10)
# print(fib2(10))
# print(fib3(10))

# print('__name: ',__name__)
# print(f'__name__ = {__name__}')


#  text 6.1.1_知识
if __name__ == '__main__' :
    import sys
    fib(int(sys.argv[1]))
    print(fib2(int(sys.argv[1])))
    print(fib3(int(sys.argv[1])))

    # sys.argv[1]  导入第一个参数  
    # py fibo.py 50    fibo.py 是sys.argv[0]   参数50是sys.argv[1]
    # int（sys。。） 将字符串格式的50参数转为int格式50
    # fib（int。。） 调用fib函数
    

    
