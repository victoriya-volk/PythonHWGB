# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: 0,56 -> 11
num_z = float(input('Введите вещественное число: '))
# sum_part_num_z = 0

def magic_float_number(number):
    increases = 1
    count = 0
    while number * increases != int(number * increases):
        increases *= 10
        count += 1
    return (number * (10 ** count))

def f_sum_of_parts_number (number_for_sum):
    sum_of_parts = 0
    while number_for_sum > 0:
        sum_of_parts += number_for_sum % 10
        number_for_sum = int(number_for_sum / 10)
    else:
        return sum_of_parts


if ( 0 < num_z < 1):
    print(f_sum_of_parts_number(int(magic_float_number(num_z))))
elif (num_z >= 1):
    print(f_sum_of_parts_number(int(num_z)))
elif(-1 < num_z < 0):
    print(f_sum_of_parts_number(int(magic_float_number((-1 * num_z)))))
elif(-1 >= num_z):
    print(f_sum_of_parts_number(int(-1 * num_z)))





