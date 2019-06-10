# 条件判断语句

"""
if 条件(真假):
    语句
elif 条件:
    语句
elif 条件:

...
else:
   语句
   pass

"""

# score = 95

# if score < 60:
#     print("不及格")
# elif 60 <=score < 80:  # 60 <= score < 80
#     print("良好")
# elif score < 90:
#     print("优秀")
# else:
#     print("杰出")


# if score > 90:
#     print("杰出")
# elif score > 80:
#     print("优秀")
# elif score > 60:
#     print("良好")
# else:
#     print("不及格")



# for 循环

fruits = ['苹果', '香蕉', '樱桃', '荔枝', '芒果']

# for 值 in list:
# for fruit in fruits:
#     print(fruit)

# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# print(help(range))

# while 循环
"""
while 条件判断:
    程序语句
    pass
"""

# a = 0
# while a <= 100:
#     print(a)
#     a += 1

# print(help(range))
# for i in range(1, 100, 3):
#     print(i)

# import time
# # 无限循环
# while True:
#     print("CTA策略运行")
#     time.sleep(5)


# break 和 continue:
## - continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
## - break 语句可以跳出 for 和 while 的循环体,结束当前的循环.

# for letter in 'BTC/USDT':  # 第一个实例  可迭代的对象
#     # print(letter)
#     if letter == 'U':
#         break
#         # continue
#     print('当前字母为 :', letter)
#
# print("*"*20)
# for letter in 'BTC/USDT':  # 第一个实例  可迭代的对象
#     # print(letter)
#     if letter == 'U':
#         # break
#         continue
#     print('当前字母为 :', letter)

#


var = 10  # 第二个实例
while var > 0:
    print('当期变量值为 :', var)
    var = var - 1
    if var == 5:
        break

print("*" * 20)
var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:  # 变量为 5 时跳过输出
        continue
    print('当前变量值 :', var)



