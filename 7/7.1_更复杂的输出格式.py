#1️⃣ Python 输出的几种方式

print("hello", 123, True, False)

print('A', 'B', sep= '-', end = '!\n')

print("A", "B", sep = "分隔符", end = '---结束----（无“\\n”下一行不换行）----', )

# 初始值sep=' '  默认是空格
print("99",'zeze', 'jct')

print(2)  #  因为上一个end替代了原来的\n换行  所以2没有换行

print(33)


# 使用 write() 方法（底层方式）
import sys
sys.stdout.write("hello\n")



# 2️⃣ f-string：格式化字符串字面值

name = 'meimei'
age = 16
print(f"her name is {name}, she is {age} year old.")


# 可以直接在 {} 里写表达式、函数、方法调用
print(f'{3+2}')
print(f'hi, {'jct'.upper()}')


# 使用格式说明符控制输出
# 示例1：保留小数
import math
print(f"Pi. {math.pi:.3f}")
# 示例2：列对齐（宽度控制）
print(f'{42:5d}')  # :5d 表示用5个字符宽度右对齐 d是整数类型 如果数字不够宽 就用空格填充
print(f'{ 88 :5d}')
# :<5d  左对齐5个宽度
print(f'{22:<5d},lily')
# :^  居中对齐
print(f'{22:^5}')

#  字符串不用加d  
s = 'hi'
print(f'{s:<5}')
print(f'{s:>5}')
print(f'{s:^5}')


# 示例3：百分比
yes = 42
total = 100
print(f"{yes / total :.2%}")  #输出 ： 42.00%
# 📎 速查表参考：按 Ctrl + P 输入 python_formatting_cheatsheet.md 可打开
# 或在 README.md 里点击跳转
# f"{值：[填充符][对齐方式][宽度][,][.精度][类型码]}"




# !s, !r, !a：转换说明符
word = "eels"
print(f"{word}")        # 默认 ： eels
print(f"{word!r}")      # 调用repr():  'eels'
print(f"{word!s}")      # 调用 str() :  eels
print(f"{word!a}")
# 📌 说明：
# !r 会调用 repr()，加引号。  适合调试、日志记录，让你一眼能看出数据类型（比如 'None' 和 None 是不一样的）。
# !s 会调用 str()，正常显示。 适合展示给用户看的内容。
# !a 会调用 ascii()，显示 ASCII 转义   适合需要转义的情境，比如写入纯 ASCII 文件，或避免非英文字符乱码。

examples = {"eels", "你好", "😀", "123", "None", None}
for word in examples:
    print(f"原始值: {word}")
    print(f"原始值: {word!r} (type: {type(word).__name__})")
    print(f"str:    {word!s}")
    print(f"repr:   {word!r}")
    print(f"ascii:  {word!a}")
    print("---")



# = 表达式自说明（调试神器）
x = 3
print(f"{x=}")   # 输出：x=3
print(f"x={x}")
# 输出变量名 + 值，非常适合调试。
#
# 它可以用于更复杂的表达式，比如：
x = 3
y = 5
print(f"{x + y =}")
print(f"{x * y =}")
print(f"{x > y =}")
print(f"{len('hello')=}")  # 输出 len('hello')=5
# 非常适合用于调试时快速查看变量或表达式的值，而且不需要你手动拼接字符串。





# 3️⃣ str.format() 方法（早期格式化方式）
# ✅3.1 最基本的写法
print("hello,{}".format("world"))
# {} 是占位符，会被 .format() 传入的值替换。
# 多个值按顺序对应多个 {}。

# ✅ 3.2 指定位置参数
print("{1} and {0}".format("spam", "eggs"))
# {0} 是第一个参数，{1} 是第二个。
# 你可以任意交换顺序


# ✅ 3.3 使用关键字参数
print("This {food} is {adj}".format(food= "spam",adj="bad"))
# 使用 key=value 的方式传参。
# 替换 {food} 和 {adj}。

# ✅ 3.4 混合位置 + 关键字参数
print("Story of {0},{1}, and {other}".format("Bill", "Manfred", other = "Georg" ))
# {0}, {1} 用于位置参数
# {other} 是关键字参数

# ✅ 3.5 字典解包作为参数
table = {"Jack": 4098, "Dcab": 8637678}
print("Jack: {Jack}, Dcab: {Dcab}".format(**table))
# **table 解包字典为关键字参数
# 这样可以按名字引用键

# ✅ 3.6 表格排版案例
for x in range(1,6):
    print("{0:2d} {1:3d} {2:4d}".format(x, x*x, x*x*x))
# :2d 表示宽度2，整数   
# :3d 宽度3
# :4d 宽度4
# 用于表格排版对齐



# 4️⃣ 手动对齐方法（字符串方法）
# ✅ str.rjust(width)
print("7".rjust(3)) # '  7'
# 右对齐，左边补空格

# ✅ str.ljust(width)
print("7".ljust(3)) # '7  '
# 左对齐，右边补空格

# ✅ str.center(width)
print("7".center(3)) # ' 7 '
# 居中对齐

# ✅ zfill(width)
print("-42".zfill(5))  # '-0042'
# 填充 0 而不是空格
# 保留负号




# 5️⃣ str() 与 repr() 的区别
s = 'Hello'
print(str(s))   # hello     用户可读的展示          日常输出
print(repr(s))  # 'hello'   开发者可读，含引号      调试，数据结构打印



# 6️⃣string.Template (模板字符串)
from string import Template
t = Template("Hello, $name!")
print(t.substitute(name = "Alice"))
# $变量名  占位符
# 通过 .substitute 替换变量
# 功能简单，不支持对齐或小数精度控制



# 7️⃣ % 旧式格式化方法（兼容 C 风格）
import math
print("Pi: %.3f" % math.pi)  # Pi: 3.142
# 📌 说明：
# %f 浮点数格式
# %.3f 表示保留三位小数
# %d 整数；%s 字符串

# ✅ 多值格式化
print("Name: %s, Age: %d" % ("Bob", 25))
