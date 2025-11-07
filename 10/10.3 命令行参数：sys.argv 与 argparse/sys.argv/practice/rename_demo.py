# 例子 2️⃣：批量重命名文件（演示思路）

# rename_demo
import sys
import os

prefix = sys.argv[1]    # 新前缀
for i, filename in enumerate(os.listdir('.'), 1):
    if filename.endswith('.txt'):
        new_name = f"{prefix}_{i}.txt"
        os.rename(filename, new_name)
        print(f"{filename} -> {new_name}")

# 终端： py rename_demo.py project
