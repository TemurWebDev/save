from aiogram import types
from loader import dp,bot,db
from aiogram.dispatcher.filters import Text
from handlers.users.instasaveapi import instasave
from keyboards.inline.inlinekey import til
from data.config import ADMINS


@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    chat_id = message.from_user.id
    user = db.select_user(chat_id=chat_id)
    try:
        url = message.text

        if len(url) == 63:
            shorted_url = url[31:len(url) - 21]
        elif len(url) == 60:
            shorted_url = url[28:len(url) - 21]
        elif len(url) == 61:
            shorted_url = url[29:len(url) - 21]
        elif len(url) == 71:
            shorted_url = url[31:len(url) - 29]

        if user[4] == None:
            await message.reply(f"🇺🇿 Tilni tanlang\n🇺🇸 Select a language\n🇷🇺 Выберите язык", reply_markup=til)
        elif user[4] == 'uz':
            t = await message.reply('yuklanmoqda...')
        elif user[4] == 'en':
            t = await message.reply('loading...')
        elif user[4] == 'ru':
            t = await message.reply('загрузка...')
        #print(shorted_url)
        data = instasave(shortcode=shorted_url)
        await message.answer_video(video=data)
        await bot.send_message(chat_id=ADMINS[0],text=f"{message.from_user.first_name} ga video yuborildi..")

    except Exception as e:
        pass
        #print(e)
        if user[4] == None:
            await message.reply(f"🇺🇿 Tilni tanlang\n🇺🇸 Select a language\n🇷🇺 Выберите язык", reply_markup=til)
        elif user[4] == 'uz':
            await message.reply('video topilmadi')
        elif user[4] == 'en':
            await message.reply('video not found')
        elif user[4] == 'ru':
            await message.reply('видео не найдено')
    
    await t.delete()