class Wash():
    def wash(self):
        print('能洗衣服')
        # self是调用该函数的对象
        # print(self)

    def print_info(self):
        # 类里面获取对象属性
        print('洗衣机的宽度是{},高度是{}'.format(self.width, self.height))

# 一个类可创建多个对象
# haier1 = Wash()
# haier1.wash()
#
# haier2 = Wash()
# haier2.wash()

# 在类外面添加对象属性
haier = Wash()
haier.width = 100
haier.height = 200

# 在类外面获取对象属性
print('洗衣机的宽度是{},高度是{}'.format(haier.width, haier.height))

# 在类里面获取对象属性
haier.print_info()


