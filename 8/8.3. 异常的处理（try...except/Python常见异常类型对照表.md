# Python 常见异常类型对照表

## 1. 数字相关
| 异常类型 | 触发场景 | 示例代码 | 报错信息 |
|----------|----------|----------|----------|
| `ZeroDivisionError` | 除数为 0 | `10 / 0` | `division by zero` |
| `OverflowError` | 数值运算结果太大 | `import math; math.exp(1000)` | `math range error` |
| `FloatingPointError` | 浮点运算出错（很少见，需要手动开启检查） | —— | —— |

---

## 2. 类型相关
| 异常类型 | 触发场景 | 示例代码 | 报错信息 |
|----------|----------|----------|----------|
| `TypeError` | 操作/函数应用在了错误的类型上 | `'2' + 2` | `can only concatenate str (not "int") to str` |
| `ValueError` | 值的类型对，但值不合法 | `int("abc")` | `invalid literal for int() with base 10: 'abc'` |
| `IndexError` | 下标越界 | `[1,2,3][5]` | `list index out of range` |
| `KeyError` | 字典里没有这个键 | `{"a":1}["b"]` | `'b'` |

---

## 3. 变量与作用域
| 异常类型 | 触发场景 | 示例代码 | 报错信息 |
|----------|----------|----------|----------|
| `NameError` | 使用了未定义的变量 | `print(x)` | `name 'x' is not defined` |
| `UnboundLocalError` | 局部变量在赋值前被引用（属于 NameError 的子类） | ```python\nx = 10\ndef f(): print(x); x=5; f()\n``` | `local variable 'x' referenced before assignment` |

---

## 4. 文件与输入输出
| 异常类型 | 触发场景 | 示例代码 | 报错信息 |
|----------|----------|----------|----------|
| `FileNotFoundError` | 文件不存在 | `open("abc.txt")` | `[Errno 2] No such file or directory: 'abc.txt'` |
| `PermissionError` | 没有权限访问文件 | 在只读文件夹里写文件 | `[Errno 13] Permission denied` |
| `IsADirectoryError` | 打开目录当作文件 | `open("/")` | `[Errno 21] Is a directory: '/'` |
| `IOError` | 输入输出操作失败（Python 3 里合并到 OSError） | —— | —— |

---

## 5. 导入与模块
| 异常类型 | 触发场景 | 示例代码 | 报错信息 |
|----------|----------|----------|----------|
| `ImportError` | 导入模块失败 | `import notexist` | `No module named 'notexist'` |
| `ModuleNotFoundError` | 模块没找到（ImportError 的子类） | `import fake` | `No module named 'fake'` |

---

## 6. 断言与属性
| 异常类型 | 触发场景 | 示例代码 | 报错信息 |
|----------|----------|----------|----------|
| `AssertionError` | 断言失败 | `assert 2+2==5` | `AssertionError` |
| `AttributeError` | 对象没有这个属性/方法 | `[1,2,3].push(4)` | `'list' object has no attribute 'push'` |

---

## 7. 迭代与生成器
| 异常类型 | 触发场景 | 示例代码 | 报错信息 |
|----------|----------|----------|----------|
| `StopIteration` | 迭代器没有数据（for 自动处理，一般看不到） | `next(iter([]))` | `StopIteration` |
| `StopAsyncIteration` | 异步迭代器结束 | —— | —— |

---

## 8. 其他常见
| 异常类型 | 触发场景 | 示例代码 | 报错信息 |
|----------|----------|----------|----------|
| `RuntimeError` | 一般运行时错误 | `import threading; t=threading.Thread(target=lambda:None); t.start(); t.start()` | `threads can only be started once` |
| `MemoryError` | 内存不足 | 大规模分配内存 | `MemoryError` |
| `KeyboardInterrupt` | 用户按 Ctrl+C 中断程序 | —— | `KeyboardInterrupt` |
| `SystemExit` | 调用 `sys.exit()` | —— | `SystemExit` |

---

## 9. 捕获方式对比
\`\`\`python
try:
    1/0
except ZeroDivisionError:   # 精确捕获
    print("除数不能为 0")
except Exception as e:      # 通用捕获
    print("发生错误:", type(e).__name__, "-", e)
\`\`\`

---

📌 小技巧：  
- 用 **精确异常**（比如 `ValueError`）更安全，能知道问题类型。  
- 用 **`Exception`** 能兜住大多数错误，适合调试或兜底。  
- 避免直接用 `except:`（不写类型），因为会把 Ctrl+C、系统退出等都吃掉。
