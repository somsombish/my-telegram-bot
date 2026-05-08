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
        'outtmpl': 'video.mp4',
        'format': 'best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
@dp.message_handler()
async def handle_message(message: types.Message):
    text = message.text
    if "http" in text:
        await message.reply("Скачиваю... ⏳")
        try:
            download_video(text)
            await message.answer_document(open("video.mp4", "rb"))
        except:
            await message.reply("Ошибка 😢")
    else:
        await message.reply("Кинь ссылку")

if name == 'main':
    executor.start_polling(dp, skip_updates=True)
