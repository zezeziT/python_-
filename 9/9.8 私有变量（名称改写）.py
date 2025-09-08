# 1️⃣ 背景：私有变量
# 在很多语言（如 Java、C++）里，类可以有 私有变量，只能在类内部访问。
# Python 没有真正的私有变量，所有属性默认都是公有的。但 Python 有一些约定和技巧，能让属性“不容易被外部访问”。




# 2️⃣ 约定：单下划线 _
class Myclass:
    def __init__(self):
        self._spam=123

# _spam 表示这是 非公有 API，也就是不建议外部访问。
# 但是外部仍然可以访问：

obj = Myclass()
print(obj._spam)  # 输出123

# 单下划线只是“约定”，并不真正限制访问。






# 3️⃣ 名称改写（Name Mangling）：双下划线 __
class Mapping:
    def __init__(self):
        self.__data=[]

# __data 是双下划线开头。
# Python 会把它自动改写为 _Mapping__data，其中 Mapping 是类名。
# 这样可以避免子类覆盖或外部直接访问。

# 4️⃣ 尝试访问

m = Mapping()

# print(m.__data) # 会报错
# 这里报错，因为外部不存在 __data 这个名字。
# Python 内部已经把它改成 _Mapping__data 了。

print(m._Mapping__data)  # 可以访问

# 通过改写后的名字 _Mapping__data，我们可以访问到这个属性。
# 说明双下划线只是防止意外访问，不是真正的私有。




# 5️⃣ 总结
# | 写法       | 意义        | 外部访问方式                 |
# | -------- | --------- | ---------------------- |
# | `spam`   | 公有属性      | `obj.spam`             |
# | `_spam`  | 非公有（约定）   | `obj._spam`（仍可访问）      |
# | `__spam` | 名称改写（私有化） | `obj._ClassName__spam` |
