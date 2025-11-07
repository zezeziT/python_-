# sum_demo.py
# 例子 1️⃣：简单计算两个数的和
import sys

if len(sys.argv) != 3:
    print("用法：python sum_demo.py num1 num2")
    sys.exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print(f"{num1} + {num2} = {num1 +num2}")
# python sum_demo.py 3 5



# 1️⃣ sys.exit()
# sys.exit([arg]) 是 Python 提供的退出程序的方式。
# 它会立即终止 Python 脚本的执行。
# arg 可以是：
# 0 或省略 → 表示正常退出（通常表示程序成功执行）。
# 非 0（比如 1、2 等） → 表示异常退出或出错。

# 2️⃣ sys.exit(1)
# 这里表示“程序因为参数不对而异常退出”。
# 当命令行参数不是两个数字时：
# 打印提示信息 "用法: python sum_demo.py num1 num2"
# 用 sys.exit(1) 结束程序，不再继续执行下面的加法计算。

# 3️⃣ 如果没有 sys.exit(1) 会怎样？
# 假设 py sum_demo.py 5 
# 这时 len(sys.argv) != 3，会打印提示信息。
# 但是程序还会继续往下执行，去做：
# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])  # <- 这里会报错，因为 argv[2] 不存在
# Python 会抛出 IndexError: list index out of range。
# ✅ 所以加上 sys.exit(1) 可以提前结束程序，避免后续报错。