from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Универ"),
            KeyboardButton("Sloboda Studio")
        ]
    ],
    resize_keyboard=True
)

subjects_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Вышка")
        ],
        [
            KeyboardButton("ООП"),
            KeyboardButton("Англ"),
            KeyboardButton("ЭТ")
        ],
        [
            KeyboardButton("ТА"),
            KeyboardButton("БЖД"),
            KeyboardButton("Веб")
        ],
        [
            KeyboardButton("Вернуться"),
            KeyboardButton("Главное меню")
        ]
    ],
    resize_keyboard=True
)
info_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Преподователи"),
            KeyboardButton("Аудитории")
        ],
        [
            KeyboardButton("Текущее дз"),
            KeyboardButton("Прошлое дз")
        ],
        [
            KeyboardButton("Лекции"),
            KeyboardButton("Практики")
        ],
        [
            KeyboardButton("Вернуться"),
            KeyboardButton("Главное меню")
        ]
    ],
    resize_keyboard=True
)
