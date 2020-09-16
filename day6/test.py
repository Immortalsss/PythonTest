# fn1 = lambda:100
# print(fn1())



# fn2 = lambda a : a
# print(fn2('hello world'))



# fn3 = lambda a, b, c=100 : a + b + c
# print(fn3(10, 20))



# fn5 = lambda **kwargs: kwargs
# print(fn5(name = 'Python', age = 10))



# def sum_num(a, b, f):
#     return f(a) + f(b)
#
# result  = sum_num(-1, 9, abs)
# print(result)


# map()
# list1 = [1,2,3,4]
#
# def func(x):
#     return x ** 2
#
# result = map(func,list1)
#
# print(result)
# print(list(result))


# reduce()
# list1 = [1,2,3,4,5]
#
# import functools
#
# def func(a,b):
#     return a+b
#
# result = functools.reduce(func,list1)
# print(result)


# filter()
list1 = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x % 2 == 0

result = filter(func,list1)

print(result)
print(list(result))



