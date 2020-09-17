# 1. 接收用户输入目标文件名
old_name = input('请输入要备份的文件名：')

# 2. 规划备份文件名
# 2.1 提取后缀--字符串中提取最右边的.及后缀
# 找出.的位置
index = old_name.rfind('.')

# 如果输入了.txt类似的非法文件名，要添加判断
if index > 0:
    postfix = old_name[index:]

# 2.2 组建新名字
new_name = old_name[0:index] + '.backup' + postfix
print(new_name)

# 3. 备份文件写入数据
old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')

# 如果不确定写入文件大小，可使用循环读取写入，当读取数据没有了结束循环
while True:
    content = old_f.read(1024)
    if len(content) == 0:
        break
    new_f.write(content)

old_f.close()
new_f.close()