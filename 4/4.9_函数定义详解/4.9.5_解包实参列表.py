# 可通过解包*元组/列表  **字典 传入参数

#* 是把「列表或元组」拆开当成位置参数传进函数
#** 是把「字典」拆开当成关键字参数传进函数

# *元组/列表 （位置参数）
s1=list(range(2,4))

# *args 就是把2，4传入了（2，4）
args=[2,4]
s2=list(range(*args))

# **
def f(name,hobby,hair):
    print(name+"\n"+hobby+"\n"+hair)

d={"name":"JC-T",
   "hobby":"sing  dance  perform",
   "hair":"black"
   }
# **d 解包字典传关键字参数（关键字参数）
# 相当于name=JC-T...
f(**d)