# finally 里面的代码总会执行 ，无论是否出错

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("除数为0！")
    else:
        print("结果是", result)
    finally:
        print("执行finally")

divide(2, 1)
divide(2, 0)


# try
# │
# ├── 成功 → else → finally
# └── 出错 → except → finally

# 💡总结： 
# try…except…else…finally
# except 处理异常
# else 只在 try 成功时执行
# finally 无条件执行