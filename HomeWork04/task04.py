# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
import random
first_path = r'first.txt'
second_path = r'second.txt'
def appended_new_koef () -> list[int]:
    koef_k = int(input('Введите степень k: '))
    koef_list = []
    i = 0
    while i <= koef_k:
        koef_list.append(random.randint(0, 100))
        i += 1
    print(koef_list)
    return koef_list
def create_new_equation(list_koef :list[int]) -> str:
    equation = ''
    for i in range(len(list_koef)):
        if list_koef[i] == 0:
            continue
        elif list_koef[i] > 0:
            if list_koef[i] == 1 and (len(list_koef) - 1 - i) > 0:
                if (len(list_koef) - 1 - i) > 1:
                    equation = equation + f'x**{len(list_koef) - 1 - i} + '
                elif (len(list_koef) - 1 - i) == 1:
                    equation = equation + f'x + '
            else:
                if (len(list_koef) - 1 - i) > 1:
                    equation = equation + f'{list_koef[i]} * x**{len(list_koef) - 1 - i} + '
                elif (len(list_koef) - 1 - i) == 1:
                    equation = equation + f'{list_koef[i]} * x + '
                elif (len(list_koef) - 1 - i) == 0:
                    equation = equation + f'{list_koef[i]}'
    else:
        equation = equation + ' = 0'
    return equation
# print(create_new_equation(appended_new_koef()))
with open(first_path, 'a') as first_data:
    first_data.write(create_new_equation(appended_new_koef()))
    first_data.close()
with open(second_path, 'a') as second_data:
    second_data.write(create_new_equation(appended_new_koef()))
    second_data.close()


