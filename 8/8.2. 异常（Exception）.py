# 示例1 除以0
# 10 * (1/0)
# ZeroDivisionError: division by zero
# 除数不能为 0，所以 Python 抛出了 ZeroDivisionError。

# 示例2 未定义的变量
# 4 + spam * 3
# NameError: name 'spam' is not defined
# spam 没定义过，所以报 NameError。


# 示例3： 类型不匹配
# '2' + 2
# TypeError: can only concatenate str (not "int") to str 
# 不能把字符串 '2' 和整数 2 相加。

# 👉 总结：异常的最后一行会告诉你 异常类型（ZeroDivisionError, NameError, TypeError 等）和 错误原因。


# Python 一次只能抛出并显示一个异常，不会把所有可能的错误都报出来。
# 1. 程序执行是 顺序 的
# 2. 一个语句里只会触发第一个错误

# 3. 如果想“看到所有潜在错误”怎么办？
# 就得用 多个 try-except，让程序不中断，把错误捕捉下来：

# 可以学完8.3再看这个

tests = [
    lambda: 10 * (1/0) ,
    lambda: 4 + spam * 3 ,
    lambda: '2' + 2
]

for t in tests:
    try:
        t()
    except Exception as e:
        print("捕获错误：", type(e).__name__, '-', e)
