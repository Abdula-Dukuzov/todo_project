from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/tasks")],
        [KeyboardButton(text="/add_task")],
    ],
    resize_keyboard=True
)
