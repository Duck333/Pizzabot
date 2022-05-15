from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#----------main menu-----------

btnmenu = KeyboardButton('/Menu')
btnmakeanorder = KeyboardButton('/Makeanorder')
btngivefeedback = KeyboardButton('/Givefeedback')
btnphonesforhelp = KeyboardButton('/Phones')

mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnmenu, btnmakeanorder, btngivefeedback, btnphonesforhelp)
