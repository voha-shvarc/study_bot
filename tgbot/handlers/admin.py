from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart


async def admin_start(message: Message):
    text = [
        "hello admin",
    ]
    await message.answer("\n".join(text))


async def cp_wanted(message: Message):
    text = [
        "You're not welcome here!",
        "Go away fucking nerd!",
        "Or write to @voha_shvarc"
    ]
    await message.answer("\n".join(text))


def register_admin(dp: Dispatcher):
    dp.register_message_handler(cp_wanted, CommandStart(deep_link="want"))
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)

