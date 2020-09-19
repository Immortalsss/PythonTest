class Dog(object):
    tooth = 10


wangcai = Dog()
xiaohei = Dog()

# 通过类对象修改类属性
# Dog.tooth = 20
# print(Dog.tooth)
# print(wangcai.tooth)
# print(xiaohei.tooth)

# 通过实例对象修改类属性
wangcai.tooth = 12
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)


