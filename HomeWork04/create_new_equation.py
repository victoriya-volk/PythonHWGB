def create_new_equation(list_koef :list[int]) -> str:
    equation = ''
    for i in range(len(list_koef)):
        if list_koef[i] == 0:
            continue
        elif list_koef[i] > 0:
            if list_koef[i] == 1 and (len(list_koef) - 1 - i) > 0:
                if (len(list_koef) - 1 - i) > 1:
                    equation = equation + f'x**{len(list_koef) - 1 - i} + '
                elif (len(list_koef) - 1 - i) == 1:
                    equation = equation + f'x + '
            else:
                if (len(list_koef) - 1 - i) > 1:
                    equation = equation + f'{list_koef[i]} * x**{len(list_koef) - 1 - i} + '
                elif (len(list_koef) - 1 - i) == 1:
                    equation = equation + f'{list_koef[i]} * x + '
                elif (len(list_koef) - 1 - i) == 0:
                    equation = equation + f'{list_koef[i]}'
    else:
        equation = equation + ' = 0'
    return equation