from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from app.parsers.steampay import steampay
from app.parsers.gaben_store import gaben_store


@Client.on_message(filters.command("start", ["/"]))
async def start(client, message: Message):
    keyboard = [[InlineKeyboardButton(f"steampay")]]
    await client.send_message(message.from_user.id, "Hello world", reply_markup=keyboard)


@Client.on_message(filters.text)
async def get_game_name(client: Client, message: Message):
    for i in steampay(message.text):
        game = f"Название: {i['name']}\n"
        keyboard = [[InlineKeyboardButton(f"steampay {i['price']}", url=i['link'])]]
        link = InlineKeyboardMarkup(keyboard)
        await client.send_message(message.from_user.id, game, reply_markup=link)
    for i in gaben_store(message.text):
        game = f"Название: {i['name']}\n"
        keyboard = [[InlineKeyboardButton(f"gabestore {i['price']}", url=i['link'])]]
        link = InlineKeyboardMarkup(keyboard)
        await client.send_message(message.from_user.id, game, reply_markup=link)
