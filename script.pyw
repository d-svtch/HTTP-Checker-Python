import requests

import time
import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types

TOKEN = "YOUR OT TOKEN"
url = 'YOUR URL'

listner = False
warnings = False

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

def catcher():
    try:
        answer = requests.get(url)
    except:
        answer = "!WARNING! \n Something goes wrong!"
    return answer

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    await message.reply(f"/start - to show this menu \n/status - requests status manualy \n/warnings - switch notifications if status != 200 \n/listner_switch - switch auto-notifications every hour")

@dp.message_handler(commands=['listner_switch'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    global listner
    if listner == False:
        listner = True
        await bot.send_message(user_id, "Auto-notifications every hour - ON")
        while listner == True:
            await asyncio.sleep(60 * 60 * 1)
            res = catcher()
            await bot.send_message(user_id, "Status: " + str(res))
    elif listner == True:
        listner = False
        await bot.send_message(user_id, "Auto-notifications every hour - OFF")

@dp.message_handler(commands=['warnings'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    global warnings
    if warnings == False:
        warnings = True
        await bot.send_message(user_id, "Notifications if status != 200 - ON")
        while warnings == True:
            await asyncio.sleep(60 * 1 * 1)
            res = str(catcher())
            if res != "<Response [200]>":
                await bot.send_message(user_id, "!WARNING! \nWrong status! \nStatus: " + str(res))
    elif warnings == True:
        warnings = False
        await bot.send_message(user_id, "Notifications if status != 200 - OFF")

@dp.message_handler(commands=['status'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    res = catcher()
    await bot.send_message(user_id, "Status: \n" + str(res))

executor.start_polling(dp)