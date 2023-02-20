from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


admincommands = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="admin panel")
        ],
        
    ],
    resize_keyboard=True
)

adminusers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="users"),
        ],
        [
            KeyboardButton(text="reklama"),
        ],
        [
            KeyboardButton(text="back")
        ],
    ],
    resize_keyboard=True
)