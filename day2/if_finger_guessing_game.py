import random

player = int(input('请出拳：0--石头，1--剪刀，2--布：'))

computer = random.randint(0, 2)

print(f'电脑出拳是：{computer}')

if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('玩家获胜')
elif ((player == 0) and (computer == 0)) or ((player == 1) and (computer == 1)) or ((player == 2) and (computer == 2)):
    print('平局')
else:
    print('电脑获胜')
    
