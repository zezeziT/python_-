class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")

d = Dog()
d.speak()  # Woof!

print("---------------------------------------")

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        Animal.speak(self)  # 调用父类方法
        print("Woof!")

d = Dog()
d.speak()  # Woof!



print("---------------------------------------")

class A:
    def say(self):
        print("A")

class B:
    def say(self):
        print("B")

class C(A, B):
    def say(self):
        super().say()  # 用 super() 自动找下一个类
        print("C")

c = C()
c.say()



print("---------------------------------------")


class A:
    def say(self):
        print("A")
        super().say()

class B:
    def say(self):
        print("B")

class C(A, B):
    def say(self):
        super().say()  # 用 super() 自动找下一个类
        print("C")

c = C()
c.say()
