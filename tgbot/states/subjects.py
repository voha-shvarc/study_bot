from aiogram.dispatcher.filters.state import StatesGroup, State


class Subjects(StatesGroup):
    subject_choose = State()
    info_choose = State()


class LizaLove(StatesGroup):
    redirect_liza = State()
