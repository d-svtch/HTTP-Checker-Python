import requests

import time
import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "5644056150:AAHlW3abaYK5W3LlBAEFc2VoAQ27841qzjQ"
url = 'https://zabbix.medvedev-it.ru/zabbix.php?action=dashboard.view'

listner = False
warnings = False

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

def catcher():
    try:
        answer = requests.get(url)
        #bot.send_message(user_id, 'Статус: ' + str(requests.get(url)))
    except:
        answer = 'Пизда, оно упало!'
        #bot.send_message(user_id, 'Оно упало, пизда!')
    return answer

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    await message.reply(f'Чо умею:\n/start - вызов меню (вот этого самого) \n/status - запросить статус в ручную \n/warnings - Включкение и выключение автоуведомлений о пиздеце \n/listner_switch - устанавливает или отключает уведомления со статусами')

@dp.message_handler(commands=['listner_switch'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    global listner
    if listner == False:
        listner = True
        await bot.send_message(user_id, 'Авто-уведомления каждые 30 секунд - вкл')
        while listner == True:
            await asyncio.sleep(30 * 1 * 1)
            res = catcher()
            await bot.send_message(user_id, 'Статус: ' + str(res))
    elif listner == True:
        listner = False
        await bot.send_message(user_id, 'АТПИСКА')

@dp.message_handler(commands=['warnings'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    global warnings
    if warnings == False:
        warnings = True
        await bot.send_message(user_id, 'Авто-уведомления о проёбах - вкл')
        while warnings == True:
            await asyncio.sleep(60 * 1 * 1)
            res = catcher()
            await bot.send_message(user_id, 'Статус: ' + str(res))
    elif warnings == True:
        warnings = False
        await bot.send_message(user_id, 'Уведомления о проёбах - выкл')

@dp.message_handler(commands=['status'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    #logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    res = catcher()
    await bot.send_message(user_id, 'Статус: ' + str(res))


executor.start_polling(dp)