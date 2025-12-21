import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram_dialog import setup_dialogs, DialogManager

from config import BOT_TOKEN
from keyboards import main_keyboard
from api import get_tasks
from dialogs.add_task import add_task_dialog, AddTaskSG


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        "Привет! Я ToDo бот",
        reply_markup=main_keyboard
    )


@dp.message(F.text == "/tasks")
async def list_tasks(message: Message):
    token = os.getenv("API_TOKEN")

    tasks = get_tasks(token)  # вызываем напрямую

    if isinstance(tasks, dict) and "error" in tasks:
        await message.answer(
            f"API ошибка:\n{tasks['error']}"
        )
        return

    if not tasks:
        await message.answer("📭 У вас нет задач")
        return

    print("TASKS FROM API:", tasks, type(tasks))

    text = ""
    for task in tasks:
        text += (
            f"{task['title']}\n"
            f"Категория: {task['category']['name'] if task['category'] else '-'}\n"
            f"Создано: {task['created_at']}\n\n"
        )

    await message.answer(text)


@dp.message(F.text == "/add_task")
async def add_task(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(AddTaskSG.title)


async def main():
    dp.include_router(add_task_dialog)
    setup_dialogs(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
