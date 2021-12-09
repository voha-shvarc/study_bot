from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.markdown import hbold

from tgbot.keyboards.reply import subjects_keyboard, info_keyboard, start_keyboard
from tgbot.states.subjects import Subjects

SUBJECTS = ['Вышка', 'Англ', 'ООП', 'Веб', 'БЖД', 'ТА', 'ЭТ']

state2keyboard = {
    "Subjects:info_choose": info_keyboard,
    "Subjects:subject_choose": subjects_keyboard
}


async def back_to_start_menu(message: types.Message, state: FSMContext = None):
    text = [
        "You came back to start menu😎"
    ]
    if state:
        await state.finish()

    await message.answer("\n".join(text), reply_markup=start_keyboard)


async def back_to_previous(message: types.Message, state: FSMContext = None):
    text = [
        "You came back to previous step😇"
    ]
    if state:
        message.bot.get("logger").info(f"{await state.get_state()}")
        await Subjects.previous()
    await message.answer("\n".join(text), reply_markup=subjects_keyboard)


async def choose_subject(message: types.Message):
    text = [
        "Выбери нужный предмет и поехали🤓"
    ]
    await message.answer("\n".join(text), reply_markup=subjects_keyboard)
    await Subjects.subject_choose.set()


async def choose_info(message: types.Message, state: FSMContext):
    chosen_subject = message.text
    if chosen_subject == "Вернуться":
        await back_to_previous(message, state)
        return
    elif chosen_subject == "Главное меню":
        await back_to_start_menu(message, state)
        return

    text = [
        "Отличный выбор!",
        "Теперь что именно ты хочешь узнать?🧐"
    ]
    await message.answer("\n".join(text), reply_markup=info_keyboard)

    await state.update_data(subject=chosen_subject)
    await Subjects.info_choose.set()


async def result(message: types.Message, state: FSMContext):
    chosen_subject = await state.get_data()
    chosen_info = message.text
    if chosen_info == "Вернуться":
        await back_to_previous(message, state)
        return
    elif chosen_info == "Главное меню":
        await back_to_start_menu(message, state)
        return

    text = [
        "Подитожим, ты хочешь:",
        f"Предмет - {hbold(chosen_subject.get('subject'))}, достать информацию - {hbold(chosen_info)}",
        "Обязательно поищу это для тебя🤖"
    ]
    await message.answer("\n".join(text), reply_markup=start_keyboard)

    await state.finish()


def register_subjects_info(dp: Dispatcher):
    dp.register_message_handler(choose_subject, Text(equals="Универ"))
    dp.register_message_handler(choose_info, state=Subjects.subject_choose)
    dp.register_message_handler(result, state=Subjects.info_choose)
