# 定义类：房屋类，家具类
# 家具类：家具名称，占地面积
class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area

# 房屋类：地理位置，总面积，剩余面积，家具列表，实例方法：容纳家具，显示家具信息
class House(object):
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []

    def add_furniture(self, item):
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('家具太大，无法容纳')

    def __str__(self):
        return '房屋位于{},占地面积为{},剩余面积为{},现有家具{}'\
            .format(self.address, self.area, self.free_area, self.furniture)


home = House('北京', 1000)
print(home)

bed = Furniture('双人床', 6)
home.add_furniture(bed)
print(home)

sofa = Furniture('沙发', 5)
home.add_furniture(sofa)
print(home)


