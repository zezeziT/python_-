#关键字参数

def parrot(voltage, state = 'a staff', action='voom',tpye='Norwegian Blue'):
    #end=''  意思是下句print不换行 直接接上
    print("-- This parrot wouldn't", action,end=' ')
    print("if you put",voltage, "volts through it.")
    print("-- Lovely plumage, the", tpye)
    print("-- It's", state, "!")

#必须接受一个voltage参数  因为它没有默认值  其他几个参数有没有无所谓 因为有默认值

# 1个位置参数
parrot(1000)

# 1个关键字参数
parrot(voltage=1000)

# 2个关键字参数
parrot(voltage=1000000, action='VOOOOOM')

# 2个关键字参数  当带关键字时，顺序不影响，可以随意
parrot(action='VOOOOOM', voltage=1000000)

# 3个位置参数  和parrot函数里面的参数位置一一对应
# 即默认 voltage='a million' state = 'bereft of life', action='jump',
parrot('a million', 'bereft of life', 'jump')

# 1个位置参数 1个关键字参数
parrot('a thousand', state = 'pushing up the daisies')


### 🟥❌以下调用函数的方式都无效

# ❌ 缺少必须的参数 因为voltage没有默认值 所以必须有输入！
#parrot()

# 位置参数不能出现在关键字参数之后
# ❌ 错误：关键字参数后面不能跟位置参数！ 这是 Python 的语法规定。
#parrot(voltage=5.0, 'dead')

# ❌ 错误：不能重复赋值 voltage 赋值了两次（一次是 110，一次是 220）
#parrot(110, voltage=220)

# ❌ 错误：函数参数里没有 actor 这个名字，不能瞎写！
#parrot(actor='John Cleese')

# 🟥对同一参数多次赋值错误例子
# def function(a):
#     pass
# function(0,a=0)
# 会报错❌TypeError: function() got multiple values for argument 'a'



### 形参*name--元组    **name--字典   
### 组合使用时，*name必须在**name前
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry,we're all out of", kind)
    #可以直接打印元组
    print("arguuments:",arguments)

    #遍历元组
    for arg in arguments:
        print(arg)
    print("--" *40)

    #可以打印字典
    print("**keywords:",keywords)
    #遍历字典
    for kw in keywords:
        print(kw,":",keywords[kw])

cheeseshop("Limburger", 
           #会自动和元组对应形成元组
           "It's very runny, sir.",
           "It's really very ,VERY RUNNY, sir.",
           #会自动和字典对应形成字典
           shopkeeper = "Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
    

def star(name, *actor, **singer):
    print(name,":")
    print("电视剧作品：",actor)
    for k,v in singer.items():
        print(f"{k}:{v}")
    
star("檀健次","《很想很想你》","《猎罪图鉴》","《长相思》","《四方馆》",
     Dreams="IMMA GET IT， 一念无明，枷锁",
     焕="蒙娜丽莎，烧掉，那些萤火，炙暗时刻")

