from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

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

# V1.1
# inline-menu
Inl_1 = InlineKeyboardButton('TEST_1', callback_data='menu_1')
Inl_2 = InlineKeyboardButton('TEST_2_Dalle', callback_data='menu_2')
Inl_3 = InlineKeyboardButton('TEST_3', callback_data='menu_3')
Inl_menu = InlineKeyboardMarkup(resize_keyboard=True).add(Inl_1, Inl_2).add(Inl_3)

# inline-menu 2
Inl1__1 = InlineKeyboardButton('1_TEST_4', callback_data='menu_4')
Inl2__2 = InlineKeyboardButton('1_TEST_5', callback_data='menu_5')
Inl3__3 = InlineKeyboardButton('1_TEST_6_Nazad', callback_data='menu_6')
Inl__2menu = InlineKeyboardMarkup(resize_keyboard=True).add(Inl1__1, Inl2__2).add(Inl3__3)
