# match-case   case(0,0) case 直接跟着是数据
# xxx  这仅仅就是个名  随便写把  起作用的是case后面的东西啊！！！！
def yuanzu(xxx):
    match xxx:
        case (0,0):
            print("zeze")
        case 9:
            print("ok,y=1")
        case _:
            print("输了个寂寞")
yuanzu((0,0))
yuanzu (9)
yuanzu((0,9))


#来一个类class 和 match-case结合 
#match要解析某个class 需要用到__match_args_  
#@dataclass  可以用这个简化解析

# class point:
#     __match_args__ =("x","y") #告诉python解构时用x,y
#     def __init__ (self,x,y):
#         self.x=x
#         self.y=y
# def  test(xxx):
#     match xxx:
#         case point(0,0):
#             print("ok,let's go")
#         case point(x,y):
#             print(f"x={x},y={y}")
#         case _:
#             print("nothing")
# test(point(0,0))
# test(point(9,9))
# test("8")


from dataclasses import dataclass
@dataclass
class Point:
    x:int
    y:int

def where_is(xxx):
    match xxx:
        case Point(0,0):
            print("Origin")
        case Point(x=0,y=y):
            print(f"y={y}")
        case Point(x=x,y=0):
            print(f"x={x}")
        case Point():
            print("Somewher else")
        case _:
            print("Not a point")



