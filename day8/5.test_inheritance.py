# 单继承
# 师傅类
# class Master(object):
#     def __init__(self):
#         self.skill = '古法煎饼果子技术'
#
#     def make_cake(self):
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#
# # 徒弟类
# class Prentice(Master):
#     pass
#
#
# # 徒弟类创建对象，调用师傅类的属性和方法
# test = Prentice()
# test.make_cake()


# 多继承
# 师傅类
# class Master(object):
#     def __init__(self):
#         self.skill = '师傅古法煎饼果子技术'
#
#     def make_cake(self):
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#
# # 学校类
# class School(object):
#     def __init__(self):
#         self.skill = '学校古法煎饼果子技术'
#
#     def make_cake(self):
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#
# # 徒弟类
# class Prentice(School, Master):
#     pass
#
#
# # 徒弟类创建对象
# test = Prentice()
# test.make_cake()


# 子类重写父类同名属性和方法
# class Master(object):
#     def __init__(self):
#         self.skill = '师傅古法煎饼果子技术'
#
#     def make_cake(self):
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#
# # 学校类
# class School(object):
#     def __init__(self):
#         self.skill = '学校古法煎饼果子技术'
#
#     def make_cake(self):
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#
# # 徒弟类
# class Prentice(School, Master):
#     def __init__(self):
#         self.skill = '独创古法煎饼果子技术'
#
#     def make_cake(self):
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#
# # 徒弟类创建对象
# test = Prentice()
# test.make_cake()
#
# print(Prentice.__mro__)


# 子类调用父类的同名属性和方法
# 师傅类
# class Master(object):
#     def __init__(self):
#         self.skill = '师傅古法煎饼果子技术'
#
#     def make_cake(self):
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#
# # 学校类
# class School(object):
#     def __init__(self):
#         self.skill = '学校古法煎饼果子技术'
#
#     def make_cake(self):
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#
# # 徒弟类
# class Prentice(School, Master):
#     def __init__(self):
#         self.skill = '独创古法煎饼果子技术'
#
#     def make_cake(self):
#         # 为了防止调用父类初始化时候覆盖子类初始化，需要重新初始化
#         self.__init__()
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#     # 子类调用父类的同名属性和方法：把父类的同名属性和方法再封装
#     def master_make_cake(self):
#         # 因为同名属性在init初始化位置，为了获取父类的同名属性，需要再次初始化
#         Master.__init__(self)
#         Master.make_cake(self)
#
#     def school_make_cake(self):
#         School.__init__(self)
#         Master.make_cake(self)
#
#
# # 徒弟类创建对象
# test = Prentice()
# test.make_cake()
#
# test.master_make_cake()
# test.school_make_cake()
# test.make_cake()


# 多层继承
# 师傅类
# class Master(object):
#     def __init__(self):
#         self.skill = '师傅古法煎饼果子技术'
#
#     def make_cake(self):
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#
# # 学校类
# class School(object):
#     def __init__(self):
#         self.skill = '学校古法煎饼果子技术'
#
#     def make_cake(self):
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#
# # 徒弟类
# class Prentice(School, Master):
#     def __init__(self):
#         self.skill = '独创古法煎饼果子技术'
#
#     def make_cake(self):
#         # *****为了防止调用父类初始化时候覆盖子类初始化，需要重新初始化*****
#         self.__init__()
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#     # 子类调用父类的同名属性和方法：把父类的同名属性和方法再封装
#     def master_make_cake(self):
#         # ***因为同名属性在init初始化位置，为了获取父类的同名属性，需要再次初始化***
#         Master.__init__(self)
#         Master.make_cake(self)
#
#     def school_make_cake(self):
#         School.__init__(self)
#         Master.make_cake(self)
#
#
# # 徒孙类
# class TuSun(Prentice):
#     pass
#
#
# test = TuSun()
# test.make_cake()
# test.master_make_cake()
# test.school_make_cake()


# super()调用父类属性和方法
# 师傅类
# class Master(object):
#     def __init__(self):
#         self.skill = '师傅古法煎饼果子技术'
#
#     def make_cake(self):
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#
# # 学校类
# class School(Master):
#     def __init__(self):
#         self.skill = '学校古法煎饼果子技术'
#
#     def make_cake(self):
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#         # 2.1 super(当前类名，self).函数名()
#         # super(School, self).__init__()
#         # super(School, self).make_cake()
#
#         # 2.2 super()无参数写法
#         super().__init__()
#         super().make_cake()
#
#
# # 徒弟类
# class Prentice(School):
#     def __init__(self):
#         self.skill = '独创古法煎饼果子技术'
#
#     def make_cake(self):
#         # *****为了防止调用父类初始化时候覆盖子类初始化，需要重新初始化*****
#         self.__init__()
#         print('运用{}制作煎饼果子'.format(self.skill))
#
#     # 子类调用父类的同名属性和方法：把父类的同名属性和方法再封装
#     def master_make_cake(self):
#         # ***因为同名属性在init初始化位置，为了获取父类的同名属性，需要再次初始化***
#         Master.__init__(self)
#         Master.make_cake(self)
#
#     def school_make_cake(self):
#         School.__init__(self)
#         Master.make_cake(self)
#
#     # 一次性调用Master和School的同名属性和方法
#     def old_make_cake(self):
#         # 方法一：代码冗余，如果父类名变化，需要大量修改
#         # Master.__init__(self)
#         # Master.make_cake(self)
#         # School.__init__(self)
#         # School.make_cake(self)
#
#         # 方法二：super()
#         # 2.1 super(当前类名，self).函数名()
#         # super(Prentice, self).__init__()
#         # super(Prentice, self).make_cake()
#         # 上面代码只是调用了School的属性和方法，如果要调用Master的属性和方法，要在对应位置也加上super
#
#         # 2.2 super()无参数写法
#         # super()会自动调用父类，调用顺序遵循__mro__，适合单继承
#         super().__init__()
#         super().make_cake()
#         # 上面代码只是调用了School的属性和方法，如果要调用Master的属性和方法，要在对应位置也加上super
#
# test = Prentice()
# test.old_make_cake()


# 私有权限
# 师傅类
class Master(object):
    def __init__(self):
        self.skill = '师傅古法煎饼果子技术'

    def make_cake(self):
        print('运用{}制作煎饼果子'.format(self.skill))


# 学校类
class School(object):
    def __init__(self):
        self.skill = '学校古法煎饼果子技术'

    def make_cake(self):
        print('运用{}制作煎饼果子'.format(self.skill))


# 徒弟类
class Prentice(School, Master):
    def __init__(self):
        self.skill = '独创古法煎饼果子技术'
        # 私有属性money
        self.__money = 200000

    # 定义函数：获取私有属性
    def get_money(self):
        return  self.__money

    # 定义函数：修改私有属性
    def set_money(self, money):
        self.__money = money

    # 私有方法
    def __print_info(self):
        print('这是私有方法')

    def make_cake(self):
        # *****为了防止调用父类初始化时候覆盖子类初始化，需要重新初始化*****
        self.__init__()
        print('运用{}制作煎饼果子'.format(self.skill))

    # 子类调用父类的同名属性和方法：把父类的同名属性和方法再封装
    def master_make_cake(self):
        # ***因为同名属性在init初始化位置，为了获取父类的同名属性，需要再次初始化***
        Master.__init__(self)
        Master.make_cake(self)

    def school_make_cake(self):
        School.__init__(self)
        Master.make_cake(self)


# 徒孙类
class TuSun(Prentice):
    pass

test = TuSun()

print(test.get_money())

test.set_money(1000)
print(test.get_money())




