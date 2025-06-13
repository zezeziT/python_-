# 用python 实现一个简单的栈结构
class Stack:
    def __init__(self):
        self.items = [] # 初始化栈

    def is_empty(self):
        return len(self.items) == 0 #判断栈是否为空

    def push(self, item) :
        self.items.append(item) # 入栈（压栈）

    def pop(self):
        if self.is_empty():
            raise IndexError("栈为空，不能弹出元素")
        return self.items.pop() # 出栈（弹栈）
    
    def peek(self):
        if self.is_empty():
            raise IndexError("栈为空，查看栈顶元素")
        return self.items[-1]  # 查看栈顶元素 不弹出
    
    def size(self):
        return len(self.items) # 饭返回栈的大小
    
    def traverse(self):
        print("从栈底到栈顶遍历：")
        for item in self.items:
            print(item)

    def __str__(self):
        return f"Stack({self.items})" #打印栈内容
    
if __name__ == "__main__":
        stack =Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        print("当前栈：", stack)
        print("栈顶元素：", stack.peek())
        print("出栈元素：", stack.pop())
        print("当前栈：", stack)

        stack.traverse()


