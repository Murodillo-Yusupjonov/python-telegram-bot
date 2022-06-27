from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

python = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='#00 dars'),
            KeyboardButton(text='#01 dars'),
            KeyboardButton(text='#02 dars'),
        ],

        [
            KeyboardButton(text='Ortag qaytish'),
            KeyboardButton(text='Asosiy menu'),
        ],

    ],
    resize_keyboard=True

)