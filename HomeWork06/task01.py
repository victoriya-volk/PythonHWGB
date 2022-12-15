# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

len_my_list = int(input('Введите длинну списка: '))
# def start_task_work(num: int) -> list[int]:
#     new_list = []
#     i = 0
#     while i < num:
#         new_list.append(random.randint(-9, 9))
#         i += 1
#     return new_list

# my_list = start_task_work(len_my_list)
my_list = list(random.randint(-9, 9) for i in range(0, len_my_list))
example_list = [2, 3, 5, 9, 3]

def sum_of_odd_num(list_of_num: list[int]) -> int:
    print(list_of_num)
    # sum_of_odd = 0
    # i = 0
    # while i < len(list_of_num):
    #     if i % 2 > 0:
    #         sum_of_odd += list_of_num[i]
    #     i += 1
    sum_of_odd = 0
    list_of_num = list(enumerate(list_of_num))
    for i in list_of_num:
        if i[0] % 2 > 0:
            sum_of_odd += i[1]
    print(sum_of_odd)

sum_of_odd_num(my_list)
sum_of_odd_num(example_list)
