# 主程序 练习所有知识点

# 看看当前作用域的名字
print("当前命名的空间：", dir())



# 对模块命名还有要求！！！   6.4_包 错误  改为myapp
# import 6.4_包.tools.math_utils.py
# ❌ 错误原因：
# 6.4_包 这个模块名不能以数字开头，也不能包含小数点（.），否则 Python 会以为你在写小数，比如 6.4，结果当然报错了。
# import ...py 也错了，import 后面不能加 .py 后缀。
# 包名或模块名中如果含有非法字符（如中文或特殊符号 _ 前面的数字或点），也是不合法的。


# ✅ 导入包中模块的方法一：完整路径
import myapp.tools.math_utils
print(myapp.tools.math_utils.add(3, 4))



# ✅ 方法二：from ... import 模块
from myapp.tools import string_utils
print(string_utils.shout('hello'))



# ✅ 方法三：from ... import 函数
from myapp.tools.math_utils import subtract
print(subtract(10, 3))



# ✅ 调用 helpers.py 里的函数
from myapp import helpers
helpers.greet('Alice')



# ✅ tools/__init__.py 里自动导入的 add 函数
from myapp.tools import add
print(add(100, 50))



# ✅ 不会报错啦！！！！！
# ❌ 报错：没有 __init__.py，不能 import   
try:
    import myapp.effects.dummy
except ImportError as e:
    print("捕获到了 ImportError:", e)
# package_summary.py

"""
Python 包与 __init__.py 的简要总结（适用于 Python 3.3 及以后版本）

1. 传统观点：
   - 包必须包含 __init__.py 文件，否则不能被识别为包。
   - 没有 __init__.py 的文件夹导入会报 ImportError。
   - __init__.py 文件可用于包初始化代码。

2. Python 3.3+ 新特性（命名空间包）：
   - 允许没有 __init__.py 的目录也被识别为包（命名空间包）。
   - 这使得没有 __init__.py 的目录下模块也能被正常导入。
   - 命名空间包不能包含包初始化代码。
   - 方便大型项目拆分和多目录合并成同一包。

3. 建议：
   - 若需要传统包行为和包初始化，请为包目录添加 __init__.py（可以为空）。
   - 这样兼容性更好，代码行为更明确。
   - 对于纯粹分布式命名空间包，__init__.py 可以省略。

4. 结论：
   - Python 3.3+ 不强制要求 __init__.py，但推荐根据项目需求决定是否添加。
"""







