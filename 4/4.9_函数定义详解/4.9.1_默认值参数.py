# def greet (name,lang='en'):
#     if lang=='en':
#         print(f"hello {name}")
#     elif lang=='cn':
#         print(f"你好 {name}")
#     else:
#         print(f"sorry,I don't speak {lang} yet" )
# greet('lily')
# greet('zeze','en')
# greet('健次','cn')
# greet('bal','ze')




# def ask_ok(prompt, retries=4, reminder = 'Please try again!'):
#     while True:
#         reply = input(prompt)
#         if reply in {'y','ye','yes'}:
#             return True
#         if reply in {'n','no','nop','nope'}:
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user responese')
#         print(reminder)
# ask_ok('Ok to overwrite the file?',2,'come on,only yes or no!')


i = 5
def f(arg=i):
    print(arg)

i=6
f()
f(8)

#重要警告： 默认值只计算一次。
# 默认值为列表、字典或类实例等可变对象时，会产生与该规则不同的结果。
# 例如,下面的函数会累积后续调用时传递的参数：
def f(a,L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def f(a,L=None):
    if L is None:
        L=[]    
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
print(f(4,['zeze','2']))