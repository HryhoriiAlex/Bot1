from aiogram import Bot, Dispatcher, executor, types
from buttons import ikb, kb
from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Ласкаво просимо до мого бота!", reply_markup=kb)

@dp.message_handler(commands=["links"])
async def command_link(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Оберіть посилання", reply_markup=ikb)

async def on_startup(_):
    print("Бот був успішно запущений!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


#lesson 10