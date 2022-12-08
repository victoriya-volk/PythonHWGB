# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141
# Ввод: 0.01
#     Вывод: 3.14
#
#     Ввод: 0.001
#     Вывод: 3.141
numP = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899582
exactness = float(input('Введите точность округления числаё: '))
def round_the_number(num_for_round: float, user_exactness: float) -> float:
    increase = 1
    step = 0
    while user_exactness * increase != int(user_exactness * increase):
        increase *= 10
        step += 1
    num_for_round = int(num_for_round * (increase)) / increase
    return num_for_round

print(round_the_number(numP, exactness))

