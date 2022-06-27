from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from keyboards.default.user_info_button import info_button

from loader import dp


@dp.message_handler(Command('start'))
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n")
    await message.answer('Telefoningiz va mazilingizni yuboring',reply_markup=info_button)
