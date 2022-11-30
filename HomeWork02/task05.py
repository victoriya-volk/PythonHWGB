import random
# Реализуйте алгоритм перемешивания списка.
my_number = int(input('Введите любое число: '))
my_list = list(range(-my_number, my_number + 1))

def my_shuffle (array):
    i = 0
    while i < len(array):
        new_i = random.randint(-len(array), len(array))
        shuffle_help = array[i]
        array[i] = array[new_i]
        array[new_i] = shuffle_help
        i += 1
    return array


print(my_list)
print(my_shuffle(my_list))
