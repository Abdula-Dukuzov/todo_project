import os
from aiogram import types
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import TextInput
from aiogram.fsm.state import State, StatesGroup
from api import create_task
from datetime import datetime


class AddTaskSG(StatesGroup):
    title = State()
    due_date = State()


async def save_title(message: types.Message, widget, dialog_manager: DialogManager, text: str):
    dialog_manager.dialog_data["title"] = text
    # Перейти к следующему состоянию
    await dialog_manager.next()


async def save_due_date(message: types.Message, widget, dialog_manager: DialogManager, text: str):
    token = os.getenv("API_TOKEN")

    # Попробуем распарсить разные форматы даты
    parsed_date = None
    for fmt in ("%Y.%m.%d %H:%M", "%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d %H:%M:%S"):
        try:
            parsed_date = datetime.strptime(text, fmt)
            break
        except ValueError:
            continue

    if not parsed_date:
        await message.answer("Неверный формат даты. Используйте YYYY-MM-DD HH:MM:SS или YYYY.MM.DD HH:MM.")
        return

    # Преобразуем обратно в строку в нужном формате
    formatted_date = parsed_date.isoformat()

    data = {
        "title": dialog_manager.dialog_data["title"],
        "due_date": formatted_date,  # только это, без 'user'
    }

    try:
        create_task(token, data)
        await message.answer("Задача создана")
    except Exception as e:
        await message.answer(f"Ошибка при создании задачи: {e}")

    await dialog_manager.done()


add_task_dialog = Dialog(
    Window(
        Const("Введите название задачи"),
        TextInput(id="title", on_success=save_title),
        state=AddTaskSG.title,
    ),
    Window(
        Const("Введите due_date (YYYY-MM-DD HH:MM:SS или YYYY.MM.DD HH:MM)"),
        TextInput(id="due_date", on_success=save_due_date),
        state=AddTaskSG.due_date,
    ),
)
