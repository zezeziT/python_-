# 一、序列之间怎么比较？
# 序列包括：list、tuple、str
# （list、元组、字符串，都叫“序列”）

# 规则：字典式顺序（就像查字典！）
# 👉 一个一个比，遇到不同就能确定大小，不同的话先比“第一个不同的元素”大小。

# 👉 如果有嵌套序列（元组里有元组），递归比较。

# 👉 如果前面都一样，谁更短，谁就“小”。


# 二、例子
l= (1,2,3) < (1,2,4)
print(l)  # True



l= (1,3) < (1,1,5)
print(l)  # 1--1 相同  3---1  3>1 所以左边大 False



l= [1,2,3]<[1,2,3]
print(l)  # False



l=[1,2,3]<[1,2,4]
print(l)  # True



l= 'ABC' < 'C' < 'Pascal' < 'Python'
print(l) # True
# 按 Unicode 码位比较（其实是 ord('A')、ord('C')...）
# A (65) < C (67) < P (80) < P (80)...


l=(1,2,3,4) < (1,2,4)
print(l)  # 1==1 2==2  3 < 4 所以true



l=(1,2) < (1,2,-1)
print(l)  # True
# 前两项一样； 第一个 tuple 结束了 → 较短的 < 较长的； 所以true



l=(1,2,3)==(1.0,2.0,3.0)
print(l)  # True
# 数值类型之间允许比较
# 1 == 1.0 → True
# → True



l=(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
print(l)  # True
# 嵌套 tuple 递归比较
# 'aa' < 'abc' → True



l=(1, 2, ('aa', 'ab')) < (1, 2, ('aa', 'a'), 4)
print(l)  # False



# 三、不同类型对象的比较？

l = 0 ==0.0
print(l)  
# True 因为 Python 允许 int 和 float 自动转换成 float 来比较。


# 不同类型不能比较 会报错
# l = [1,2,3] < 'a,b,c'
# TypeError: '<' not supported between instances of 'list' and 'str'

# l = [1,2,3] < (1,2,5)
# TypeError: '<' not supported between instances of 'list' and 'tuple'


