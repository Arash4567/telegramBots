from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="BOT API TOKEN")

dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    # text = "Hello World!"

    # sendd_message = await bot.send_message(chat_id=chat_id, text=text)
    # print(sendd_message.to_python())

    # photoo = await bot.send_photo(chat_id=chat_id, photo="https://picsum.photos/500")
    # print(photoo.photo[-1].file_unique_id)

    bot_username = await bot.get_me()
    print(bot_username.username)
    print(bot_username.url)

executor.start_polling(dp)
