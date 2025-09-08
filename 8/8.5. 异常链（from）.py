# 一个异常可以作为另一个异常的原因
try:
    open("database.sqlite")
except OSError as exc:
    raise RuntimeError("无法处理错误")  from exc

# except OSError :
#     raise RuntimeError("无法处理错误")  

# 📌 解释：
# from exc 表明 RuntimeError 是由 OSError 直接导致的。
# 方便定位问题。


#  raise  ... from  ...有什么用处 
#  参考
#  file:///E:\python\official_docs\8\8.5.python_exception_chain.md