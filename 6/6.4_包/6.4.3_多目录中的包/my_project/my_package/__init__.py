# my_package/__init__.py

print("[mypackage] __init__.py 执行中")

import os

# 获取 extra_modules 的绝对路径
extra_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'extra_modules'))


# 输出当前__path__  （默认是【mypackage 的路径】 ）
print(f'[my_package] 初始 __path__ = {__path__}')


# 修改__path__ , 添加 extra_modules
__path__.append(extra_path)


# 再次输出__path__, 你会看到多了 extra_modules
print(f'[my_package] 修改后 __path__ = {__path__}')

