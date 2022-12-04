# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def num_in_binary_sistem(num: int) -> str:
    text = ' в двоичной системе это ' + str(num)
    arr_of_binary_nums = []
    i = 0
    while num > 0:
        arr_of_binary_nums.insert(0, num % 2)
        i += 1
        num = int(num/2)
    i = 0
    while i < len(arr_of_binary_nums):
        print(arr_of_binary_nums[i], end='')
        i += 1
    return text


print(num_in_binary_sistem(45))
print(num_in_binary_sistem(75))
print(num_in_binary_sistem(97))
print(num_in_binary_sistem(3))
