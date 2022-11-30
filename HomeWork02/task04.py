# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

number_n = int(input("Введите число: "))

new_list = list(range(-number_n, number_n + 1))

indexes = input('Введите индексы через пробел: ')
indexes = indexes.split(' ')
my_multy = 1
for i in indexes:
    my_multy = my_multy * new_list[int(i)]
    print(my_multy)
print(new_list)
print(indexes)
