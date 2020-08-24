mystr = 'hello world and itcast and itheima and Python'

# startwith(子串，开始下标，结束下标):返回值为bool类型
print(mystr.startswith('hello'))
print(mystr.startswith('he'))
print(mystr.startswith('hels'))

# endswith(子串，开始下标，结束下标):返回值为bool类型
print(mystr.endswith('Python'))
print(mystr.endswith('thons'))

# isalpha():判断字符串是否全为字符

# isdigit():判断字符串是否全为数字

# isalnum():判断字符串是否全为字符或全为数字或组合

# isspace():判断字符串是否全为空格