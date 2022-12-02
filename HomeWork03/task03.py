# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

example_1 = [1.1, 1.2, 3.1, 5, 10.01]
example_2 = []

def diff_of_fract_part(list_of_fract):
    i = 0
    while i < len(list_of_fract):
        list_of_fract[i] = round(list_of_fract[i] - int(list_of_fract[i]), 2)
        if list_of_fract[i] == 0:
            del list_of_fract[i]
        else:
            i += 1
    maximum = 0
    minimum = 1
    for fract in list_of_fract:
        if fract > maximum:
            maximum = fract
        elif fract < minimum:
            minimum = fract

    diff_of_fract = maximum - minimum

    return diff_of_fract
print(diff_of_fract_part(example_1))
