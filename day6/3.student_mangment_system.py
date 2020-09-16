# 定义功能界面函数
def info_print():
    print('------请选择功能------')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员')
    print('4、查询学员')
    print('5、显示所有学员')
    print('6、退出系统')
    print('-' * 21)


# 定义一个列表，存储学员信息，信息类型为字典
info = []


# 添加学员信息的函数
def add_info():
    # 1.用户输入信息并保存
    user_id = int(input('请输入学员学号：'))
    user_name = input('请输入学员姓名：')
    user_tel = input('请输入学员电话号码：')

    # 2.判断是否添加这个学员数据：如果存在重名，报错；否则添加
    global info

    # 2.1 存在重名，即判断输入的user_name和列表中字典的name对应的值是否相等
    for i in info:
        if user_name == i['name']:
            print('此用户已存在')
            return

    # 2.2.不存在重名，添加学员数据：准备空字典，字典添加数据，列表追加数据
    info_dict = {'id': user_id, 'name': user_name, 'tel': user_tel}

    info.append(info_dict)

    print(info)


# 删除学员信息的函数
def del_info():
    # 1.输入要删除的学员姓名
    del_name = input('请输入要删除的学员姓名：')

    # 2.如果存在，删除数据，如果不存在，提示报错信息
    global info

    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('{}不存在'.format(del_name))

    print(info)


# 修改学员信息的函数
def modify_info():
    # 1.输入要修改的学员姓名
    modify_name = input('请输入要修改的学员姓名：')

    # 2.如果存在，修改学员的手机号，如果不存在，提示报错信息
    global info

    for i in info:
        if modify_name == i['name']:
            i['tel'] = input('请输入新的手机号：')
            break
    else:
        print('{}不存在'.format(modify_name))

    print(info)


# 查询学员信息的函数
def search_info():
    # 1.输入要查询的学员姓名
    search_name = input('请输入要查询的学员姓名：')

    # 2.如果存在，打印学员的信息，如果不存在，提示报错信息
    global info

    for i in info:
        if search_name == i['name']:
            print('学员{}的信息如下------'.format(search_name))
            print('学号={},姓名={},手机号={}'.format(i['id'], i['name'], i['tel']))
            break
    else:
        print('{}不存在'.format(search_name))


# 打印所有学员信息的函数
def print_all():
    # 1.打印提示信息
    print('学号 姓名 手机号')

    # 2.打印所有学员信息
    global info
    for i in info:
        print('{}\t{}\t{}\t'.format(i['id'], i['name'], i['tel']))


# 系统功能需要循环使用，直到用户输入6，才退出系统
while True:
    # 1、显示功能选择
    info_print()

    # 2、用户输入功能序号
    user_num = int(input('请输入要选择的功能序号：'))

    # 3、根据输入的序号选择执行相应的功能
    if user_num == 1:
        add_info()
    elif user_num == 2:
        del_info()
    elif user_num == 3:
        modify_info()
    elif user_num == 4:
        search_info()
    elif user_num == 5:
        print_all()
    elif user_num == 6:
        exit_flag = input('确定要退出吗？（Y/N）:')
        if exit_flag == 'Y' or exit_flag == 'y':
            break
    else:
        print('输入的功能序号有误')