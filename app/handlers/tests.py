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


async def test_get_game_name(bot, send_message, tg_user, response, fixture):
    message = Message(text=Str("mafia"), id=1, from_user=tg_user)

    # фикстура response перехватывает вызов метода get модуля requests (requests.get)
    # и не подменяет ответ на заранее заготовленную нами страницу html (которая загружается в фикстуре fixture)
    response.side_effect = [
        fixture("steampay_response"),
        fixture("gabe_store_response")
    ]

    async def tg_fake_response():
        """Fake response for pyrogram.Client.send_message method."""
        return True
    send_message.side_effect = [tg_fake_response() for _ in range(8)]

    await get_game_name(bot, message)

    assert send_message.called
    assert send_message.call_count == 7

    (user_id1, text1), params1 = send_message.call_args_list[0]
    button1 = params1['reply_markup'].inline_keyboard[0][0]
    assert user_id1 == tg_user.id
    assert text1 == 'Название: Mafia: Trilogy Экшены, Приключения\n'
    assert button1.text == 'steampay 2385 ₽'
    assert button1.url == 'https://steampay.com/game/mafia-trilogy'

    (user_id2, text2), params2 = send_message.call_args_list[1]
    button2 = params2['reply_markup'].inline_keyboard[0][0]
    assert user_id2 == tg_user.id
    assert text2 == 'Название: Mafia II: Definitive Edition Экшены, Приключения\n'
    assert button2.text == 'steampay 789 ₽'
    assert button2.url == 'https://steampay.com/game/mafia-ii-definitive-edition'

    # TODO: продолжить тест
    # запустить все тесты можно командой "pytest"
    # запустить один тест можно командой "pytest app/handlers/test.py::test_get_game_name"
