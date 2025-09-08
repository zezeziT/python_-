# 示例3 异常类的继承顺序
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
# 输出 B C D
raise C()
# 检查 except 顺序：
# except D: ❌ C 不是 D
# except C: ✅ 匹配成功
# 输出
# C
# 注意：即使 C 继承了 B，也不会走 except B:，因为 Python 只匹配第一个符合类型的 except。




# Exception (Python 内置基类)
# └── B
#     └── C
#         └── D
# B 是父类
# C 继承自 B
# D 继承自 C
# 所以 D 也是 C 和 B 的子类，Python 的 except 会匹配第一个能匹配的类型





# 🦔总结规律
# 异常匹配是从上到下顺序匹配的
# 子类异常会匹配父类 except，但前面的 except 优先
# 如果你写成：
for c in [B, C, D]:
    try:
        raise c()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")
# 输出 B B B
# 当抛出 C 或 D 时，会先被 except B 捕获
# 这就是为什么通常 要把子类 except 写在父类 except 之前




# 🐟小结口诀
# “先子类，后父类；先上面的 except，后下面的 except”
# 遵循这个顺序，就不会出现异常被“吃掉”而匹配到父类的情况。
