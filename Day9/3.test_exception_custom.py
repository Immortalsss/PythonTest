# 自定义异常类
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return '您的密码长度是{},密码长度不能少于{}字符！'.format(self.length, self.min_len)


# 抛出异常
def main():
    try:
        con = input('请输入密码：')
        if len(con) < 3:
            raise ShortInputError(len(con), 3)
    except Exception as result:
        print(result)
    else:
        print('您的密码符合要求')


# 捕获异常
main()