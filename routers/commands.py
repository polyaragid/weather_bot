from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import logging
from keyboards.builders import keyboard


router = Router()

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я бот для работы с OpenWeatherMap\n"
                         "Введи /help для вывода списка доступных команд",
                         reply_markup=keyboard)

    logging.info(f"User {message.from_user.id} called /start")

@router.message(Command("help"))
async def start_command(message: Message):
    await message.answer(
        "Команды:\n"
        "/start - приветсвие\n"
        "/weather - погода\n"
        "/city <city> - выбрать город\n"
        "/favs - города в избранном\n"
        "/addfav <city> - добавить город в избранное\n"
        "/delfav <city> - удалить город из избранного\n"
        "/help- список команд\n"
        "/support- поддержка"
    )
