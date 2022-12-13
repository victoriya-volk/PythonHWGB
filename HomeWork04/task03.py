# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

my_list = [0, 1, 1, 2, 3, 4, 4, 4, 5]

def deleted_double_nums(user_list: list[int]) -> list[int]:
    count = 0
    list_unic_nums = []
    for check in range(len(user_list)):
        i = 0
        while i < len(user_list):
            if user_list[check] == user_list[i]:
                count += 1
            i += 1
        if count == 1:
            list_unic_nums.append(user_list[check])
        count = 0
    return list_unic_nums

print(deleted_double_nums(my_list))
