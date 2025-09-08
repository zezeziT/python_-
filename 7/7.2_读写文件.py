# Write
f = open ("example.txt", "w", encoding="utf-8")
f.write("hello, Python!\n")
f.write("This is a second line")
f.close()

# Read
f = open ("example.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()


# with 自动关闭文件
with open ("example.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data)
# 此处自动关闭文件


# a 写文本追加
with open ("example.txt", "a", encoding= "utf-8") as f:
    f.write("这是追加的内容.")
    f.write("这是追加的内容\n")
    f.write("这是追加的内容\n")   # 每一句换不换行根据上一句是否有换行符号\n



# wb b 二进制写入
with open ("binary.dat", "wb") as f:
    f.write(b'\x00\x01\x02') # 必须写bytes 对象

with open("binary.dat", "rb") as f:
    print(f.read())




# 读取方法详解
# 1 read(size) :读取真个文件或指定字符数
with open("example.txt", "r", encoding="utf-8") as f:
    print(f.read(5)) # 读取前5个字符

# 2 readline() : 读取一行（包含换行符）
with open ("example.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    print(line1, end='') # 自动保留\n
    print(line2)
    print(line3, end = '') 


# 3 readlines()/ list(f): 读取所有行，结果是列表
with open("example.txt", "r", encoding="utf=") as f:
    lines = f.readlines()
    print(lines)

    print(list(f.read()))  # 输出空[] 因为文件已经读完了指针在文件末尾
    f.seek(0) # 回到开头
    print(list(f.read()))  # 现在能读到东西了
    # .read() 是个“大串”，list(f.read()) 是“一个一个拆开来的小字”，



# for line in f: ：推荐的逐行读方式（节省内存）
with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # 去掉末尾的\n

    f.seek(0)
    for line in f:
        print(line)   
        # 因为print会自带"\n",   再加上line自由的‘\n’  所以中间空了一行




# 写入方法
# 1  write(string): 写入文本，返回写入字符数
with open("write_test.txt", "w", encoding= "utf-8") as f:
    chars = f.write("Teat line.\n")
    print(chars) # 输出写入的字符数

# 2 写入非字符串对象要转换为字符串
value = ('pi', 3.14)
with open("tuple.txt", "w", encoding="utf-8") as f:
    f.write(str(value)) # 写入字符串形式的元组



# 文件位置控制
# f.tell(): 获取当前文件的指针位置（字节或字符）
with open("example.txt", "r", encoding="utf-8") as f:
    print(f.tell())  # 一开始是0  
    f.read(5)
    print(f.tell())  # 指针已向后移动


# f.seek(offset, whence)  设置文件指针位置
# offset：偏移量（可以是正数或负数）；
# whence：起点位置（从哪里开始偏移）：
# whence=0：从文件开头（默认）
# whence=1：从当前位置
# whence=2：从文件结尾

with open ("exampleseek.txt", "rb") as f:
    f.seek(0,0) # 从开头偏移0
    print(f.read(5))  #读出“hello”

    f.seek(2,0) #从开头偏移两个字符
    print(f.read(5))  # "llo, "

    f.seek(0,2)  # 跳到结尾
    print(f.read()) # 空，已经在结尾

    f.seek(-6, 2) # 从结尾往前数6个字符
    print(f.read())  # 读出“world!”
# ❗注意：
# ⚠ whence=1 和 whence=2 通常只在 二进制文件 模式下使用！
# 文本模式（"r"）下用 seek(offset, 1) 和 seek(offset, 2) 可能不太准确，尤其涉及多字节字符（中文、emoji）；
# 如果你真的要用 whence=1 或 2，请使用二进制模式打开文件

with open("seek_test.txt", "wb+") as f:
    f.write(b'abcdef')
    f.seek(3)  # 移动到第4个字节
    print(f.read(1) ) # 读取b‘d’





# 适用json 保存结构化数据
# f.write() 只能写字符串
# 想保存字典、列表等结构，用 json 更方便
# 1. json.dumps()：对象转成 JSON 字符串
import json

data = {"name": "Tom", "age": 25}
s = json.dumps(data)
print(s)  # '{"name":"Tom", "age": 25}'




# 2. json.dump(obj, file)：对象 → JSON → 写入文件
import json

data = [1, 2, 3, {'a': 10, 'b': 20}]
with open("data.json", "w", encoding='utf-8') as f:
    json.dump(data, f)


# 3. json.load(file)：从文件读取 JSON 并转成 Python 对象
with open ("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded) # [1, 2, 3, {'a': 10, 'b': 20}]