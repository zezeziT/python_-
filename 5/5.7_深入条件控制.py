# 1️⃣ in 和 not in —— 检查成员关系
a =[1, 2, 3, 4]
print(1 in a) # True
print(5 not in a) # True
print(6 in a) # False

s = "hello"
print ('e' in s) # True
print ('x' not in s) # True
print('j' in s) # False



# 2️⃣ is 和 is not —— 判断是否是同一个对象
# 作用：判断两个变量是不是引用同一个对象（“身份”），不是值是否相等！
a = [1, 2]
b = [1, 2]
print(a==b)   # True   ----值相等 
print(a is b) # False  ----不是同一个对象(两个list)

c = a
print(a is c) # True   ----c 和 a是同一个对象


# 3️⃣ 链式比较 —— 多个条件串起来
a = 1
b = 2
c = 2

print(a < b==c)  # True
# 等价于 ：(a < b) and (b == c)  很自然的写法！不用写 and。


# 4️⃣ 布尔运算符 and, or, not
# 优先级 not > and > or
A = True
B = False
C = True

print(A and not B or C)
# 等价于： (A and (not B)) or C
# 结果：True


# 5️⃣ 短路运算符 and 和 or
# 👉 “短路” 是指：如果能提前知道结果，就不会再继续算了，节省时间。

# and :  有False 则 False
print(1 and 0 and 3)  # 0
# or :  有 True 则 True
print(0 or 2 or 3)    # 2

# 例子(短路效果)
def f():
    print("f 被执行了")
    return True
False and f()  # f() 不会被执行，短路了 ！ 因为false导致直接输出false 然后停止了
True  and f()  # f() 会被执行


# 6️⃣ or 可以作为“默认值”选择器
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)  # Trondheim
# 👉 因为 or 会返回第一个“为真”的值，空字符串算 False，'Trondheim' 是 True，第一个非空的返回。



# 7️⃣ 海象运算符 := （Python 3.8+）
# 作用：可以在表达式内部赋值。
if (n := len([1,2,3,4,5])) > 3:
    print(n)
#  相当于先 n = len(...)，然后再判断
# C 语言里容易写成 = 错误，Python 需要 := 才允许在表达式里赋值，更安全。
# 这避免了 C 程序中常见的问题：要在表达式中写 == 时，却写成了 =。


# 你心里想的流程是对的：
n = len(...)
if n > 3 :
    pass

# 但是，Python 语法规定：
# if () 里必须是表达式，不能是赋值语句
# 如果想赋值 + 比较，必须用 :=

if (n := len(...)) > 3:   # 这就合法





# 🌟 总结小抄：
#   语法	              作用	                     例子
# in / not in	       检查成员关系	              'a' in 'abc'
# is / is not	    判断是否同一个对象	             a is b
# 链式比较	             多条件连写	               a < b == c
# and or not	         逻辑运算	              x and not y
# 短路	提前终止    	True or f()                 不执行 f
# or 选择器	            取第一个非空               x or y or z
# :=	                赋值表达式	        if (n := len(a)) > 3:




#
# and、or 在 Python 里其实 不仅仅返回 True / False，而是会 “返回值”！
# 👉 and 返回 第一个为 False 的值（如果没有，就返回最后一个）
# 👉 or 返回 第一个为 True 的值（如果没有，就返回最后一个）
# 它们并不是强制返回 True / False —— 而是返回 “它们遇到的值” 本身
# 🌟 总结口诀
# and：遇 False 停，返回 False 值；都 True，返回最后一个
# or ：遇 True 停，返回 True 值；都 False，返回最后一个
