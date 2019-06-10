# 函数(方法) 定义


"""
def 函数名称(参数1, 参数2):
    程序语句
"""

# def print_hello():
#     print("hello world")
#
# 函数调用（通过函数名加括号调用）
# print_hello()


# 带有参数的函数
# def print_hello1(name):
#     print("hello world:", name)
# print_hello1("stephen")

# def print_hello2(name, age, score):
#     print("hello world:", name, age, score)
#
#
# print_hello2("stephen", 20, 80)
# 带有返回值的函数

# def child_or_adult(age):
#     if age > 18:
#         return "adult"
#     else:
#         return "child"
#
# per = child_or_adult(15)
# print(per)


# 局部变量和全局变量
# num = 100
# def func():
#     num = 123
#     print(num)
#
# func()

# num = 100
# def func():
#     num += 100
#     # num = num + 100
#     print(num)
#
# func()

# 函数内部的变量名如果第一次出现，且出现在=前面，即被视为定义一个局部变量。
#函数内部的变量名如果第一次出现，且出现在=后面，且该变量在全局域中已定义，则
# 这里将引用全局变量，如果该变量在全局域中没有定义，当然会出现“变量未定义”的错误。例如：
# num = 100
# def func():
#     x = num + 100
#     print(x)
#
# func()
# print(num)



# 只要是*使用*变量，而该变量在全局域中有定义，而在局部没有定义，则会使用全局变量。

# num = 100  # 全局变量
# def func():
#     num = 200 # 局部变量
#     x = num + 100
#     print(x)
# func()
# print(num)

# 函数中使用某个变量时，该变量名既有全局变量也有同名的局部变量，则会使用局部变量

# num = 100 # 全局变量
# def func():
#     global num
#     num = 200
#     num += 100  # num = num + 100
#     print(num)
# func()
# print(num)


# 直接敲main
# if __name__ == '__main__':
#     pass

if __name__ == '__main__':
    pass
    # 面向对象编程
    # self
    # 网易云课堂
    # imooc
    # 极客网















# 函数(方法)：作用主要是提高代码可读性、维护性、还有开发效率