#Lambda表达式
#lambda 参数：返回值表达式
#lambda x : x+1  #接收一个参数，返回+1的结果
#lambda a,b : a+b  #接收两个参数，返回它们的和
#lambda pair : pair[1]  #接收一个元组，返回第二个参数

def  f(pair):
    return pair[1]
f((2,'three'))

g = lambda pair : pair[1]
g((2,'three'))

# g()和f()是一种功能的函数其实 g(参数)  其实参数就是匿名函数中的参数，‘：’前面的东西