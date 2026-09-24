# -*- coding: utf-8 -*-
"""
04_flow_control.py —— Python 流程控制 学习脚本
面向零基础学员：变量、运算符、表达式已学过，本章学习如何用代码控制执行顺序。
本文件可从上到下顺序运行，不会报错。练习题与参考答案用注释包住。
"""

# ===== 1. 缩进是语法 =====
# Python 不用 {} 表示代码块，而是用"缩进"（通常是 4 个空格）来表示从属关系。
# 同一层级的语句必须保持相同的缩进，否则会报 IndentationError。

print("===== 1. 缩进是语法 =====")
print("下面用缩进表示代码块：")

score = 85
if score >= 60:
    # 这一行比上一行多缩进 4 个空格，属于 if 的代码块
    print("缩进正确：这行在 if 内部，会被执行")
print("这行没有缩进，属于外部，永远会执行")


# ===== 2. if / elif / else：成绩等级判断 =====
# 根据分数给出等级：>=90 优秀，>=80 良好，>=60 及格，否则不及格。
print("\n===== 2. if / elif / else：成绩等级 =====")

score = 85
print(f"当前分数：{score}")
if score >= 90:
    print("等级：优秀")
elif score >= 80:
    print("等级：良好")
elif score >= 60:
    print("等级：及格")
else:
    print("等级：不及格")


# ===== 3. if 嵌套与多条件组合（and / or）=====
# 组合多个条件：用 and（都满足）或 or（满足其一）。
print("\n===== 3. if 嵌套与多条件组合 =====")

age = 20
has_ticket = True

# 多条件组合：年龄够且持有门票
if age >= 18 and has_ticket:
    print("可以入场：成年且有票")
else:
    print("不能入场")

# 嵌套：先判断是否成年，再判断是否有票
print("嵌套判断示例：")
if age >= 18:
    if has_ticket:
        print("  成年且有票 -> 放行")
    else:
        print("  成年但无票 -> 需补票")
else:
    print("  未成年 -> 需家长陪同")


# ===== 4. match-case 简介（Python 3.10+）=====
# match-case 适合"一个变量对应多种固定取值"的场景，类似其他语言的 switch。
print("\n===== 4. match-case 简介 =====")

weekday = 3
print(f"今天是周几（数字）：{weekday}")
match weekday:
    case 1:
        print("星期一，开工！")
    case 2:
        print("星期二")
    case 3:
        print("星期三")
    case 6 | 7:  # 用 | 表示"或"
        print("周末，休息~")
    case _:  # _ 是通配符，匹配其余所有情况
        print("其他工作日")


# ===== 5. while 循环：计数与累加 =====
# while 在"条件为真"时反复执行，注意要在循环内改变条件，否则会死循环。
print("\n===== 5. while 循环 =====")

# 计数循环：打印 1 到 5
print("用 while 打印 1~5：")
count = 1
while count <= 5:
    print(f"  第 {count} 次")
    count += 1  # 改变条件变量，最终让循环结束

# 求 1~100 的累加和
print("求 1~100 的累加和：")
total = 0
n = 1
while n <= 100:
    total += n
    n += 1
print(f"  1 + 2 + ... + 100 = {total}")


# ===== 6. for 循环 + range() =====
# for 常用于"遍历"，range() 生成一串整数。range 有 3 种常用写法。
print("\n===== 6. for 循环 + range() =====")

# 6.1 range(stop)：从 0 数到 stop-1
print("range(5) -> 0,1,2,3,4：")
for i in range(5):
    print(f"  {i}", end=" ")
print()

# 6.2 range(start, stop)：从 start 数到 stop-1
print("range(2, 6) -> 2,3,4,5：")
for i in range(2, 6):
    print(f"  {i}", end=" ")
print()

# 6.3 range(start, stop, step)：带步长
print("range(0, 10, 2) -> 0,2,4,6,8：")
for i in range(0, 10, 2):
    print(f"  {i}", end=" ")
print()


# ===== 7. 遍历字符串和列表 =====
print("\n===== 7. 遍历字符串和列表 =====")

# 遍历字符串：逐个字符
word = "Python"
print(f"遍历字符串 '{word}'：")
for ch in word:
    print(f"  字符：{ch}")

# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
print("遍历列表 fruits：")
for fruit in fruits:
    print(f"  水果：{fruit}")


# ===== 8. break 与 continue 的区别 =====
# break：立刻结束整个循环。
# continue：跳过本次剩余语句，直接进入下一次循环。
print("\n===== 8. break 与 continue =====")

print("break 示例（遇到 3 就停止）：")
for i in range(1, 6):
    if i == 3:
        break
    print(f"  {i}", end=" ")
print("  <- 循环在此结束")

print("continue 示例（跳过 3）：")
for i in range(1, 6):
    if i == 3:
        continue
    print(f"  {i}", end=" ")
print("  <- 3 被跳过，其余都打印")


# ===== 9. 循环的 else 子句（进阶小知识）=====
# for/while 正常"跑完"（不是被 break 打断）时，会执行 else 块。
print("\n===== 9. 循环的 else 子句 =====")

print("没有 break 时执行 else：")
for i in range(3):
    print(f"  处理 {i}")
else:
    print("  循环正常结束，这里执行了 else")

print("被 break 打断时不执行 else：")
for i in range(3):
    if i == 1:
        break
    print(f"  处理 {i}")
else:
    print("  这行不会执行")


# ===== 10. 嵌套循环：九九乘法表 =====
print("\n===== 10. 嵌套循环：九九乘法表 =====")
for i in range(1, 10):        # 外层：行（1~9）
    for j in range(1, i + 1):  # 内层：每行从 1 乘到 i
        print(f"{j}×{i}={i * j}", end="\t")
    print()  # 每行结束换行


# ===== 练习题（注释区，请先自己尝试）=====
# 题目 1：猜数字（思路练习）
#   用 fixed_answer = 42 模拟"答案"，写一段 while 循环，
#   让 guess 从 1 开始递增，直到等于 fixed_answer 时打印"猜中了"并 break。
#
# 题目 2：打印菱形星号
#   用循环在控制台打印一个由 "*" 组成的菱形（如 5 行）。
#
# 题目 3：找出 1~50 中所有 3 的倍数
#   用 for + range + if，打印出能被 3 整除的数字。
#
# 题目 4：判断质数
#   写一个函数 is_prime(n)，判断正整数 n 是否为质数（只能被 1 和自身整除）。
#   然后测试 is_prime(17) 与 is_prime(15)。
#
# ---------------- 参考答案（先自己做，再看这里）----------------
# 题1：
# fixed_answer = 42
# guess = 1
# while True:
#     if guess == fixed_answer:
#         print("猜中了！")
#         break
#     guess += 1
#
# 题2（5行星号菱形）：
# for i in range(-2, 3):
#     print(" " * abs(i) + "*" * (5 - 2 * abs(i)))
#
# 题3：
# print("1~50 中 3 的倍数：")
# for x in range(1, 51):
#     if x % 3 == 0:
#         print(x, end=" ")
# print()
#
# 题4：
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(17), is_prime(15))
