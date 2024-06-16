from config import token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from data import welcome_input, goodbye_input
from funcs import Response

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler()
async def echo_message(msg: types.Message):
    if (msg.text).lower() in welcome_input:
        await msg.answer('Привет!')
    elif (msg.text).lower() in goodbye_input:
        await msg.answer('Буду ждать вас!')
    else:
        await msg.answer('Дайте подумать...')
        await msg.answer(Response(msg.text))

if __name__ == '__main__':
    executor.start_polling(dp)