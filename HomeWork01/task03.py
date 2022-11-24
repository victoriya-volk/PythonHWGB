# Напишите программу, которая принимает на вход координаты точки
# (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка.

coord_x = int(input('Введите координату X: '))
coord_y = int(input('Введите координату Y: '))
if (coord_x > 0) and (coord_y > 0):
    print('Эта точка в I четверти')
elif (coord_x < 0) and (coord_y > 0):
    print('Эта точка в II четверти')
elif (coord_x < 0) and (coord_y < 0):
    print('Эта точка в III четверти')
elif (coord_x > 0) and (coord_y < 0):
    print('Эта точка в IV четверти')
elif coord_x == 0 or coord_y == 0:
    print('Для проверки обе координаты должны быть больше 0')