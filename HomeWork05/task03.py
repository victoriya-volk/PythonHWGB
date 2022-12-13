# Создайте программу для игры в ""Крестики-нолики"".
playing_field = [['1', '2', '3'],
                 ['4', '5', '6'],
                 ['7', '8', '9']]

def drowing_plaing_field(playing_field: list[list[int | str]]):
    for i in range(0, len(playing_field)):
        for j in range(0, len(playing_field[i])):
            if j == 0:
                print(f'|{playing_field[i][j]}|', end='')
            else:
                print(f'{playing_field[i][j]}|', end='')
        print()

drowing_plaing_field(playing_field)

def players_cell(field: list[int | str], sign: str) -> list[str | int]:
    player_cell = int(input('Введите номер ячейки:'))
    if 1 > player_cell > 9:
        player_cell = int(input('Введите номер ячейки еще раз:'))
    else:
        for i in range(0, len(field)):
            for j in range(0, len(field[i])):
                if field[i][j] == str(player_cell):
                    field[i][j] = sign
                    break
        drowing_plaing_field(field)
        return field

def checking_winners(field):
    for row in field:
        if row[0] == row[1] == row[2]:
            return True


def turn_of_movies() -> str:
    i = 0
    while i < 9:
        if checking_winners(playing_field) == True:
            print('Победитель найден')
            break
        else:
            if i % 2 > 0:
                players_cell(playing_field, 'X')
            else:
                players_cell(playing_field, '0')
            i += 1
    return 'Спасибо за игру!'


turn_of_movies()

