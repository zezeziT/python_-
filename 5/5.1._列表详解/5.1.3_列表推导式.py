# 📌 列表推导式
# 对序列或可迭代对象中的每个元素应用某种操作，用生成的结果创建新的列表；或用满足特定条件的元素创建子序列。

# 创建平方值的列表
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
# 这段代码创建（或覆盖）变量 x，该变量在循环结束后仍然存在。
print(x)


# 无副作用地计算平方列表
squares = [y**2 for y in range(10)]
print(squares)
# print(y) # 会报错  y is not defined ；y是内部变量，用完后自动销毁



# 📌 map() 与生成器
#map() 把一个函数f应用到一个序列（或其他可迭代对象）中的每个元素上，返回一个新的迭代器
# 感觉返回的像range（） 也是一个可迭代对象  需要辅助才能显示出现 eg list（range（））

# ❗❗❗什么都没有,map返回的懒惰对象，是一种“可迭代对象”，本质上是个生成器（iterator）
# ❗❗❗错误！！ squares = map(lambda x:x**2,range(10))
# ❗❗❗        squares = [<map 对象>]   # 只是把 map 包装进了列表里！不是计算结果！
# ❗ 所以用list（map（））
squares=list( map(lambda x:x**2,range(10)))
print (squares)




# map(function, iterable)
# ❗❗❗把 func 应用到 iterable 中的每个元素上，返回一个**“懒惰的”可迭代对象**（不是列表！）。
# ❗❗❗它不立刻执行所有运算，而是返回一个“迭代器”，你必须“拉”它一把（比如用 list()、for 循环等）它才会真正跑出来结果。
def square(x):
    return x**2
nums = [1,2,3,4]
result=map(square, nums)
print(list(result))
# 就可以写成匿名函数（lambda）
result = map(lambda x : x**2, [1,2,3,4])
print(list(result))




# ❗列表表达式
# 包含：一个表达式，后面为一个for子句，然后是0个或多个for 或 if 子句 
# 结果是由表达式依据for 和 if 子句求值而得出新列表

s=[(x,y ) for x in [1, 2, 3] for y in [3, 1, 4] if x!=y]
print(s)
# 把s外面的 [] 换成 ()：
# 不会报错  输出：<generator object ...>
# 但是结果不是列表，而是生成器对象
# 你需要用 list() 或 for 才能取出值

# ((x, y) for x in [1,2,3] for y in [3,1,4] if x != y)
# 这是 生成器表达式（generator expression），不是元组！
# 外面的 () 在这里不是在“构造元组”
# 而是 Python 的语法规定：使用括号 () 包住推导式，就会变成一个生成器

#       表达式	                实际含义
#  [(x, y) for ...]	    列表推导式，结果是列表
#  ((x, y) for ...)  	生成器表达式，结果是生成器
#  ((1, 2), (2, 3))  	手动写的元组，含两个元组元素

# ❗生成器表达式
lst = [(x, y) for x in [1, 2] for y in [3, 4]]
gen = ((x, y) for x in [1, 2] for y in [3, 4])

print(lst)          # [(1, 3), (1, 4), (2, 3), (2, 4)]
print(list(gen))    # [(1, 3), (1, 4), (2, 3), (2, 4)]
print(list(gen))    # [] 因为生成器用一次就没了





# 等价于

# combs= ()会报错 因为元组不支持 .append
# [] 是“可以增长”的列表，支持 .append()；
# () 是“固定不变”的元组，不支持 .append()，如果你写了 combs = ()，就不能往里加东西了！

combs= []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))
print(combs)


# combs[0][0]=9 #会报错 元组不可变
combs[0]=(9,9) #正确  list可变
print(combs[0])
print(combs)



# 📌 元组 vs 列表
# [(x,y)]  与  [[x,y]]
# () 代表的是元组：固定组合，不可修改  ，所以 [(x, y)] 是 “一组固定搭配的数据”,比如可以用来表示坐标,配对之类的
# [] 代表的是列表：可以自由添加、修改   ，而 [[x, y]] 是 “可以随时改动的结构化数据”  如果你是做嵌套结构，比如“学生成绩表”、“二维表格”，就用 [[x, y]]
# 如果你想省内存、处理超大数据，可以用 ()（生成器推导式）
# 如果你就想立刻拿到结果、反复使用，还是用 []（列表推导式）
a = [(1,2)]
b = [[1,2]]

#尝试修改
#a[0][0]=100  # ❌ 报错：元组不能改
a[0]=(9,9)    # ✅ 成功 list可改 
b[0][0]=100   # ✅ 成功
print(a,b)




# 📌📌📌再做一些实践
vec = [-4, -2, 0, 2, 4]
# 新建一个将值翻倍的列表
L0= [x*2 for x in vec]
print(L0)

# 过滤列表以排除负数
L1 = [x for x in vec if x >= 0]
print(L1)

# 对所有元素应用一个函数
L2 = [abs(x) for x in vec] #abs(x) 是 Python 内置的绝对值函数,用来返回数字 x 的绝对值
print(L2)

# ❗❗❗在每个元素上调用一个方法
# .strip()
# ✅ 去除字符串首尾空白，也就是 strip() 方法，和 列表推导式 配合用。
# 🔸 .strip() 是字符串的一个方法
# 👉 它的作用是：去掉字符串开头和结尾的空格（包括换行符 \n、制表符 \t 等）。
# 👉 不会改动中间的空格。
freshfruit = {'  banana', '    loganberry', 'passion fruit'}
s=[weapon.strip() for weapon in freshfruit]
print(s)


# 创建一个包含（数字 平方）2 元组的列表
sq= [(x, x**2) for x in range(10)]
print (sq)


# 使用两个 ‘for’ 来展平嵌套的列表
vec = [[1,2,3], [4,5,6], [7,8,9]]
f=[y for x in vec for y in x]
print(f)

# 等价
ll=[]
for x in vec:
    for y in x:
        ll.append(y)
print(ll)

# 这样出来是每一个元素 而每一个元素是一个元组整体的
zeze= [x for x in [(1,2),(3,4),(5,6)]]
print(zeze)
# 要想展平 需要对x进行一次遍历展开
zeze =[y for x in [(1,2),(3,4),(5,6)] for y in x]
print(zeze)



# 列推导式可以使用复杂的表达式和嵌套函数
# 逐步拆解：
# from math import pi
# 导入数学常量 π（圆周率，约等于3.1415926535...）。
# 列表推导式 [str(round(pi, i)) for i in range(1, 6)]
# range(1, 6) 生成数字序列：1, 2, 3, 4, 5
# 对每个 i，计算 round(pi, i)，就是把 π 四舍五入到第 i 位小数
# 再用 str() 把数字转成字符串
# 最终生成一个字符串列表，包含 π 不同精度的表示。
from math import pi
p=[str(round(pi, i)) for i in range (1, 6)]
print(p)
# round(x, n) 的作用是把数 x 四舍五入到小数点后 n 位。