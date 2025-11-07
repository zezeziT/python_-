# 操作系统接口 ： os/ pathlib / shutil
# os 管理系统，pathlib 管路径，shutil 干搬家。

# ➡️核心用途
#   os: 进程与环境、路径、目录/文件操作、权限、进程号等。
#   pathlib：面向对象的路径操作（推荐，易读可跨平台）。
#   shutil：更高层的文件/目录拷贝、移动、压缩等。

# ➡️注意
#   使用import os （不要 from os import *），避免把内建open() 和os.open()搞混；
#   两者语义不同（os.open是底层POSI风格，返回文件描述符）。

# ➡️示例：常见文件操作（跨平台写法）
import os
from pathlib import Path
import shutil

print(os.getcwd())  # 当前工作目录

# 1） 使用 pathlib 处理路径（推荐）
# 路径操作（pathlib）
p = Path("sandbox")         # 相对路径对象
p.mkdir(exist_ok=True)      # 创建目录 （若已存在不报错）
file_path = p / "hello.txt" # 路径拼接


# 2） 写/读文件 （用内建 open，不要用 os.open）
# 文件操作
file_path.write_text("hello, world!\n", encoding="utf-8")
print(file_path.read_text(encoding="utf-8"))



# 3） 列出目录内容
# 目录操作
print([child.name for child in p.iterdir()])


# 4) 复制/移动/删除(shutil)
# 搬家（shutil）
shutil.copy(file_path, p / "hello_copy.txt")        # 复制文件
shutil.move(str(p / "hello_copy.txt"), "hello.moved.txt")   #移动到工作目录

# 删除
shutil.rmtree(p)        # 删除整个目录树（小心！）
os.remove("hello.moved.txt")



# ➡️其他零散的函数 → 知道在哪查就行
#   环境变量 → os.environ / os.getenv()
#   CPU/进程信息 → os.getpid() / os.cpu_count()
#   运行外部命令 → subprocess.run(...)（比 os.system 好）


