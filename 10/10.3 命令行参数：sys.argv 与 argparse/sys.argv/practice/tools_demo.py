# 把多种操作放一起
# Python 小工具集合示例，用命令行参数控制不同功能，一份脚本就能做多种操作，非常直观地展示 sys.argv 的用法。

# tools_demo.py
import sys
import os

def add_numbers(args):
    """计算两个数字的和"""
    if len(args) != 2:
        print("用法: python tools_demo.py add num1 num2")
        return
    try:
        num1 = float(args[0])
        num2 = float(args[1])
        print(f"{num1} + {num2} = {num1 + num2}")
    except ValueError:
        print("请输入数字")

def rename_files(args):
    """批量重命名当前目录下的txt文件"""
    if len(args) != 1:
        print("用法: python tools_demo.py rename prefix")
        return
    prefix = args[0]
    for i, filename in enumerate(os.listdir('.'), 1):
        if filename.endswith('.txt'):
            new_name = f"{prefix}_{i}.txt"
            os.rename(filename, new_name)
            print(f"{filename} -> {new_name}")

def search_text(args):
    """搜索data.md中包含关键字的行"""
    if len(args) != 1:
        print("用法: python tools_demo.py search keyword")
        return
    keyword = args[0]
    try:
        with open('data.md', 'r', encoding='utf-8') as f:
            for line in f:
                if keyword in line:
                    print(line.strip())
    except FileNotFoundError:
        print("data.md 文件不存在")

def main():
    if len(sys.argv) < 2:
        print("工具集合用法: python tools_demo.py <命令> [参数...]")
        print("命令: add, rename, search")
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "add":
        add_numbers(args)
    elif command == "rename":
        rename_files(args)
    elif command == "search":
        search_text(args)
    else:
        print(f"未知命令: {command}")
        print("可用命令: add, rename, search")

if __name__ == "__main__":
    main()



# 计算两数之和：python tools_demo.py add 3 5

# 批量重命名 txt 文件：python tools_demo.py rename project

# 搜索 data.txt 里的关键字：python tools_demo.py search error

