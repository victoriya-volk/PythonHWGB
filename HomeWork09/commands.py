from bot_config import dp, bot
from aiogram import types

total = 150

@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    global total
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                      f', игра началась!')
    await bot.send_message(message.from_user.id, text=f'На столе лежит {total} конфет.'
                                                      f'Сколько конфет хочешь взять, '
                                                      f'{message.from_user.first_name}?')

@dp.message_handler()
async def candies_game(message: types.Message):
    global total
    if total > 29:
        if message.text.isdigit():
            if 0 < int(message.text) < 29:
                total -= int(message.text)
                await bot.send_message(message.from_user.id, f'{message.from_user.first_name} '
                                                             f'взял со стола {message.text} конфет.'
                                                             f'На столе осталось {total} конфет.')
            else:
                await message.reply(f'{message.from_user.first_name} возьми поменьше, не будь жадиной!')
        else:
            await bot.send_message(message.from_user.id, f'{message.from_user.first_name} '
                                                     f', не хочешь играть так и скажи! '
                                                     f'Или введи число и мы будем играть.')
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, ты выиграл!')


@dp.message_handler()
async def bot_move(message: types.Message):
    global total
    if total > 29:
        step = total % 29
        total -= step
        await bot.send_message(message.from_user.id, f'Я беру {step} конфет. '
                                                     f'На столе остается{total}')
    else:
        await bot.send_message(message.from_user.id, f'Я выиграл!')

