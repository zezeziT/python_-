class Dog:
    tricks = []

    def __init__(self,name):
        self.name=name
    
    def add_trick(self,trick):
        self.tricks.append(trick)


dog1 = Dog("檀小呆")
dog2 = Dog("檀力球")
print(dog1.tricks)  # 输出 []
print(dog1.name,dog2.name)

dog1.add_trick("喜欢鸭子")
dog2.add_trick("喜欢白色的东西")
print(dog1.tricks,"\n")
print(dog2.tricks,"\n")
print(Dog.tricks,"\n")   
# 输出都是 ['喜欢鸭子', '喜欢白色的东西']   





# 类变量最好不要用可变对象 如列表 字典等
# 本来应该是 dog1 喜欢鸭子  dog2 喜欢白色的东西 分开的  
# 更正

print("----------------------------------------------")
print("----------------------------------------------")
print("----------------------------------------------")
# 类定义
class DDog:  
    tricks=[]    # 类变量
    def __init__(self,name):
        self.name=name
        self.tricks=[]   # 实例变量
    
    def add_trick(self,trick):
        self.tricks.append(trick)

dog3 = DDog("呆呆")
dog4 = DDog("球球")
print(dog3.name,dog4.name)
print(dog3.tricks,dog4.tricks,DDog.tricks)





print("----------------------------------------------")
# 仅让类变量有值
# dog3.tricks有自己的实例变量为[]! 是可以输出的
DDog.tricks.append("爱爸爸")
print(dog3.tricks,dog4.tricks,DDog.tricks)  





print("----------------------------------------------")
# 往实例里添加
dog3.add_trick("爱鸭子")
dog4.add_trick("爱白色")
print(dog3.tricks,dog4.tricks,DDog.tricks)






# 清空实例变量列表
# clear() 是在 原地修改实例变量的列表对象。
# 列表依然存在，只是长度变成 0。
# dog3.tricks 依然是实例变量，不会“退回”类变量。
# 💡 关键点：即便是 []，也表示“实例变量存在，只是内容为空”。
print("----------------------------------------------")
dog3.tricks.clear()
print(dog3.tricks)  # 输出为 “ [] ”





# 删除实例变量
# del 是把 dog3.__dict__ 里的 "tricks" 键删掉了。
# 再访问 dog3.tricks 时，Python 在实例里找不到，于是去类里找 → DDog.tricks → ['爱爸爸']。
# 💡 关键点：删除和清空不同，删除是属性不存在，清空是列表还在只是空的。
print("----------------------------------------------")
del dog3.tricks
print(dog3.tricks)  # 输出为 “ ['爱爸爸'] ”



