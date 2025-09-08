# 反向迭代
class Reverse:
    def __init__(self,data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
rev = Reverse('spam')
for char in rev:
    print(char)

print("-------------------------------------")

# 简单计数器迭代
class Counter:
    def __init__(self,n):
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.n:    
            raise StopIteration
        self.current += 1
        return self.current
for x in Counter(5):
    print(x)



print("-------------------------------------")


# 自定义返回规则
class SkipTwo:
    def __init__(self, data):
        self.data = data
        self.pos = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.pos >= len(self.data):
            raise StopIteration
        val = self.data[self.pos]
        self.pos += 2
        return val

for s in SkipTwo([10,20,30,40,50]):
    print(s) 



print("-------------------------------------")

# 无限迭代
class Infinite:
    def __init__(self):
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.num += 1
        return self.num
    
it = Infinite()
print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # 3

