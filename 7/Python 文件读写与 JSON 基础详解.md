
# Python 文件读写与 JSON 基础详解

## 一、`open()` 函数基本用法

```python
open(file, mode='r', encoding=None)
```
- `file`: 文件路径，字符串。
- `mode`: 文件打开模式（如 'r', 'w', 'a', 'rb', 'wb' 等）。
- `encoding`: 文本模式下的编码方式，推荐使用 `"utf-8"`。

### 示例：写入与读取文本
```python
# 写入
f = open("example.txt", "w", encoding="utf-8")
f.write("Hello, Python!\nThis is a second line.")
f.close()

# 读取
f = open("example.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()
```

---

## 二、使用 `with` 管理文件（推荐）

```python
with open("example.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data)
```

好处：自动关闭文件，避免遗漏关闭或错误关闭。

---

## 三、文件打开模式汇总

| 模式     | 含义                        |
|--------|---------------------------|
| `'r'`  | 读取文本（默认）                   |
| `'w'`  | 写文本，覆盖原文件                 |
| `'a'`  | 写文本，追加                    |
| `'r+'` | 读写文本，不清空内容                |
| `'b'`  | 二进制模式，如 `'rb'`, `'wb'`     |
| `'t'`  | 文本模式（默认）                   |

### 示例：写入二进制数据
```python
with open("binary.dat", "wb") as f:
    f.write(b'\x00\x01\x02')
```

---

## 四、文件读取方法

```python
f.read(size)       # 读取 size 个字符
f.readline()       # 读取一行
f.readlines()      # 读取所有行到列表
for line in f:     # 推荐的逐行读取方式
```

```python
# 逐行读取并 strip
with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

---

## 五、写入方法

```python
f.write(string)        # 写入字符串
f.write(str(object))   # 将对象转为字符串写入
```

---

## 六、文件位置控制

```python
f.tell()  # 获取当前指针位置
f.seek(offset, whence)
# whence: 0=开头, 1=当前位置, 2=结尾
```

### 示例
```python
with open("seek_test.txt", "wb+") as f:
    f.write(b"abcdef")
    f.seek(3)
    print(f.read(1))  # b'd'
```

---

## 七、JSON 操作

```python
import json

# Python → JSON 字符串
json_str = json.dumps(obj)

# JSON 字符串 → Python
obj = json.loads(json_str)

# Python → 写入 JSON 文件
json.dump(obj, file)

# JSON 文件 → Python
obj = json.load(file)
```

---

## 八、字符串 vs 字节串（str vs bytes）

| 表达式        | 类型      | 含义                    |
|-------------|---------|-----------------------|
| `'abc'`     | str     | 字符串，人类可读               |
| `b'abc'`    | bytes   | 字节串，给电脑/磁盘/网络使用         |
| `"w"`       | 文本写入   | 接收字符串                    |
| `"wb"`      | 二进制写入 | 接收字节串                    |

```python
# 字节写入（推荐用于非文本文件）
with open("img.jpg", "wb") as f:
    f.write(b"\x89PNG\x0D\x0A...")
```

---

## 九、print 与 json.dumps 区别

| 方法              | 用途               |
|------------------|------------------|
| `print(data)`    | 方便调试，给人看         |
| `json.dumps()`   | 标准格式，给机器传输/存储使用 |

```python
data = {"name": "小明", "age": 18}

print(data)  # {'name': '小明', 'age': 18}
print(json.dumps(data, ensure_ascii=False))  # {"name": "小明", "age": 18}
```

---

## 十、总结表

| 名词/函数          | 中文解释                          |
|------------------|---------------------------------|
| `f.read()`       | 读取整个文件内容                    |
| `f.write()`      | 写入字符串                        |
| `b'abc'`         | 二进制字节数据                     |
| `strip()`        | 去除字符串前后的空白字符与换行               |
| `seek()`         | 改变读取位置（类似翻页）                 |
| `json.dumps()`   | Python → JSON 字符串             |
| `json.dump()`    | Python → JSON 文件                |
| `json.load()`    | JSON 文件 → Python 对象          |
| `with open()`    | 安全打开文件并自动关闭文件              |
| `f.close()`      | 手动关闭文件                       |
