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


if __name__ == '__main__':
    fib(10)
    print(fib2(10))
    print(fib3(10))