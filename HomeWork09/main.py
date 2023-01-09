from aiogram.utils import executor
from commands import dp

async def bot_start(_):
    print('Bot took off!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=bot_start)
