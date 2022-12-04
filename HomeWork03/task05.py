# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

user_number = int(input('Введите количество чисел в последовательностях Фибоначчи и Негафибоначчи: '))
def fib(n:int) -> int:
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def negafib(n:int) -> int:
    if n == -1:
        return 1
    elif n == -2:
        return -1
    elif n == -3:
        return 2
    else:
        return negafib(n+2) - negafib(n+1)
def f_list_negafib(number: int) -> list:
    listfib = [0]
    for e in range(1, user_number):
        listfib.append(fib(e))
        listfib.insert(0, negafib(-e))
    return listfib

print(f_list_negafib(user_number))
