# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
import create_new_equation as create
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

# first_equation = create.create_new_equation(appended_new_koef())
second_equation = create.create_new_equation(appended_new_koef())
with open(first_path, 'w') as first_data:
    first_data.write(create.create_new_equation(appended_new_koef()))
    first_data.close()
with open(second_path, 'w') as second_data:
    second_data.write(second_equation)
    second_data.close()


