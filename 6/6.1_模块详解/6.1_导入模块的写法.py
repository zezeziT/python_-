#
#🌟 导入模块的 4 种常见写法

# 1️⃣ 最基础：
# import 模块名
#
import fibo
fibo.fib(10)
print(fibo.fib2(10))
print(fibo.fib3(10))
#
# 👉 效果：
# 把整个模块 fibo 导入
# 用的时候要写 fibo.xxx




# 2️⃣ 给模块起别名：
# import 模块名 as 别名
# 
import fibo as fib
fib.fib(10)
print(fib.fib2(10))
#
#👉 效果：
# 也是导入整个模块
# 但是调用的时候可以用短名字（别名）



# 3️⃣ 只导入模块里某个函数 / 变量：
# from 模块名 import 某个名称
from fibo import fib
fib(500)
#fib2(10)  # 会报错  因为只导入了fib  并没有导入fib2 fib3  
# 👉 效果：
# 只导入模块里的某个函数
# 用的时候可以直接用 fib()，不用写模块名




# 4️⃣ 一次导入模块里的全部函数（不推荐用）：
# form 模块名 import *
from fibo import *
fib(500)
# 👉 效果：
# 导入模块里全部函数/变量（名字不以下划线开头的）
# 用的时候直接用名字，不用模块名
# ❗️ 缺点：容易弄混命名空间，变量可能冲突，平时写代码基本不推荐用，除非是交互式用（测试或临时试一试）




# 额外补充：
# 模块导入只会发生一次，如果你改了模块的代码，想重新加载，要用：
# import importlib
# importlib.reload(模块名)


