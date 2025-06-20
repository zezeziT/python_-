#  一个集合不同输出
#set 是“装字母的袋子”，袋子里顺序是乱的，不要期待它有顺序。
#如果需要顺序，自己 sorted(set(...)) 转换一下。
z={'39', 'y', 'uu', 'op'}
print(z)



#
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)  #显示重复项已删除

print('orange'in basket) # 快速成员检测

print('jct' in basket)

# 演示针对两个单词中独有的字母进行集合运算
#
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a-b)  # 存在于 a 但不存在于 b

print(a|b)  # 存在于 a 或 b 或两者中都有的

print(a & b) # 同时存在于 a 和 b

print(a ^ b) # 存在于 a 或 b 中但是非两者皆有的字母


# 与列表推导式类似，集合也支持推导式
#
a = {x for x in 'abcdefgashf' if x not in 'abcd'}
print(a)