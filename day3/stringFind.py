mystr = 'hello world and itcast and itheima and Python'

# find()
print(mystr.find('and'))    # 12
print(mystr.find('and', 15, 30))    # 23
print(mystr.find('ands'))   # -1

# index()
print(mystr.index('and'))    # 12
print(mystr.index('and', 15, 30))    # 23
# print(mystr.index('ands'))   # 报错

# count():统计子串出现次数
print(mystr.count('and'))    # 3
print(mystr.count('and', 15, 30))    # 1
print(mystr.count('ands'))   # 0

# rfind():从右侧开始查找
print(mystr.rfind('and'))    # 35

# rindex():从右侧开始查找
print(mystr.rindex('and'))    # 35
