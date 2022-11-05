import os

from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
token = str(os.environ.get('TOKEN'))

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(content_types=[types.ContentType.VIDEO_NOTE])
async def download_video(message: types.Message):
    print(f'Пришло видео от пользователя {message.from_user}')
    file_id = message.video_note.file_id
    # file = await bot.get_file(file_id) # Получить файл
    # await bot.download_file(file.file_path, f'{file_id}.mp4') # Загрузка файл
    await bot.send_video_note(message.from_id, file_id)

if __name__ == '__main__':
    executor.start_polling(dp)
