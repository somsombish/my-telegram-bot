import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import yt_dlp

API_TOKEN = os.getenv("API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def download_video(url):
    ydl_opts = {
        'outtmpl': 'video.%(ext)s',
        'format': 'best[ext=mp4]',
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@dp.message_handler()
async def handle_message(message: types.Message):
    text = message.text

    if "http" in text:
        await message.reply("Идёт скачивание...")

        try:
            download_video(text)

            # ищем скачанный файл
            for file in os.listdir():
                if file.startswith("video"):
                    await message.answer_document(open(file, "rb"))
                    os.remove(file)
                    break

        except Exception as e:
            await message.reply("Ошибка 404")
            print(e)
    else:
        await message.reply("Отправьте ссылку :")

if name == 'main':
    executor.start_polling(dp, skip_updates=True)
    executor.start_polling(dp, skip_updates=True)
