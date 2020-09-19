# 类方法
# class Dog(object):
#     __tooth = 10
#
#     @classmethod
#     def get_tooth(cls):
#         return cls.__tooth
#
#
# wangcai = Dog()
# result = wangcai.get_tooth()
# print(result)

# 静态方法
class Dog(object):
    @staticmethod
    def print_info():
        print('这是一个静态方法')


wangcai = Dog()
wangcai.print_info()
Dog.print_info()