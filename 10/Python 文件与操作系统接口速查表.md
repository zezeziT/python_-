# 📝 Python 文件与操作系统接口速查表

## 1. `os`（系统级操作）
```python
import os

os.getcwd()           # 当前工作目录 (get current working dir)
os.chdir("path")      # 切换目录 (change dir)
os.listdir(".")       # 列出目录内容

os.mkdir("d")         # 创建目录
os.rmdir("d")         # 删除空目录
os.remove("f.txt")    # 删除文件

os.environ["PATH"]    # 环境变量字典
os.getenv("HOME", "") # 获取环境变量，没找到给默认值

os.getpid()           # 当前进程号
os.cpu_count()        # CPU 核心数
```

---

## 2. `pathlib`（推荐，面向对象路径）
```python
from pathlib import Path

p = Path("sandbox")     # 路径对象
p.mkdir(exist_ok=True)  # 创建目录，已存在不报错

f = p / "hello.txt"     # 拼接路径（跨平台安全）

f.write_text("hi\n")    # 写文件（自动 open/close）
print(f.read_text())    # 读文件

for child in p.iterdir():   # 遍历目录
    print(child.name)

f.exists()              # 是否存在
f.is_file()             # 是否是文件
f.is_dir()              # 是否是目录
```

---

## 3. `shutil`（高层文件操作）
```python
import shutil

shutil.copy("a.txt", "b.txt")    # 复制文件
shutil.move("b.txt", "backup/")  # 移动/重命名
shutil.rmtree("sandbox")         # 删除整个目录树（小心！）

# 压缩/解压
shutil.make_archive("backup", "zip", "sandbox")  # 打包成 backup.zip
shutil.unpack_archive("backup.zip", "restore")  # 解压到 restore/
```

---

## 4. 小口诀（帮助记忆）
- **os 管系统**（目录、环境变量、进程）  
- **pathlib 管路径**（拼路径、读写文件，更优雅）  
- **shutil 管搬家**（复制、移动、删除、压缩）  
