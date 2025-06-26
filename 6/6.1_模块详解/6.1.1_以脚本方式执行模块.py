# 
import fibo

print(f"__name__ = {__name__}")
print(f"fibo.__name__ = {fibo.__name__}")

fibo.fib(10)
print(fibo.fib2(10))

import fibo2
print(f"__name__ = {__name__}")
print(f"fibo2.__name__ = {fibo2.__name__}")


