from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram import F
from services.favorites_storage import FavoritesStorage
from services.choice_storage import ChoiceStorage
from aiogram.utils.keyboard import InlineKeyboardBuilder
from services.choice_storage import ChoiceStorage


router = Router()

# инициализируем хранилище (файл рядом с bot.py: storage/favorites.json)
storage = FavoritesStorage("storage/favorites.json")
choice_storage = ChoiceStorage("storage/choice.json")

# ---- Добавить в избранное ----
# Использование: /addfav <city>
@router.message(Command("addfav"))
async def cmd_add_fav(message: Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        return await message.reply("Нужно написать название города: /addfav Санкт-Петербург")

    city = parts[1].strip()
    # опционально можно проверить существование через mal_client.anime_exists
    await storage.add(message.from_user.id, city)
    await message.reply(f"Город {city} добавлен в избранное.")

# ---- Список избранного ----
@router.message(Command("favs"))
async def cmd_list_fav(message: Message):
    favs = await storage.list(message.from_user.id)
    if not favs:
        return await message.reply("Пока нет избранного 🙁")
    text = "Ваше избранное:\n" + "\n".join(f"- {a}" for a in favs)
    # кнопки для выбора каждого:
    kb = InlineKeyboardBuilder()
    for fav in favs:
        kb.button(text=f"Выбрать {fav}", callback_data=f"change_city_{fav}")
    kb.adjust(1)
    await message.reply(text, reply_markup=kb.as_markup())

# Выбрать по кнопке
@router.callback_query(lambda c: c.data.startswith("change_city_"))
async def cmd_change_city(query: CallbackQuery):
    city = query.data.split("_", 2)[2]
    await choice_storage.choice(query.from_user.id, city)
    await query.answer(f"Город {city} выбран.", show_alert=False)

# ---- Удалить из избранного командой ----
@router.message(Command("delfav"))
async def cmd_remove_fav(message: Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        return await message.reply("Нужно название города: /delfav Москва")
    city = parts[1].strip()
    await storage.remove(message.from_user.id, city)
    await message.reply(f"❌ Город {city} удален из избранного.")



