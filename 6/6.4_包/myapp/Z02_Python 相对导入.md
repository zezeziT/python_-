# Python 相对导入 `.`, `..`, `...` 总结（含上下文完整说明）

---

## ❓ 问题背景

用户在执行如下命令时报错：

```bash
py -m myapp.main
```

报错信息：

```
ModuleNotFoundError: No module named 'math_utils'
```

出错位置在：

```python
# myapp/tools/__init__.py
print("6.4_.tools包已经初始化 ")
from math_utils import add  # ❌ 错误写法
```

---

## ✅ 错误分析

### 问题原因：

`from math_utils import add` 是“**顶级导入（absolute import）**”，意味着 Python 会在 `sys.path` 的根目录中查找 `math_utils.py` 文件，但这个模块实际是位于当前包 `tools` 内部的。

---

## ✅ 正确做法：使用相对导入

应该将上述导入改为：

```python
from .math_utils import add
```

这样写表示：从当前包（`tools`）中导入 `math_utils` 模块中的 `add` 函数。

---

## 🧭 `.`, `..`, `...` 是什么？

在相对导入中：

| 写法            | 含义                                       | 示例作用                         |
|-----------------|--------------------------------------------|----------------------------------|
| `.`             | 当前包（current package）                  | `from . import foo`              |
| `..`            | 上一级包（parent package）                 | `from .. import bar`             |
| `...`           | 上上一级包（grandparent package）          | `from ... import x`              |

---

## 🧩 示例目录结构

```
6.4_包/
│
├── myapp/
│   ├── __init__.py
│   ├── main.py
│   └── tools/
│       ├── __init__.py
│       ├── math_utils.py
│       └── string_utils.py
```

---

## ✅ 示例 1：同一包中模块导入（使用 `.`）

`math_utils.py` 中引用 `string_utils.py`：

```python
# 错误（找不到）
from string_utils import to_upper

# 正确（相对导入）
from .string_utils import to_upper
```

---

## ✅ 示例 2：从子包中导入主模块函数（使用 `..`）

`main.py` 中有：

```python
def main_func():
    print("main_func called")
```

在 `tools/math_utils.py` 中使用：

```python
from ..main import main_func
```

---

## ✅ 相对导入规则总结

| 语法                        | 含义                         | 适用情况          |
|-----------------------------|------------------------------|-------------------|
| `from .module import x`     | 当前目录                     | 包内部模块调用    |
| `from ..module import x`    | 上一级目录                   | 跨包调用          |
| `from ...module import x`   | 上上级目录                   | 深层嵌套结构       |

---

## ⚠️ 注意事项

- 相对导入只能在“模块作为包的一部分”时使用；
- 不能直接运行包含相对导入的 `.py` 文件，否则会报错；
- 建议使用如下方式运行模块：

```bash
python -m myapp.main
```

这样 `myapp` 会作为包被解释器正确识别，内部的相对导入就能生效。

---

## ✅ 最后建议

- 包内模块之间引用时，**统一使用相对导入 (`.`, `..`)**
- 包外部使用包时，使用绝对导入（例如：`import myapp.tools.math_utils`）
- `__init__.py` 文件中也应遵守相同的导入规则

---

如需我为你设计一套带测试的相对导入用例，请告诉我。

