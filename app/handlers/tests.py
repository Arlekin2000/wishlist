from pyrogram.types import Message
from pyrogram.types.messages_and_media.message import Str

from .main import start, get_game_name


async def test_start(bot, send_message, tg_user):
    message = Message(text=Str("/start"), id=1, from_user=tg_user)

    await start(bot, message)
    assert send_message.called

    user_id, text = send_message.call_args.args
    assert user_id == tg_user.id
    assert text == "Hello world"

async def test_get_game_name(bot, send_message, tg_user):
    message = Message(text=Str("mafia"), id=1, from_user=tg_user)
    async def response():
        return True
    send_message.side_effect = [
        response(),
        response(),
        response(),
        response(),
        response(),
        response(),
        response(),
        response()
    ]
    await get_game_name(bot, message)
    assert send_message.called

    assert send_message.call_count == 8
    args = list(send_message.call_args_list)
    breakpoint()
    pass
