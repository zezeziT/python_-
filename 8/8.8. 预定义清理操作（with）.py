# 8.8. 预定义清理操作（with）
with open("myfile.txt", "w") as f:
    f.write("hello")

# 自动关闭文件

# 📌 解释：
# 不需要写 f.close()，with 会自动关闭。

# 为什么会把文件清理与异常连接起来
# 防止出现异常后直接结束 不关闭文件
# 参考
# file:///E:\python\official_docs\8\8.8.python_with_exception_summary.md