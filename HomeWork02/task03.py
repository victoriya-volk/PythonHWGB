# списокЗадайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06
new_number = int(input('Введите число: '))
new_list = []
while new_number != len(new_list):
    new_list.append((1+1/new_number)**new_number)
print(new_list)
