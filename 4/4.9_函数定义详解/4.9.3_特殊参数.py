# /前面是位置参数  *后面是关键字参数 
# /  * 之间随意

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2)

#参数不要重复赋值！！！
# def foo(name, **kwds):
#     return 'name' in kwds
#foo(1,**{'name':2}) 
# 会报错 因为name重复赋值了
#  神奇的是 为什么字典会和关键字name冲突呢？不会自动识别是字典吗？
#  会先识别出name=2和name=1冲突了！都来不及去送给字典！！！就报错了！！！

# ✅ 练习题 1
def f(a, **kwargs):
    print(a, kwargs)
f(1, **{'a': 2})
# 💡 解释：
# 1 作为位置参数给了 a
# **{'a': 2} 又想给 a，重复了！
# Python 报错：TypeError: f() got multiple values for argument 'a'




# ✅ 练习题 2
def f(a, /, **kwargs):
    print(a, kwargs)
f(1, **{'a': 2})
# 💡 解释：
# a 是“仅限位置参数” /
# 1 赋值给 a
# {'a': 2} 不会再试图传给 a，而是当作 kwargs
# 打印：1 {'a': 2}



# ✅练习题 3
def f(*, a, b):
    print(a, b)
f(a=1, b=2)
# 💡 解释：
# 函数以 * 开头，表示：后面所有参数必须使用关键字传入
# f(a=1, b=2) 符合要求，没问题！



# ❌ 练习题 4
def f(*, a, b):
    print(a, b)
f(1, 2)
# 💡 解释：
# 有 *，就必须写成 a=xxx, b=xxx
# 不能传位置参数
# 报错：TypeError: f() takes 0 positional arguments but 2 were given



# ✅ 练习题 5
def f(a, b):
    print(a, b)
f(1, **{'b': 2})
# 💡 解释：
# **{'b': 2} 会被拆成 b=2，其实是“关键字参数”的传值方式
# 所以和 f(1, b=2) 是完全等价的 ✅
# 📌 Python 的规则是：
# **字典 可以把字典中的每个键值对拆解成 key=value 形式传给函数
# 不管你有 1 个还是 100 个参数，都可以这样传，只要 key 是字符串，value 是任意值。



# ❌ 练习题 6
def f(a, b):
    print(a, b)
f(1, **{'a': 2})
# 💡 解释：
# 1 已经赋给了 a
# **{'a': 2} 又试图给 a
# 两次赋值 → 冲突 → 报错：TypeError: f() got multiple values for argument 'a'

