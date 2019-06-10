# list 是列表，跟数组相似，列表的数据可以相同，可以不相同 增删改查

# a = []
# b = ['a', 'b', 'c', 'd']
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# 遍历列表
# for value in b:
#     print(value)
#     print(a)

# for index, value in enumerate(b):
#     print(index, value)
    # print(value)

# 列表长度
# print(len(b))


# 列表通过下标访问元素
# print(b[0])
# print(b[2])

# 列表切片操作
# print(b[0:2])
# print(b[1:])
# print(b[1:3])
# 列表元素查找
# print(b.index('a'))
# print(b.index('b'))
# print(b.index('f'))


# 列表排序
# list2 = [1, 9, 4, 5, 8]
# print(list2)

# print(sorted(list2))
# list2.sort()
# print(list2)
# print(list2)

# list2.reverse()
# print(list2)

# dict 字典，一组键值对  javascript 对象
dict_0 = {}

dict_1 = {"BTC": "比特币",
          "ETH": "以太坊",
          "XRP": "瑞波币",
          "LTC": "莱特币"
          }
# print(dict_1)

# dict 获取值
for key in dict_1:
    # print(key, dict_1[key])
    # print()
    # pass
    print(dict_1.get(key))



# dict 获取健
# keys = dict_1.keys()
# print(keys, type(keys))

# values = dict_1.values()
# print(values)


# dict插入值
dict_0['EOS'] = '柚子'
dict_0['HT'] = "火腿"

print(dict_0)

# 删除
dict_0.pop('EOS')
print(dict_0)





