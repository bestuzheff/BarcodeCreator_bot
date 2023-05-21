import qrcode
import barcode
from barcode.writer import ImageWriter
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


def get_file_name():
    import random
    import string
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(16))
    return rand_string


# Хэндлер на команду /start
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    text_message = "'Barcode Creator Бот' генерирует изображение штрихкода или QR-кода по переданной ему строке.\n"
    text_message = text_message + "Просто отправь боту строку с кодом и он обратно пришлет изображение."
                                        
    await message.answer(text_message)


@dp.message_handler()
async def create_barcode(message: types.Message):
    chat_id = message.chat.id
    array_of_messages = message.text.split("\n")
    for mess in array_of_messages:
        if mess.isdigit():
            if len(mess) == 13:
                code = barcode.get('ean13', mess, writer=ImageWriter())
            else:
                code = barcode.get('code128', mess, writer=ImageWriter())
            filename = code.save('codes/' + get_file_name())
        else:
            qrimage = qrcode.make(mess)
            filename = 'codes/' + get_file_name()+'.png'
            qrimage.save(filename)
        photo = open(filename, 'rb')
        await bot.send_photo(chat_id, photo)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
