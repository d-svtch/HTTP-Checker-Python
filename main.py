import requests

import time
import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "5644056150:AAHlW3abaYK5W3LlBAEFc2VoAQ27841qzjQ"
url = 'https://zabbix.medvedev-it.ru/zabbix.php?action=dashboard.view'

listner = False

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    await message.reply(f'Чо умею:\n/start - вызов меню (вот этого самого) \n/status - запросить статус в ручную \n/listner_switch - устанавливает или отключает уведомления со статусами')

    while listner == True :
        await asyncio.sleep(30*1*1)
        await bot.send_message(user_id, 'Авто-Статус: ' + str(requests.get(url)))

@dp.message_handler(commands=['listner_switch'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    global listner
    if flag == False:
        flag = True
        await bot.send_message(user_id, 'Авто-уведомления каждые 30 секунд - вкл')
        while flag == True:
            await asyncio.sleep(30 * 1 * 1)
            await bot.send_message(user_id, 'Статус: ' + str(requests.get(url)))
    elif flag == True:
        flag = False
        await bot.send_message(user_id, 'АТПИСКА')

async def listner (id):
    user_id = id
    global listner

    if flag == False:
        flag = True
        await bot.send_message(user_id, 'Авто-уведомления каждые 30 секунд - вкл')
        while flag == True:
            await asyncio.sleep(30 * 1 * 1)
            await bot.send_message(user_id, 'Статус: ' + str(requests.get(url)))

    elif flag == True:
        flag = False
        await bot.send_message(user_id, 'АТПИСКА')

@dp.message_handler(commands=['status'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    #logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await bot.send_message(user_id, 'Статус: ' + str(requests.get(url)))

executor.start_polling(dp)