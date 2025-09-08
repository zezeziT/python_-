# 生成器自动实现迭代器协议。
def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]

for char in reverse('golf'):
    print(char)


# 生成器表达式：

sum(i*i for i in range(10))  # 285

# 优点：节省内存、自动保存状态。