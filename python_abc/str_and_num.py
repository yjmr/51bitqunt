# python 定义变量 只能以字母和下划线开头， 书写全部以英文半角输入法.

"""
a = "hello world"
a23 = "hello world"
print(a23)

"""



# 整数和浮点数  +、- * / %(求余数) **, 保留小数点

# a1 = 12
# a2 = 12.5
#
# c = a1 + a2
# print(c)
#
# d = a1 - a2
# print(d)

# e = a1 * a2
# print(e)
#
# e = a1 / a2
# print(e)

#
# a1 = 5
# a2 = 3
# e = a1 % a2
# print(e)

# a1 = 2
# a2 = 2
# e = a1 ** a2
# print(e)

# a1 = 12.9566
# c = round(a1, 2)
# print(c)


# a = True
# b = False
#
# print(a)
# print(b)

# 比较运算 > < >= <= == !=

# print(3 > 2) # True
# print(3 < 2) # False
# print(3>=2) # True
# print(3<=3)  # True
# print(3==2)  # False
# print(3!=2)  # True


# 布尔值 布尔运算and or & |

# a = (3>2) and (1<2)  # True
# # print(a)

# a = (3>2) & (1<2)  # True
# print(a)

# b = (3>2) | (1>2)  # True
# print(b)

# b = (3 > 2) or (1>2)  # True
# print(b)


# 代码注释 ，单行注释和多行注释


# 操作符 type, help函数, 查看帮助文档， 按住command 点击查看.
# print(help(round))


# 字符串定义 String 以单引号'，双引号''，三引号''' 开始，同样符号结束

hello = "hello world"
hello1 = 'hello world'
hello2 = '''Hello world'''
# print(hello)
# print(hello1)
# print(hello2)

# 字符串截取和运算 * + 通过下标来运算, 分割， 替换, 大写小写转变

# print(hello[1])

# a = hello + "我"
# print(a)
#
# print(hello * 3)  # "hello world" + "hello world" + "hello world"


# a = hello.split(' ')
# # print(a)
#
# for value in a:
#     print(value)

# a = hello.upper()  # 转成大写
# print(a)
#
# b = a.lower()  # 转成小写
# print(b)


# 替换

symbol = "BTC/USDT"
# print(symbol.split('/'))
symbol1 = 'btc_usdt'
symbol2 = symbol1.upper()
print(symbol2)

symbol3 = symbol2.replace('_', '/')
print(symbol3)

print(symbol == symbol3)

