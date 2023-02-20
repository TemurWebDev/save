import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot
from keyboards.default.adminKey import adminusers,admincommands


@dp.message_handler(text="/start", user_id=ADMINS)
async def get_all_users(message: types.Message):

    #await message.answer('admin panel',reply_markup=admincommands)
    await bot.send_message(chat_id=ADMINS[0],text='Siz adminsiz',reply_markup=admincommands)




@dp.message_handler(text="admin panel", user_id=ADMINS)
async def get_all_users(message: types.Message):

    await message.answer('admin panel',reply_markup=adminusers)




@dp.message_handler(text="users", user_id=ADMINS)
async def get_all_users(message: types.Message):
    count = db.count_users()
    users = db.select_all_users()
    text = f"instabot || Foydalanuvchilar soni: {count[0]}\n\n"
    for user in users:
        text+= f"{user[0]}). || {user[2]} || @{user[3]}\n"
    await message.answer(text)


@dp.message_handler(text="back", user_id=ADMINS)
async def back_button(message: types.Message):

    await message.answer('Bosh menyu',reply_markup=admincommands)




@dp.message_handler(text="reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[1]
        await bot.send_message(chat_id=user_id, text="@pythonapiuz kanaliga obuna bo'ling!")
        await asyncio.sleep(0.05)

