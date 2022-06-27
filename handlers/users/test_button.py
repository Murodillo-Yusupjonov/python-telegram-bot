from aiogram.dispatcher.filters import Command,Text
from aiogram.types import Message,ReplyKeyboardRemove
from keyboards.default.menukeybord import menu
from keyboards.default.python_lessons import python

from loader import dp

@dp.message_handler(Command('menu'))
async def menu_button(msg:Message):
    await msg.answer('kuslarni tanglang',reply_markup=menu)


@dp.message_handler(text='Telegram bot')
async def pythyon_button(msg: Message):
    await msg.answer('Telegram bot darslari:  https://www.youtube.com/watch?v=oRSa8NXWMXQ&list=PLwsopmzfbOn8x3CJKdQLtqDKhaF8n2r_7')

@dp.message_handler(text='Python')
async def menu_button(msg:Message):
    await msg.answer('darsliklar ro\'hati',reply_markup=python)

@dp.message_handler(text='Asosiy menu')
async def main(msg:Message):
    await msg.answer('kuslarni tanglang',reply_markup=menu)

@dp.message_handler(text='#00 dars')
async def back(msg:Message):
    await msg.answer('#00 dars https://www.youtube.com/watch?v=ZqFjXM8k-PY&list=PLwsopmzfbOn9Lw5D7a26THpBDgAma1Sus&index=1')




