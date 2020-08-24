i = 1
result = 0

while i <= 100:
    result += i
    i += 1
print('result = {}'.format(result))

j = 1
result_even = 0

while j <= 100:
    if j % 2 == 0:
        result_even += j
    j += 1
print('result_even = {}'.format(result_even))
