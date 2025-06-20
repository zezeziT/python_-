tel = {'jack': 4098, 'sape': 4219}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
print(tel)

tel['irv']= 4127
print(tel)

s=list(tel)
print(s)

s1=sorted(tel)
print(s1)

# sorted(可迭代对象) 返回一个“排好序的新列表”
# 原对象不会被修改
# 返回结果是一个list，不管你传入的是set、list、字符串、元组
zz = set('abracadara')
zz1 = sorted(zz)
print(zz1)

#  重点
#  sorted() 永远返回一个新 list
#  如果你想“原地排序”，list 可以用 .sort() 方法（但是 set 没有 .sort() 方法，因为 set 本来就无序）
L=['s','d','P','p','g']
L.sort()  # .sort() 改变原列表
print(L)
L1 = sorted(L)  # 形成有序新列表
print(L1)


# dict() 构造函数可以直接用键值对序列创建字典
#
D=dict([('space', 4139),('guido', 4127),('jack', 4098)])
print(D)

# 字典推导式可以用任意键值表达式创建字典：
#
D={x: x**2 for x in (2, 4, 5)}
print(D)

# 关键字是比较简单的字符串时，直接用关键字参数指定键值对更便捷：
s = dict(sape=4139, guido=4127, jack=4098)
print(s)


# 5种常用的dict字典创建方法

# ① 直接用大括号 {} —— 最常用
d = {'sape': 4139, 'guido': 4127, 'jack': 4098}
print(d)


# ② 用 dict() + 关键字参数
d = dict(sape=4139, guido=4127, jack=4098)
print(d)



# ③ 用 dict() + 列表 [()] 或元组 (()) 里面放 (key, value) 二元组
d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d)
# 或者：
d = dict((('sape', 4139), ('guido', 4127), ('jack', 4098)))
print(d)


# ④ 用 dict() + zip() —— 两个列表配对成字典
# 👉 zip 把两个列表“拉链”配对，非常好用！
names = ['sape', 'guido', 'jack']
numbers= [4139, 4127, 4098]

d = dict(zip(names,numbers))
print(d)


# ⑤ 字典推导式（dict comprehension）
d = {x: x**2 for x in (2, 4, 5)}
print(d)
# 输出 {2: 4, 4: 16, 5: 25}


# 总结表
#     方法	                      适用场景
# {} 大括号	                    最简单、最常用
# dict(关键字参数)    	      key 是合法英文单词时
# dict([(), (), ()])         	有二元组数据（如数据库数据）
# dict(zip(list1, list2)) 	    两个列表合并成字典
# {k: v for ...}	            动态生成 dict，含计算