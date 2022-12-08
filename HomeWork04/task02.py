# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
numZ = int(input('Введите число для проверки простых множителей: '))
def factorize(num: int) -> list[int]:
    nums_list = []
    i = 2
    while i <= (num ** 0.5 + 1):
        while num % i == 0:
            nums_list.append(i)
            num = int(num / i)
        else:
            i += 1
    if num != 1:
        nums_list.append(num)
    return nums_list

print(factorize(numZ))

