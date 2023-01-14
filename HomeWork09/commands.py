import random

from bot_config import dp, bot
from aiogram import types

total = 0

@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Сложный")],
        [types.KeyboardButton(text="Легкий")],
        [types.KeyboardButton(text="Выход")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери сложность игры, если осмелишься)"
    )
    await message.answer("Какой уровень сложности хочешь выбрать?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Выход")
async def exit_btn(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name},  не хочешь играть? '
                                                 f'Хорошо, поиграем в другой раз.',
                           reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(lambda message: message.text == "Сложный")
async def hard_level(message: types.Message):
    global total
    total = 150
    await message.reply("Сложный уровень... Посмотрим как у тебя получится меня обыграть)))",
                        reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                      f', игра началась!')
    await bot.send_message(message.from_user.id, text=f'На столе лежит {total} конфет.'
                                                      f'Сколько конфет хочешь взять, '
                                                      f'{message.from_user.first_name}?')

    async def player_tern(message):
        await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, '
                                                          f'теперь твой ход.')

    async def bot_move(message):
        global total
        if total > 28:
            step = total % 29
            total -= step
            await bot.send_message(message.from_user.id, f'Я беру {step} конфет. '
                                                         f'На столе остается {total}')
            await player_tern(message)
        else:
            await bot.send_message(message.from_user.id, f'Я забираю все конфеты и выигрываю!')
            await start_bot(message)
    @dp.message_handler()
    async def candies_game(message: types.Message):
        global total
        if total > 28:
            if message.text.isdigit():
                if 0 < int(message.text) < 29:
                    total -= int(message.text)
                    await bot.send_message(message.from_user.id, f'{message.from_user.first_name} '
                                                                 f'взял со стола {message.text} конфет.'
                                                                 f'На столе осталось {total} конфет.')
                    await bot_move(message)
                else:
                    await message.reply(f'{message.from_user.first_name} возьми поменьше, не будь жадиной!')
            else:
                await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                             f', не хочешь играть так и скажи! '
                                                             f'Или введи число и мы будем играть.')
        else:
            await bot.send_message(message.from_user.id, f'Забирай эти конфеты и победу!')
            await start_bot(message)


@dp.message_handler(lambda message: message.text == "Легкий")
async def light_level(message: types.Message):
    global total
    total = 150
    await message.reply("Легкий уровень? Сомневаешься в себе?", reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                      f', игра началась!')
    await bot.send_message(message.from_user.id, text=f'На столе лежит {total} конфет.'
                                                      f'Сколько конфет хочешь взять, '
                                                      f'{message.from_user.first_name}?')

    async def player_tern(message):
        await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, '
                                                          f'теперь твой ход.')
    async def bot_move(message):
        global total
        if total > 28:
            step = random.randint(0, 28)
            total -= step
            await bot.send_message(message.from_user.id, f'Я беру {step} конфет. '
                                                         f'На столе остается {total}')
            await player_tern(message)
        else:
            await bot.send_message(message.from_user.id, f'Я забираю все конфеты и выигрываю!')
            await start_bot(message)

    @dp.message_handler()
    async def candies_game(message: types.Message):
        global total
        if total > 28:
            if message.text.isdigit():
                if 0 < int(message.text) < 29:
                    total -= int(message.text)
                    await bot.send_message(message.from_user.id, f'{message.from_user.first_name} '
                                                                 f'взял со стола {message.text} конфет.'
                                                                 f'На столе осталось {total} конфет.')
                    await bot_move(message)
                else:
                    await message.reply(f'{message.from_user.first_name} возьми поменьше, не будь жадиной!')
            else:
                await bot.send_message(message.from_user.id, f'{message.from_user.first_name} '
                                                             f'не хочешь играть так и скажи! '
                                                             f'Или введи число и мы будем играть.')
        else:
            await bot.send_message(message.from_user.id, f'Забирай эти конфеты и победу!')
            await start_bot(message)

@dp.message_handler(commands=['stop'])
async def stop_bot(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name},  cпасибо за игру! '
                                                 f'Если захочешь еще поиграть, я здесь)')

@dp.message_handler(commands=['help'])
async def help_bot(message: types.Message):
    await bot.send_message(message.from_user.id, f'Это бот для игры в Конфетки.\n'
                                                 f'Правила: на столе лежат конфеты, мы по очереди берем их.'
                                                 f' За ход можно взять не более 28. '
                                                 f'Побеждает забравший последнюю конфету.'
                                                 f'Звучит скучновато, но давай попробуем?')
    await bot.send_message(message.from_user.id, f'/start\n /stop\n /help')

