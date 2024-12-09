# Бот поддержки (Начало)

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api=''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.reply("Привет! Я бот помогающий твоему здоровью.")

# Обработчик всех остальных сообщений
@dp.message_handler(lambda message: True)
async def all_messages(message: types.Message):
    print("Введите команду /start, чтобы начать общение.")
    await message.reply("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

