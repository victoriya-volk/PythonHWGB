# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
import random
len_my_list = int(input('Введите длинну списка: '))
def start_task_work(num):
    new_list = []
    i = 0
    while i < num:
        new_list.append(random.randint(1000, 9999))
        i += 1
    print(new_list)
    return new_list
my_list = start_task_work(len_my_list)
del_num = int(input('Введите цифру для удаления: '))

def crash_number_for_list(list_of_numbers):
    j = 0
    while j < len(my_list):
        my_list[j] = [int(a) for a in str(my_list[j])]
        j += 1
    return list_of_numbers

crash_number_for_list(my_list)

def deleted_number(list_for_deleted):
    for arr in list_for_deleted:
        k = 0
        while k < len(arr):
            if arr[k] == del_num:
                del arr[k]
            k += 1
    return list_for_deleted

deleted_number(my_list)
def list_after_deleting(list_for_split):
    step = 0
    arr_spliting = []
    while step < len(list_for_split):
        arr_spliting.append(int(''.join(map(str, list_for_split[step]))))
        step += 1
    print(arr_spliting)

list_after_deleting(my_list)

def sum_of_numbers(list_for_sum):
    elem = 0
    sum_of_list = 0
    while elem < len(list_for_sum):
        for i in list_for_sum[elem]:
            sum_of_list += i
        if sum_of_list > 9:
            while sum_of_list > 9:
                sum_of_list = int(sum_of_list / 10) + sum_of_list % 10
        list_for_sum[elem] = sum_of_list
        sum_of_list = 0
        elem += 1
    return list_for_sum

sum_of_numbers(my_list)

print(my_list)
def deleted_doubles(list_for_sort):
    index = 0
    while index < len(list_for_sort):
        step = index + 1
        while step < len(list_for_sort):
            if list_for_sort[index] == list_for_sort[step]:
                del list_for_sort[step]
            else:
                step += 1
        index += 1
    return list_for_sort

deleted_doubles(my_list)

print(my_list)
