import random

from aiogram import Dispatcher
from aiogram.types import Message
from aiogram import types
from aiogram.utils.markdown import hcode
from aiogram.dispatcher.filters import CommandStart
from tgbot.keyboards.reply import start_keyboard
from tgbot.states.subjects import LizaLove


async def user_start(message: Message):
    full_name = message.from_user.full_name
    text = [
        f"Привет, {full_name}👋",
        "Ниже ты можешь выбрать интересующий тебя раздел!"
    ]
    await message.answer("\n".join(text), reply_markup=start_keyboard)


async def send_advice(message: Message):
    text = [
        "Your advice for today:",
        hcode("Don't eat chips!!!"),
        "Cheers, @voha_shvarc"
    ]
    await message.answer("\n".join(text))


async def send_lovely_cat(message: Message):
    text = [
        "Приветики, какие планы на эту пятницу?)"
    ]
    sticker_id = "CAACAgIAAxkBAAOaYauUwAhI5FZ9pTckkmPMXgJgX5cAAikAAzx0phJOfQovnNCEdyIE"
    await message.answer_sticker(sticker_id)
    await message.answer("\n".join(text))
    await LizaLove.redirect_liza.set()


async def redirect_to_vova(message: Message, state):
    text = [
        "Я просто бездушная машина",
        "Напиши лучше Вове, он скучает🥺👉👈"
    ]
    await message.answer("\n".join(text))
    await state.finish()


async def send_for_timur(message: Message):
    text = [
        "Приветики"
    ]
    sticker_id = "CAACAgIAAxkBAAOkYauVT14GpKXWIcqvg44LNWW16dsAAt0HAAL1K6waSbZvpMQ5BEYiBA"
    await message.answer("\n".join(text), reply_markup=start_keyboard)
    await message.answer_sticker(sticker_id)




async def send_random_sticker_from_set(message: Message):
    bot = message.bot
    sticker_set_name = message.sticker.set_name
    sticker_set = await bot.get_sticker_set(sticker_set_name)
    sticker_to_send = random.choice(sticker_set.stickers)
    await message.answer_sticker(sticker_to_send.file_id)


def register_user(dp: Dispatcher):
    dp.register_message_handler(send_for_timur, CommandStart("for_timur"), is_private=True)
    dp.register_message_handler(send_lovely_cat, CommandStart("for_liza"), is_private=True)
    dp.register_message_handler(user_start, commands=["start"], is_private=True)
    dp.register_message_handler(send_advice, commands=["advice"], is_private=True)
    dp.register_message_handler(send_random_sticker_from_set, content_types=types.ContentType.STICKER, is_private=True)
    dp.register_message_handler(redirect_to_vova, state=LizaLove.redirect_liza)
