import time
from aiogram import types, executor, Dispatcher, Bot
import markups as anv
import Config

bot = Bot(token=Config.TOKEN)
dp = Dispatcher(bot)

temp_number = 0

print("Starting...")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    time.sleep(1)

    await bot.send_message(message.chat.id, f"Hi /start \n sadas", reply_markup=anv.menu)


@dp.message_handler(content_types=['text'])
async def menu_1(message: types.message):
    # menu_1
    if message.text == 'Меню':
        await bot.send_message(message.from_user.id, 'меню', reply_markup=anv.menu_1)
        await bot.delete_webhook(drop_pending_updates=True)

    elif message.text == 'Інформація про бота':
        await bot.send_message(message.from_user.id, '2', reply_markup=anv.menu_info)
    # menu_Information_Bot
    elif message.text == 'Возможности бота':
        await bot.send_message(message.from_user.id, '2', reply_markup=anv.menu)

    elif message.text == 'Для чого был он создан':
        await bot.send_message(message.from_user.id, '2', reply_markup=anv.menu)
    # menu_Other
    elif message.text == '↙ Вернуться назад':
        await bot.send_message(message.from_user.id, '2', reply_markup=anv.menu)


executor.start_polling(dp)
