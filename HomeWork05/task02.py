# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random

def making_a_move(player_name: str) -> int:
    player_num_sweets = int(input(f'{player_name}, сколько возьмешь конфет? '))
    if player_num_sweets > 28:
        print(f'{player_name}, попробуй еще раз и возьми не более 28 конфет')
        return making_a_move(player_name)
    elif player_num_sweets < 0:
        print(f'{player_name}, возьми хотя бы одну конфетку ;)')
        return making_a_move(player_name)
    else:
        return player_num_sweets

def botty_move(sweets: int) -> int:
    new_botty_move = sweets % 29
    print(f'Я беру {new_botty_move}')
    return new_botty_move

def turn_of_moves(player_1: str, player_2: str):
    sweets = 150
    step = 0
    while sweets >= 28:
        if step % 2 > 0:
            if player_1 == 'Botty':
                sweets = sweets - botty_move(sweets)
                print(f'Осталось {sweets} конфет на столе')
            else:
                sweets -= making_a_move(player_1)
                print(f'Осталось {sweets} конфет на столе')
            if sweets < 28:
                print(f'{player_2} победил и забирает все конфеты!')
            step += 1
        else:
            if player_2 == 'Botty':
                sweets = sweets - botty_move(sweets)
                print(f'Осталось {sweets} конфет на столе')
            else:
                sweets -= making_a_move(player_2)
                print(f'Осталось {sweets} конфет на столе')
            if sweets < 28:
                print(f'{player_2} победил и забирает все конфеты!')
            step += 1


def initialize_game_data(type_of_game: int):
    if type_of_game == 1:
        player_1 = input('Как тебя зовут?\n')
        player_2 = 'Botty'
        print(f'Меня зовут {player_2}')
        numZ = random.randint(1, 101)
        if numZ % 2 > 0:
            turn_of_moves(player_1, player_2)
        else:
            turn_of_moves(player_2, player_1)
    elif type_of_game == 2:
        player_1 = input('Как зовут первого игрока? ')
        player_2 = input('Как зовут второго игрока? ')
        numZ = random.randint(1, 101)
        if numZ % 2 > 0:
            turn_of_moves(player_1, player_2)
        else:
            turn_of_moves(player_2, player_1)


def start_game():
    user_choice = input('Это игра с конфетами) выбирай с кем будешь играть: со мной'
                        '(введи 1) \nили с другом (введи 2). \n'
                        'Если передумал играть нажми любую другую клавишу.\n')
    if user_choice == '1':
        print('Ты выбрал игру со мной! Спасибо! Давай начнем)')
        initialize_game_data(1)
    elif user_choice == '2':
        print('Ты выбрал игру с другом! Да начнется она!)')
        initialize_game_data(2)
    else:
        print('Игры не состоится( Я буду ждать тебя здесь!')

start_game()