# 创建一些文件
import os, shutil
from pathlib import Path

p = Path("globtext")    # 创建一个文件通配符glob测试目录 代表当前工作目录下的 "globtext" 子目录
p.mkdir(exist_ok=True)  # 如果没有就创建这个目录

file_a = p / "text01.py"  # 拼接成 "globtext/text01.py"
# file 只是一个 路径对象（PosixPath 或 WindowsPath），并不代表实际存在的文件。
# 所以不会在磁盘上看到 text01.py 文件。


# 写文件
# 如果你要真正创建 text01.py，需要写点东西进去
# Path.write_text() 就是 在指定路径创建/覆盖文件并写入文本内容。
# 语法形式是：
# Path对象.write_text(data, encoding=None, errors=None)
file_a.write_text("# hello from text01.py\n", encoding="utf-8")


file_b = p / "text02.py"
with open (file_b, "w", encoding = "utf-8") as f:
    f.write("# text02.py\n")

file_c = p / "text03.py"
file_c.write_text("# text03.py\n", encoding="utf-8")

file_d = p / "data-01.csv"
file_d.write_text("# data-01.csv\n", encoding = "utf-8" )

file_e = p / "data-02.csv"
with open (file_e, "w", encoding= "utf-8") as fe:
    fe.write("# data-02.csv")




# 用途
# 在目录中用通配符（如 *.py、data-??.csv）收集匹配的文件名。
# 基础与递归匹配
import glob


# 查当前工作目录（os.getcwd() 的位置)
# 所以只能列出当前目录的 .py 文件。
print(glob.glob("*.py"))        # 当前目录下所有 .py
print(glob.glob("data-??.csv")) # data-01.csv、data-02.csv...之类
print("-------------------------------------------------------------")
print("\n")




# 递归所有子目录查
# 在 glob.glob() 里，recursive=True 的作用就是：
#      👉 允许 ** 这个通配符去匹配子目录（递归查找）。  没有的话查不到子目录 
print(glob.glob("**/*.py", recursive=True))     # 递归匹配所有子目录 .py
print(glob.glob("**/data-??.csv", recursive=True)) # 递归匹配所有子目录的 data-??.csv
print("--------------------------------------------")
print("\n")



# 查指定目录

# 错误 输出为[]
print(glob.glob("E:\python\official_docs\10\globtext\*.py"))
print("\n")

# 这里的 \p 被 Python 当作转义序列了（但 \p 不是合法的转义符，所以警告）。
# ✅ 正确写法有三种：
# 方法 1：在字符串前加 r，表示 raw string
print(glob.glob(r"E:\python\official_docs\10\globtext\*.py"))
print("\n")
# 方法 2：把反斜杠写成双反斜杠
print(glob.glob("E:\\python\\official_docs\\10\\globtext\\*.py"))
print("\n")
# 方法 3：用正斜杠（Windows 也支持）
print(glob.glob("E:/python/official_docs/10/globtext/*.py"))
print("\n")


# 🔑 总结
# Windows 路径要用 r"..."、双反斜杠 \\ 或正斜杠 /，避免转义问题。
# ** 通配符要配合 recursive=True 才能递归子目录。









# ✅ 小技巧：结合 os.path.join
# 更通用写法：
import os,glob

target_dir = r"E:\python\official_docs\10\globtext"
# 定义了要查找的目标目录。
# 前面的 r 表示 raw string（原始字符串），避免 Windows 路径里的 \ 被当作转义符。
# 比如 "E:\n\test" 会被 Python 解释成换行符和 \test
# 用 r"E:\n\test" 就不会被转义，按原样读取路径。

pattern  = os.path.join(target_dir, "*.py")
# os.path.join() 用来安全地拼接路径。
# 在这里就是把目标目录和通配符拼起来
# *.py：通配符，表示匹配 所有以 .py 结尾的文件。
# 最终 pattern 就是完整路径 + 通配符，用于 glob 查找。
# pattern 并不是一个“具体文件”的路径，而是 路径 + 匹配规则 的组合，也叫 路径模式（path pattern）。

print(glob.glob(pattern))
# 这个函数根据 通配符 查找匹配的文件列表。
# 返回值是 列表，里面是匹配到的文件完整路径。