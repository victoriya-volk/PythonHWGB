# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num_n = int(input('Введите Ваше число: '))
user_list = list(range(1, num_n + 1))
user_list_multi = 1
user_multi_list = []
for i in user_list:
    user_list_multi *= i
    user_multi_list.append(user_list_multi)
print(user_multi_list)

