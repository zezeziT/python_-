# 我们可以创建自己的异常类

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"MyError: {self.value}"
    
try:
    raise MyError("出错啦")
except MyError as e:
    print(e)

