# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).
import create_new_equation as create
import create_new_equation
first_path = r'first.txt'
second_path = r'second.txt'
result_path = r'result.txt'

with open(first_path, 'r') as first_data:
    first_equation = first_data.read()
    first_data.close()
with open(second_path, 'r') as second_data:
    second_equation = second_data.read()
    second_data.close()


def get_the_numbers(equation: str) -> list[int]:
    equation = equation.replace(' ', '')
    equation = equation[:-2].split('+')
    equation_numbers = []
    for item in equation:
        equation_numbers.append(item.split('*x')[0])
    i = 0
    while i < len(equation_numbers):
        if 'x' in equation_numbers[i]:
            equation_numbers[i] = '1'
        i += 1
    return equation_numbers

def add_lists_of_numbers(first_list : list[str], second_list : list[str]) -> list[int]:
    numbers_for_new_equation = []
    if len(first_list) == len(second_list):
        i = 0
        while i < len(first_list):
            numbers_for_new_equation.append(int(first_list[i]) + int(second_list[i]))
            i += 1
    elif len(first_list) > len(second_list):
        i = 0
        differ = len(first_list) - len(second_list)
        numbers_for_new_equation = list(map(int, first_list))
        while i < len(second_list):
            numbers_for_new_equation[i + differ] = numbers_for_new_equation[i + differ] + int(second_list[i])
            i += 1
    elif len(first_list) < len(second_list):
        i = 0
        differ = len(second_list) - len(first_list)
        numbers_for_new_equation = list(map(int, second_list))
        while i < len(first_list):
            numbers_for_new_equation[i + differ] = numbers_for_new_equation[i + differ] + int(first_list[i])
            i += 1
    return numbers_for_new_equation

new_list = add_lists_of_numbers(get_the_numbers(first_equation), get_the_numbers(second_equation))

with open(result_path, 'w') as result_data:
    result_data.write(create.create_new_equation(new_list))
    result_data.close()

