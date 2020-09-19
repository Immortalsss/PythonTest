# 定义地瓜类：初始化属性，被烤和添加调料方法，显示信息str
class SweetPotato(object):
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cook_state = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            self.cook_state  = '糊了'
        else:
            print('您输入的时间有误')

    def add_condiments(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return  '这个地瓜烤了{}分钟，目前状态是{}，调料有{}'.format(self.cook_time, self.cook_state, self.condiments)


# 创建对象，调用对应的方法
digua1 = SweetPotato()

print(digua1)

digua1.cook(2)
digua1.add_condiments('胡椒')
print(digua1)

digua1.cook(2)
digua1.add_condiments('酱油')
print(digua1)
