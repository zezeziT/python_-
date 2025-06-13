#涉及到文件操作
#file.write()  文件写入
#separator.join(args)   用分隔符separator把args元组/序列拼接起来
# 用分隔符把很多个小字符串拼成一个大的字符串 

# .join() 的作用是：把一个字符串列表合成一个新的字符串
s="--".join(['2025','6','9','maybe''happy''?'])
print(s)

#.join()	只能拼接字符串序列，不接受数字
"/".join(['1','2','3'])
#"/".join([1,2,3])  
# 会报错！！！TypeError: sequence item 0: expected str instance, int found 


#.split() 来反过来拆，把有分隔符连接的字符串又变成列表
nos=s.split("--")
print(nos)





#文件操作
# file 和 separator 是普通参数
# *args 收集剩下的所有位置参数
def write_multiple_items(file, separator, *args):
    # .join()把一个字符串列表合成一个新的字符串
    # file.write(...)  	把字符串写入文件中
    file.write(separator.join(args))

# open("文件名","w")  以写入模式打开文件（如果不存在就创建）
# with ... as f: 自动管理文件打开与关闭
#       1.打开一个叫 output.txt 的文件
#       2.把文件对象命名为 f
#       3.在 with 语句块结束后，自动关闭文件（防止出错)
with open("output.txt","w") as f:
    write_multiple_items(f,"-","hello","world","Python")



def concat(*args, sep="/"):
    return sep.join(args)
s1=concat("earth", "mars", "venus")
s2=concat("earth", "mars", "venus", sep=".")
#会不对齐 s1 + 空格 + 换行符 + 空格 + s2
#print默认在","之间加空格
print(s1,"\n",s2) 

print(s1+"\n"+s2)

print(s1,end="\n")
print(s2)

print(s1)
print(s2)
# 不会报错，‘--’被当成args的一员 所以用了默认的分隔符”/“
# *后面甭出现位置参数！ *args 默认占了后面的所有位置参数 所以sep需要使用关键字参数
s3=concat("earth", "mars", "venus", "--")
print(s3)