from math import sqrt
# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

coord_A_x = int(input('Введите координату X точки A: '))
coord_A_y = int(input('Введите координату Y точки A: '))
coord_A_z = int(input('Введите координату Z точки A: '))

coord_B_x = int(input('Введите координату X точки B: '))
coord_B_y = int(input('Введите координату Y точки B: '))
coord_B_z = int(input('Введите координату Z точки B: '))


distance = sqrt(((coord_B_x - coord_A_x)**2) + ((coord_B_y - coord_A_y)**2) + ((coord_B_z - coord_A_z)**2))
print(round(distance, 2))

