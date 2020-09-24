import time

try:
    f = open('test.txt', 'r')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        print('程序被意外终止')
except:
    print('该文件不存在')