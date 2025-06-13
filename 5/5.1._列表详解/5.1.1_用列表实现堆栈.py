# 栈 栈顶 栈底 先进后出 在栈顶输入和输出

# 输入 append（）  输出 pop（）  刚好都是在末尾添加和删除 与栈先进后出匹配

#  入栈出栈 时间复杂度O(1)

stack=[3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

stackpop=stack.pop()
print(stackpop)

print(stack.pop())
print(stack)

print(stack.pop())
print(stack)
