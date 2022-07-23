from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# menu_1
_1 = KeyboardButton("Меню")
_2 = KeyboardButton("Інформація про бота")
menu = ReplyKeyboardMarkup(resize_keyboard=True).add(_1).add(_2)


# Other
_3 = KeyboardButton("button 3")
_4 = KeyboardButton("button 4")
_5 = KeyboardButton("↙ Вернуться назад")
menu_1 = ReplyKeyboardMarkup(resize_keyboard=True).add(_3, _4).add(_5)


# information_Bot
Info_1 = KeyboardButton("Возможности бота")
Info_2 = KeyboardButton("Для чого был он создан")
Info_3 = KeyboardButton("↙ Вернуться назад")
menu_info = ReplyKeyboardMarkup(resize_keyboard=True).add(Info_1, Info_2).add(Info_3)
