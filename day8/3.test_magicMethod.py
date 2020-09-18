# __init__()

# 体验__init__()
# class Washer():
#     # __init__()方法在创建一个对象时默认被调用，不需要手动调用
#     # __init__(self)方法中的self参数不需要开发者手动传递，会自动引用
#     def __init__(self):
#         self.width = 100
#         self.height = 200
#
#     def print_info(self):
#         print('洗衣机的宽度是{},高度是{}'.format(self.width, self.height))
#
#
# haier = Washer()
# haier.print_info()


# 带参数的__init__()
# class Washer():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def print_info(self):
#         print('洗衣机的宽度是{},高度是{}'.format(self.width, self.height))
#
# haier1 = Washer(100, 200)
# haier1.print_info()
#
# haier2 = Washer(300, 400)
# haier2.print_info()


# __str__()
# class Washer():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return '这是海尔洗衣机的说明'
#
# haier = Washer(100, 200)
# print(haier)


# __del__()
class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __del__(self):
        print('{}已经被删除'.format(self))

haier = Washer(100, 200)
del haier