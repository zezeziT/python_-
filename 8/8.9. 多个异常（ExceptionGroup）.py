# Python 3.11 新增，可以同时抛出多个异常。

def f():
    excs = [OSError("错1"), SystemError("错2")]
    raise ExceptionGroup("多个异常", excs)

try:
    f()
except* OSError:
    print("捕获 OSError")
except* SystemError:
    print("捕获 SystemError")
