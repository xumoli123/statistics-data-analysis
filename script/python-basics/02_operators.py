# -*- coding: utf-8 -*-
"""
Python 零基础入门：运算符（Operators）
=====================================
本文件按小节演示 Python 中常用的各类运算符。
所有示例均可从顶到底顺序运行，输出附带中文说明。
"""


# ===== 1. 算术运算符 =====
# 包括：+（加） -（减） *（乘） /（真除法） //（整除） %（取余） **（幂）

a, b = 10, 3

print("===== 1. 算术运算符 =====")
print("加法 a + b =", a + b)          # 13
print("减法 a - b =", a - b)          # 7
print("乘法 a * b =", a * b)          # 30

# 重点1：/ 与 // 的区别
# /  是“真除法”，结果永远带小数（float），哪怕能除尽
# // 是“整除/地板除”，结果只保留整数部分（向下取整）
print("真除法 a / b =", a / b)        # 3.3333333333333335（浮点数）
print("整除   a // b =", a // b)       # 3（只取整）

# 负数整除会向下取整，注意区别
print("负数整除 -10 // 3 =", -10 // 3)  # -4（向下取整，不是 -3）

# 重点2：% 取余（取模）的用途
# 得到“除法之后剩下的部分”
print("取余   a % b =", a % b)        # 1，因为 10 = 3*3 + 1

# 取余的实用场景：判断奇偶、循环点位、时分秒换算等
# 如果一个数除以 2 余数为 0，它就是偶数
number = 7
print("7 是否为偶数（7 % 2 == 0）:", number % 2 == 0)  # False

# 幂运算：a 的 b 次方
print("幂运算 a ** b =", a ** b)      # 1000，即 10 的 3 次方
print("2 的 10 次方 2 ** 10 =", 2 ** 10)  # 1024


# ===== 2. 比较运算符 =====
# 包括：==（相等） !=（不等） >（大于） <（小于） >=（大于等于） <=（小于等于）
# 比较运算的结果都是布尔值（bool）：True 或 False

print("\n===== 2. 比较运算符 =====")
x, y = 5, 8
print("x == y（相等）:", x == y)      # False
print("x != y（不等）:", x != y)      # True
print("x > y （大于）:", x > y)       # False
print("x < y （小于）:", x < y)       # True
print("x >= 5（大于等于）:", x >= 5)  # True
print("y <= 7（小于等于）:", y <= 7)  # False

# 比较运算符常用于条件判断（配合 if，这里先只演示结果）
age = 18
print("age 是否成年（>=18）:", age >= 18)  # True


# ===== 3. 逻辑运算符 =====
# 包括：and（与） or（或） not（非）
# 结果通常是 bool，用于组合多个条件

print("\n===== 3. 逻辑运算符 =====")
p, q = True, False
print("p and q（都为真才为真）:", p and q)  # False
print("p or  q（有一个真即为真）:", p or q)  # True
print("not p  （取反）:", not p)            # False

# 重点：短路特性（short-circuit）
# and：左侧为假时，右侧不再计算（因为结果已确定为假）
# or ：左侧为真时，右侧不再计算（因为结果已确定为真）
# 利用短路可以写出“安全写法”，避免出错：

# 示例：只有当 name 不为 None/空时才调用 .upper()
name = None
# 下面这行如果不用短路，单独写 name.upper() 会报错（None 没有 upper 方法）
safe_result = name and name.upper()
print("短路安全写法 name and name.upper() =", safe_result)  # None，没有报错

name = "python"
safe_result = name and name.upper()
print("有值时 name and name.upper() =", safe_result)  # PYTHON

# 示例：提供默认值（or 短路）
user_input = ""          # 假设用户输入为空
value = user_input or "默认值"
print("user_input or '默认值' =", value)  # 默认值


# ===== 4. 赋值运算符 =====
# = 是最基础的“赋值”，其它是“带运算的赋值”简写

print("\n===== 4. 赋值运算符 =====")
n = 0
print("初始 n =", n)      # 0

n += 5                   # 等价于 n = n + 5
print("n += 5 后 =", n)   # 5

n -= 2                   # 等价于 n = n - 2
print("n -= 2 后 =", n)   # 3

n *= 4                   # 等价于 n = n * 4
print("n *= 4 后 =", n)   # 12

n //= 5                  # 等价于 n = n // 5
print("n //= 5 后 =", n)  # 2

n %= 2                   # 等价于 n = n % 2
print("n %= 2 后 =", n)   # 0

n = 3
n **= 2                  # 等价于 n = n ** 2
print("n **= 2 后 =", n)  # 9


# ===== 5. 成员运算符 =====
# in      ：判断元素是否在序列（字符串/列表等）中，在则为 True
# not in  ：与 in 相反

print("\n===== 5. 成员运算符 =====")
text = "hello python"
print("'py' 是否在 text 中:", "py" in text)       # True
print("'xyz' 是否不在 text 中:", "xyz" not in text)  # True

fruits = ["apple", "banana", "orange"]
print("'banana' 是否在 fruits 列表中:", "banana" in fruits)   # True
print("'pear' 是否不在 fruits 列表中:", "pear" not in fruits)  # True


# ===== 6. 身份运算符 is 与 == 的区别 =====
# == 比较“值是否相等”
# is 比较“是否是同一个对象（内存地址相同）”

print("\n===== 6. 身份运算符 is 与 == =====")
list_a = [1, 2, 3]
list_b = [1, 2, 3]
print("list_a == list_b（值相等）:", list_a == list_b)  # True
print("list_a is list_b（同一对象）:", list_a is list_b)  # False

# 小整数缓存现象：Python 会缓存常用的小整数（-5 ~ 256），
# 所以这部分整数即使分别创建，也可能是同一个对象：
i = 100
j = 100
print("100 is 100（小整数缓存）:", i is j)            # 通常为 True

# 超出缓存范围的大整数，结果“不稳定”（有时 True 有时 False，取决于运行环境），
# 这正是隐患所在：
k = 257
m = 257
print("257 is 257（结果不稳定，切勿依赖）:", k is m)   # 可能为 True 也可能为 False

# 提醒：不要使用 is 来比较数值大小/相等，
# 数值请用 ==；is 只用于判断是不是同一个对象（例如 x is None）。
value1 = 1000
value2 = 1000
print("用 == 比较数值（正确写法）:", value1 == value2)  # True，稳定可靠


# ===== 7. 运算符优先级简介 =====
# 优先级（大致）：算术 > 比较 > 逻辑
# 口诀：先算括号，再算幂，再乘除取余，再加减，再比较，最后逻辑。
# 建议：不确定时一律用括号 () 明确顺序，可读性最好，也不易错。

print("\n===== 7. 运算符优先级 =====")

# 不用括号（依赖默认优先级）：先算乘法，再算加法
result1 = 2 + 3 * 4
print("2 + 3 * 4 =", result1)        # 14，因为先算 3*4=12，再加 2

# 用括号明确顺序：先算括号内加法，再乘
result2 = (2 + 3) * 4
print("(2 + 3) * 4 =", result2)      # 20

# 综合示例：先算术，再比较，再逻辑
score = 85
passed = score >= 60 and score <= 100
print("成绩 85 是否在 60~100 之间（>=60 and <=100）:", passed)  # True

# 用括号让逻辑更清晰（推荐写法）
passed_clear = (score >= 60) and (score <= 100)
print("用括号明确后的写法结果相同:", passed_clear)  # True


# ===== 8. 练习题 =====
# 请在下方注释块中，尝试自己写出代码完成练习。
# （以下为练习题目，练习时请新建一个 .py 文件或在本文件下方取消注释完成。）

"""
【练习题】（建议另存文件练习，或在下方书写后取消注释运行）

1) 秒数转时分秒：给定 total_seconds = 3700，
   计算它等于多少小时、多少分钟、多少秒余。
   提示：用 // 和 % 配合 3600、60 来拆分。

2) 判断偶数：输入一个数 n，判断它是否为偶数，
   输出类似 "偶数" 或 "奇数"。提示：n % 2 == 0。

3) 判断字符是否在字符串中：给定 s = "hello" 和 c = "e"，
   判断 c 是否出现在 s 中，输出 True/False。提示：使用 in。

4) 综合：给定年龄 age 和是否会员 is_member（bool），
   若“年龄 >= 18 且 是会员”则输出 "欢迎"，否则输出 "不满足条件"。
   提示：使用 >= 与 and，并用括号明确优先级。
"""

# ---------------- 参考答案（注释包住，运行时不执行） ----------------
"""
【参考答案】

# 练习1：秒数转时分秒
total_seconds = 3700
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(hours, "小时", minutes, "分钟", seconds, "秒")  # 1 小时 1 分钟 40 秒

# 练习2：判断偶数
n = 4
if n % 2 == 0:
    print("偶数")
else:
    print("奇数")

# 练习3：判断字符是否在字符串中
s = "hello"
c = "e"
print(c in s)  # True

# 练习4：综合判断
age = 20
is_member = True
if (age >= 18) and is_member:
    print("欢迎")
else:
    print("不满足条件")
"""
