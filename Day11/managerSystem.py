# 存放数据的位置：文件（student.data）
# 加载文件数据，修改文件数据并保存

# 数据存储形式：列表

# 系统功能：增加学员，删除学员，修改学员信息，查询学员信息，显示所有学员信息，保存学员信息，退出系统

from Day11.student import *


class StudentManager(object):
    def __init__(self):
        # 存储数据的列表
        self.student_list = []

    # 程序入口函数
    def run(self):
        # 1.加载文件中的学员数据
        self.load_student()

        while True:
            # 2. 显示功能菜单
            self.show_menu()

            # 3. 用户输入功能选项
            menu_num = int(input('请输入您所需要的功能：'))

            # 4. 根据用户输入执行不同功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统
                break


    # 系统功能函数
    # 加载学员信息
    def load_student(self):
        print('加载学员信息')

    # 显示功能菜单
    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员信息')
        print('6.保存学员信息')
        print('7.退出系统')

    # 添加学员
    def add_student(self):
        # 1.用户输入姓名，性别，手机号
        name = input('请输入要添加的学员姓名：')
        gender = input('请输入添加的学员性别：')
        tel = input('请输入添加的学员手机号：')

        # 2.创建学员对象
        student = Student(name, gender, tel)

        # 3.添加到学员列表
        self.student_list.append(student)

        # print(self.student_list)
        # print(student)

    # 删除学员
    def del_student(self):
        # 1.输入学员姓名
        del_name = input('请输入要删除的学员姓名：')

        # 2.遍历列表，存在即删除，不存在报错
        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)
                break
        else:
            print('查无此人')

        # result = self.student_list
        # print(result)

    # 修改学员信息
    def modify_student(self):
        # 1.输入学员姓名
        modify_name = input('请输入要修改的学员姓名：')

        # 2.遍历列表，存在即修改，不存在报错
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input('请输入姓名：')
                i.gender = input('请输入性别：')
                i.tel = input('请输入手机号：')
                print('修改学员信息成功，姓名{},性别{},手机号{}'.format(i.name, i.gender, i.tel))
                break
        else:
            print('查无此人')

    # 查询学员信息
    def search_student(self):
        # 1.输入学员姓名
        search_name = input('请输入要查询的学员姓名：')

        # 2.遍历列表，存在即打印信息，不存在报错
        for i in self.student_list:
            if search_name == i.name:
                print('学员姓名{},性别{},手机号{}'.format(i.name, i.gender, i.tel))
                break
        else:
            print('查无此人')

    # 显示所有学员信息
    def show_student(self):
        # 打印表头
        print('姓名\t性别\t手机号')
        # 打印信息
        for i in self.student_list:
            print('{}\t\t{}\t\t{}'.format(i.name, i.gender, i.tel))

    # 保存学员信息
    def save_student(self):
        # 打开文件
        f = open('student.data', 'w')

        # 写入数据
        # 写入的数据不能是内存地址，要转换为列表中的字典数据
        new_list = [i.__dict__ for i in self.student_list]
        # print(new_list)

        # 文件要求写入类型为字符串
        f.write(str(new_list))

        # 关闭文件
        f.close()









