# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

def n_succession():
    end_number = int(input('Введите число: '))
    sum_of_numbers = 0
    num = 1
    while num <= end_number:
        elem = (1 + 1 / num) ** num
        sum_of_numbers += elem
        num += 1
    print(round(sum_of_numbers, 2))

n_succession()
