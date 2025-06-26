#
import sys
# print(sys.ps1)  只能在交互式命令行执行

# sys.ps1='>c '

# import text  # 会报错 因为text模块和这个不在一个目录下
sys.path.append('./6.2_text')  # 把还有模块text的子目录加入搜索路径’
import text