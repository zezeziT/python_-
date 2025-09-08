try:
    raise TypeError("类型错误")
except Exception as e:
    e.add_note("这是第一条说明")
    e.add_note("这是第二条说明")
    raise


# def shuru():
#         # 尝试把输入转成整数
#         return  int(input("请输入一个数字"))
# while True:  
#     try:
#         num = shuru()
#         print("✅ 你输入的数字是：", num)
#         break  # 输入成功就跳出循环
#     except Exception as e:
#         # 添加说明
#         e.add_note("请检查输入是否为数字")
#         e.add_note("输入不能为空")

#         # 打印友好提示（不显示复杂的 Traceback）
#         print("出错啦：", e)
#         for note in e.__notes__:
#              print("提示：", note)
#         print("请重新输入！\n")




# import traceback

# def shuru():
#         # 尝试把输入转成整数
#         return int(input("请输入一个数字: "))
# while True:  
#     try:
#         num = shuru()
#         print("✅ 你输入的数字是：", num)
#         break # 输入成功就跳出循环
#     except Exception as e:
#         # 添加说明
#         e.add_note("请检查输入是否为数字")
#         e.add_note("输入不能为空")

#         # 打印异常（Traceback + notes），但不中断程序
#         traceback.print_exception(e)  # 打印完整 Traceback，不会退出程序
#         print("请重新输入！\n")
        
        
