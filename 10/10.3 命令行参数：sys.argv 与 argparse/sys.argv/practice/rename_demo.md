# rename_demo.py 代码讲解

``` python
import sys
import os

prefix = sys.argv[1]  # 新前缀
for i, filename in enumerate(os.listdir('.'), 1):
    if filename.endswith('.txt'):
        new_name = f"{prefix}_{i}.txt"
        os.rename(filename, new_name)
        print(f"{filename} -> {new_name}")
```

------------------------------------------------------------------------

## 1️⃣ sys.argv\[1\]

-   `sys.argv` → 命令行参数列表。

运行：

``` bash
py rename_demo.py project
```

-   `sys.argv[0]` = `"rename_demo.py"`\
-   `sys.argv[1]` = `"project"`

所以这里 `prefix = "project"`。

------------------------------------------------------------------------

## 2️⃣ os.listdir('.')

-   `os.listdir(path)` → 列出目录下的所有文件和文件夹。\
-   `'.'` 表示当前目录。

比如你目录里有：

    rename01.txt
    rename02.txt
    notes.docx

那么 `os.listdir('.')` 可能返回：

``` python
['rename01.txt', 'rename02.txt', 'notes.docx']
```

⚠️ 注意：这个顺序 **不是固定的**，可能取决于系统。\
所以可能你期待是 `rename01.txt, rename02.txt` → 改成
`project_1.txt, project_2.txt`\
但实际上 Python 返回顺序可能不一样，所以就出现你看到的
`project_2.txt, project_3.txt`。

👉 想要按顺序，就要加排序：

``` python
for i, filename in enumerate(sorted(os.listdir('.')), 1):
```

------------------------------------------------------------------------

## 3️⃣ enumerate(..., 1)

-   `enumerate(列表, 1)` → 给每个元素编号，编号从 1 开始。

示例：

``` python
for i, name in enumerate(['a', 'b', 'c'], 1):
    print(i, name)
```

输出：

    1 a
    2 b
    3 c

所以这里 `i` 就是数字编号，`filename` 是文件名。

------------------------------------------------------------------------

## 4️⃣ if filename.endswith('.txt')

-   只处理 **以 `.txt` 结尾的文件**。
-   避免把别的文件（比如 `.docx`、`.py`）也改掉。

------------------------------------------------------------------------

## 5️⃣ new_name = f"{prefix}\_{i}.txt"

-   f-string → 字符串插值。
-   把 `prefix` 和编号拼起来。

例如：

``` python
prefix = "project"
i = 1
new_name = "project_1.txt"
```

------------------------------------------------------------------------

## 6️⃣ os.rename(filename, new_name)

-   把文件改名。
-   例如 `rename01.txt` 改成 `project_1.txt`。

------------------------------------------------------------------------

## 7️⃣ print(f"{filename} -\> {new_name}")

-   打印改名前后的对照，比如：

```{=html}
<!-- -->
```
    rename01.txt -> project_1.txt

------------------------------------------------------------------------

## ✅ 总结一下运行效果

如果目录里有：

    rename01.txt
    rename02.txt
    notes.docx

运行：

``` bash
py rename_demo.py project
```

可能结果是：

    rename01.txt -> project_1.txt
    rename02.txt -> project_2.txt

但也可能顺序乱掉（因为 `os.listdir()` 不保证顺序），所以你才会看到
`project_2.txt`、`project_3.txt` 这种情况。

👉 **解决方法**：\
在 `for` 循环里加 `sorted()`：

``` python
for i, filename in enumerate(sorted(os.listdir('.')), 1):
```

这样就会严格按照文件名字母顺序来改名。
