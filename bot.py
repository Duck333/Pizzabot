import logging
from aiogram import Bot, Dispatcher, executor, types
import menu
import reviews
import Base

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm PizzaBot!\nCreated by aiogram.",reply_markup=menu.mainmenu)

@dp.message_handler(commands=['phones'])
async def send_welcome(message: types.Message):
    await message.reply("Номер босса: +3756694025482,\nНомер тех поддержки: +375838418669,\nНомер повара: +37594859417,\nНомер второго повара: +3758346733418.")

@dp.message_handler(commands=['menu'])
async def readTable(message: types.Message):
    await message.answer("Menu: ",Base.readTable())

@dp.message_handler(lambda message: message.text.startswith('/Makeanorder '))
async def insertData(message: types.message):
    try:
     parsed_message = (message.text[13:])
     reviews.insertData(parsed_message)
     await message.reply("Отзыв отправлен")
    except TypeError:
        await message.reply("Произошла ошибка, отзыв не добавлен")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
