def my_function():
    """Dn nothing, but document it.
#这样可以对齐
No, really, it doesn't do anything.  

    yes 
    # 这样不能对齐 要想对其需要删除前面的缩进
    """
    pass
print(my_function.__doc__)


# 还可以使用textwrap.dedent()来自动清除缩进


#textwrap.dedent() 是按照以下逻辑清除缩进的：
# 它会找出第一行非空行之后的所有行中最小的“公共缩进量”，把这个最小缩进从所有行里删掉。
# 但是，如果某些行本身缩进更少，或者没有缩进，dedent() 是不会“统一整理”成你想要的对齐效果的。
# 在你的例子中：
# " 要对齐呀" 有 4 个空格
# "在用了清除缩进的函数又手动删了缩进会怎么样" 没有缩进
# 所以 textwrap.dedent() 会判断最小缩进是 0，于是 啥也不删！


import textwrap

# def my_duiqi():
#     """zeze

#     要对齐呀

# 在用了清除缩进的函数又手动删了缩进会怎么样
# #不怎样  因为缩进不一致 函数判断了最小缩进为0 所以啥也不删除
#     """
#     pass
# print(textwrap.dedent(my_duiqi.__doc__))


# 上面那个函数不对齐的情况下会导致下面这个函数也无法对齐

#要想textwrap.dedent()生效  要让想要对齐的缩进一致 就得写的时候一致  函数会删除相同的缩进
# 全部对齐 zeze挪到下一行
def my_f():
    """
    zeze

    lily

    oppp

    jct
    zeze
    """
    pass
print(textwrap.dedent(my_f.__doc__))
print(repr(textwrap.dedent(my_f.__doc__)))
