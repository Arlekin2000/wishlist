import asyncio

import json
from pathlib import Path
import pytest
from unittest import mock

from pyrogram.types.user_and_chats.user import User


class FakeRequestsResponse:
    def __init__(self, text):
        self.text = text


@pytest.fixture(scope='session')
def loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="session")
def bot():
    from app import bot
    bot.me = User(id=5454227880, is_self=True, is_bot=True, username="UN")
    bot.is_connected = True
    return bot


@pytest.fixture
def tg_user():
    return User(
        id=238322888,
        is_bot=False,
        is_self=False,
        first_name="Eugene",
        username="fake_user"
    )


@pytest.fixture
def send_message():
    async def response():
        return True
    with mock.patch("app.Bot.send_message") as mocked:
        mocked.return_value = response()
        yield mocked


@pytest.fixture
def response():
    def resp():
        return True

    with mock.patch("requests.get") as mocked:
        mocked.return_value = resp()
        yield mocked


@pytest.fixture()
def fixture():
    def load(name):
        with Path(__file__).parent.joinpath(f"fixtures/{name}").open() as source:
            # return json.load(source)
            return FakeRequestsResponse(source.read())

    return load
