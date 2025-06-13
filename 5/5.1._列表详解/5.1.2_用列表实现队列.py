# 队列 先进先出  
# 在开头删除或删除元素都很麻烦 后面的每一个元素都需要往前移动很麻烦 时间复杂度O(N) 效率低
Q= ["zeze","jvt","mi"]
Q.append("xxxxx") #入队 时间复杂度O(1)
Q.pop(0)  #出队   会让后面的元素每一个都往前移动 所以时间复杂度O(n) 所以效率低
print(Q)



# 导入模块中的双端队列 
# 用collections.deque 快速从两端添加或删除元素
# deque 是 双端队列（double-ended queue），底层用的是 双向链表结构
# append() 和 popleft() 都是 O(1) 的快速操作；

from collections import deque  
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry到了 添加到队列末尾
queue.append("Graham") # Graham到了
first=queue.popleft()  #第一个到的现在走了
print(first)
second=queue.popleft() # 第二个到的现在走了
print(second)
print(queue)

# deque的神奇之在于可以在队头 队尾 的插入和删除时间复杂度都是O（1）
q=deque({"66","88","xxxx","980"})
#队头插入
q.appendleft("left")
#队尾插入
q.append("right")
print(q)

#d队头删除
q.popleft()
print(q)
#队尾删除
q.pop()
print(q)