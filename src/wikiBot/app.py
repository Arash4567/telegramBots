import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'BOT API TOKEN HERE'

logging.basicConfig(level=logging.INFO)

wikipedia.set_lang('uz')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Assalomu aleykum! Wikipedia botiga xush kelibsiz!")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):

    await message.reply("Bot bo`yicha muammo bo`lsa, men bilan bog`laning: @fullstackmaster007")

@dp.message_handler()
async def sendWiki(message: types.Message):

    try:
        response = wikipedia.summary(message.text)
        await message.answer(response)
    except:
        await message.answer('Izlash natijasi topilmadi! Iltimos qaytadan harakat qilib ko`ring!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)