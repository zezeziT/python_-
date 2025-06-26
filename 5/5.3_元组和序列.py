#
t = 1245, 54321, 'hello！'
print(t)

#元组可以嵌套
u = t, (1, 2, 3, 4, 5)
print(u)

#元组是不可变对象 会报错
#  t[0]=99
#     ~^^^
# TypeError: 'tuple' object does not support item assignment

#但是元组可以包含可变对象
v =([1, 2, 3,],(9, 9, 0))
print(v)
v[0][2]=99  # v[0]是列表 可变
print(v)
#v[1][0]=88  会报错 因为v[1]是元组 ，不可变

#构造 0 个或 1 个元素的元组比较特殊：为了适应这种情况，对句法有一些额外的改变。
# 用一对空圆括号就可以创建空元组；
# 只有一个元素的元组可以通过在这个元素后添加逗号来构建（圆括号里只有一个值的话不够明确）。丑陋，但是有效。例如：
empty = ()
singleton = 'hello' ,
print(len(empty))
print(len(singleton))
print(singleton)
jct=('zez'  ,  'lily',   'jct')
print(jct)

#语句 t = 12345, 54321, 'hello!' 是 元组打包 的例子：
# 值 12345, 54321 和 'hello!' 一起被打包进元组。
# 逆操作也可以：
# 序列解包！
x,y,z = jct
print (x,y,z)