# 我们可以用 try...except 来捕获异常，避免程序崩溃。

# try:
#     # 可能出错的代码
# except 错误类型:
#     # 如果出错，执行这里


# 示例 1：输入数字
while True:
    try :
        x = int(input("请输入一个数字："))
        break
    except ValueError:    #ValueError: → 专门处理“值不对”的错误
        print("输入无效，请重新输入...")
# 📌 解释：
# try 里面放可能出错的代码。
# 如果出错（比如输入了 "abc"），就会进入 except ValueError。
# except ValueError: → 专门处理“值不对”的错误
# 如果发生别的错误（比如 ZeroDivisionError），就不会被这个捕获
# 如果没错，就会跳过 except，正常运行。

# 可参考异常类型文件
# file:///E:\python\official_docs\8\8.3\Python常见异常类型对照表.md

while True:   # 真
    print("运行一次")
    break     # 否则会死循环

while False:  # 假
    print("不会运行")






