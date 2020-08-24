j = 1
while j <= 9:
    # 打印一行
    i = 1
    while i <= j:
        print('{} * {} = {}'.format(i, j, i*j), end='\t')
        i += 1
    # 打印一行后换行
    print()
    j += 1
