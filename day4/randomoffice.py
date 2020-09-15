import random


teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]


for name in teachers:
    num = random.randint(0, 2)
    offices[num].append(name)

i = 1
for office in offices:
    print('办公室{}的人数是{},老师分别是：'.format(i, len(office)))

    for name in office:
        print(name,end='\t')
    print()
    i+=1