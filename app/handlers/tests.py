from pyrogram.types import Message
from pyrogram.types.messages_and_media.message import Str

from .main import start


async def test_start(bot, send_message, tg_user):
    message = Message(text=Str("/start"), id=1, from_user=tg_user)

    await start(bot, message)
    assert send_message.called

    user_id, text = send_message.call_args.args
    assert user_id == tg_user.id
    assert text == "Hello world"
