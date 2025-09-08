# 示例2 多个异常
import sys

try:
    f = open("myfile.txt")  # 文件可能不存在
    s = f.readline()
    i = int(s.strip())      # 转换可能失败
except OSError as err:
    print("文件错误：", err)
except ValueError:
    print("数据无法转换成整数")
except Exception as err:
    print(f"未知错误：{err}")
    print("未知错误：", err)
    raise   # 重新抛出异常
# 📌 解释：
# OSError：文件打不开。
# ValueError：字符串转整数失败。
# Exception：兜底处理，捕获其他未知错误。

