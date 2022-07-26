import time
from aiogram import types, executor, Dispatcher, Bot
import markups as anv
import Config

bot = Bot(token=Config.TOKEN)
dp = Dispatcher(bot)

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
        await bot.send_message(message.from_user.id, '2', reply_markup=anv.Inl_menu)

    elif message.text == 'Для чого был он создан':
        await bot.send_message(message.from_user.id, '2', reply_markup=anv.Inl_menu)
    # menu_Other
    elif message.text == '↙ Вернуться назад':
        await bot.send_message(message.from_user.id, '2', reply_markup=anv.menu)

# V1.1
@dp.callback_query_handler(text_contains='menu_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("menu_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.edit_text('TEST_1', reply_markup=anv.Inl_menu)
        if code == 2:
            await call.message.edit_text('TEST_2_dalle', reply_markup=anv.Inl__2menu)
        if code == 3:
            await call.message.edit_text('TEST_3', reply_markup=anv.Inl_menu)
        if code == 4:
            await call.message.edit_text('TEST_4', reply_markup=anv.Inl__2menu)
        if code == 5:
            await call.message.edit_text('TEST_5', reply_markup=anv.Inl__2menu)
        if code == 6:
            await call.message.edit_text('TEST_6_Nazad', reply_markup=anv.Inl_menu)
        else:
            await bot.answer_callback_query(call.id)

executor.start_polling(dp)
