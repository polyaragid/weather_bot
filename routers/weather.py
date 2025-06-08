from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import F
from config.settings_weather import weather_config
from services.api_client import WeatherClient
from services.choice_storage import ChoiceStorage
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime

router = Router()

choice_storage = ChoiceStorage("storage/choice.json")
mal_client = WeatherClient(weather_config.api_key_weather)


# Использование: /city <city>
@router.message(Command("city"))
async def cmd_choose_city(message: Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        return await message.reply("Нужно написать название города: /city Санкт-Петербург")

    city = parts[1].strip()
    await choice_storage.choice(message.from_user.id, city)
    await message.reply(f"Город {city} выбран.")


# Использование: /wheather
@router.message(Command("weather"))
async def cmd_weather(message: Message):
    city = await choice_storage.get_city(message.from_user.id)
    if city == "":
        await message.reply("Город не выбран.\n Выберите его с помощью /city\n Пример: /city Москва")
        return 
    response = await mal_client.get_weather(city)
    if response['cod'] == 200:
        return await message.reply(f"Погода для {response['name']}\nТемпература: {round(float(response['main']['temp']) -273, 2)}\nСкорость ветра: {response['wind']['speed']} м/с")
    else:
        return await message.reply(f"Произошла ошибка.\n Код {response['cod']}\n сообщение от апи: {response['message']}")
    
    
        
    
    
