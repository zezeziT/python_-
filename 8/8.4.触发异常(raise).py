# 我们可以自己主动判处异常
# raise NameError("HiThere")
# 📌 解释：
# raise 异常类(信息) 用来手动触发异常。


# 重新抛出异常
try:
    raise NameError("HiThere")
except NameError:
    print("捕获到异常，重新抛出")
    raise #重新抛出捕获到的异常对象



# 重新抛出可以在抛出前做一些收尾工作，而不是直接停止了
# 参考
# file:///E:\python\official_docs\8\8.4.python_raise_exceptions.md


#  有时候会有 Traceback 
# 参考
# file:///E:\python\official_docs\8\8.4.python_exception_traceback.md