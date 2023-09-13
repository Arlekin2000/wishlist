from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("start", ["/"]))
async def start(client, message: Message):
    await client.send_message(message.from_user.id, "Hello world")
