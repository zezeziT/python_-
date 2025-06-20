# 原 3x4 矩阵
matrix=[
    [1,2,3,4],      # 行 0
    [5,6,7,8],      # 行 1
    [9,10,11,12]    # 行 2
]

# 创建空矩阵，准备放结果
T=[]

# 外层循环，遍历列（原来的列，会变成新的行）
for i in range(4):      # 0, 1, 2, 3 — 总共 4 列
    new_row=[]              # 新行
    # 内层循环，遍历行
    for j in range(3):  # 0, 1, 2 — 总共 3 行
        new_row.append(matrix[j][i])  # 取出第 j 行第 i 列的元素
    T.append(new_row) #连接起来把3行
print(T)
for row in T:
    print(row)


#
T=[[matrix[j][i] for j in range(3)] for i in range(4)]
print(T)

# 内置 zip 函数转置矩阵（以后很常用）
T = list(map(list, zip(*matrix)))
print(T)
