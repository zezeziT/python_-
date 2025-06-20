# 当对字典执行循环时，
# 可以用items（）同时提取键及对应值
knights = {'gallahad':'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)


# 在序列的循环中
# 用 enumerate()   函数可以同时取出索引和对应的值
L=[1,5,8,3,'zeze']
for i,v in enumerate(L):
    print(i,v)


# 同时循环两个或多个序列时
# 用zip(L1,L2,L3...)可以将其内的元素一一匹配
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    # .format(q, a) 是字符串格式化 —— 用 q 和 a 来“填空”
    # 里面的 {0} → 位置 0 → 会被 q 替换
    # {1} → 位置 1 → 会被 a 替换
    print('what is your {0}? it is {1}'.format(q,a))
  
    # 这种通俗易懂一点
    print(f'what is your {q}? it is {a}.')




# 🌟 zip() 是什么？
# zip() 是一个内置函数，用来把多个“可迭代对象”（比如列表、元组、字符串）按“对应位置”配对，组合成一个“迭代器”。

# 就像拉拉链一样，把多个序列的相同位置的元素拉到一起，组成一个个“对”。


# 🌟 zip() 的用法

# zip(iterable1, iterable2, ... )
# iterable：可迭代对象（列表、元组、字符串都可以）

# 返回值：一个 zip 迭代器（可以用 list(), dict(), set() 转换成你想要的结果）




# 为了你逆向对序列循环, 可以求出欲循环的正向序列，然后调用reversed()函数
for i in reversed(range(1,10,2)):
    print(i)


# 按指定顺序循环序列，可以用 sorted() 函数，在不改动原序列的基础上，返回一个重新的序列
basket = ['appele', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)


# 使用set()去除序列中的重复元素 
# 使用 sorted() 加 set() 则按排序后的顺序，循环遍历序列中的唯一元素
basket = ['appele', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
    print(i)



# 一般来说，在循环中修改列表的内容时，创建新列表比较简单，且安全
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8, 'NaN']
s= [x for x in raw_data if x != 'NaN'] #float('NaN')是一个特殊的 浮点数值 NaN（不是字符串 'NaN'），所以判断 x ！=’NaN‘ 永远不会为识别到 浮点数NaN  它只能过滤字符串'NaN’
print (s)

# 再来
# 应该用 math.isnan(x) 来判断 NaN：
import math
raw_data = [56.2, float('nan'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data :
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)


