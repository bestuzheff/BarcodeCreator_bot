from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from dotenv import load_dotenv


load_dotenv()


# Получаем TOKEN бота из переменной окружения
bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")
bot = Bot(token=bot_token)


# Диспетчер для бота
dp = Dispatcher(bot)

# Хэндлер на команду /start
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    text_message = "Barcode Creator Бот генерирует изображение штрихкода или QR-кода по переданной ему строке.\n"
    text_message = text_message + "Просто отправь боту строку с кодом и он обратно пришлет изображение."
                                        
    await message.answer(text_message)


@dp.message_handler()
async def create_barcode(message: types.Message):
    await message.answer("Hi! QR-code")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
