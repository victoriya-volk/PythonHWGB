# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

example_1 = [2, 3, 4, 5, 6]
example_2 = [2, 3, 5, 6]

def arr_of_multi_pairs(list_of_num: list[int]) -> list[int]:
    count_pairs = round(len(list_of_num)/2)
    if count_pairs < len(list_of_num) / 2:
        count_pairs += 1
    arr_of_multis = [list_of_num[i] * list_of_num[len(list_of_num) - i - 1] for i in range(count_pairs)]
    # i = 0
    # while i < count_pairs:
    #     arr_of_multis.append(list_of_numbers[i] * list_of_numbers[len(list_of_numbers) - i - 1])
    #     i += 1
    return arr_of_multis

print(arr_of_multi_pairs(example_1))
print(arr_of_multi_pairs(example_2))