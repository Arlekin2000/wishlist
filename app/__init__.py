from pyrogram import Client


class Bot(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


token = "5454227880:AAGf824-F5uiWL1kXEWiTlpuDYblIWFeZ5I"
api_id = 28276544
api_hash = "ad1ab2763f72c7c2f7bac547f2207d96"

bot = Bot("bot_name", bot_token=token, api_id=api_id, api_hash=api_hash, plugins=dict(root="app/handlers"))
