# 例子 3️⃣：简单文本搜索

# search_demo.py
import sys

keyword = sys.argv[1]  # keyword为输入的第一个参数

with open('data.md', 'r', encoding = 'utf-8') as f:
    for line in f :
        if keyword in line:
            print(line.strip())

# 命令行执行：  py search_demo.py error
#   脚本会输出 data.md 中包含 "error" 的所有行
#   命令行参数可以随意换成 "warning" 或其他关键字


# 命令行执行：  py search_demo.py hello 
