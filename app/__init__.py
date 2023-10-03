import os
import uvloop

from pyrogram import Client
from modconfig import Config


class Bot(Client):
    def __init__(self, env=None, *args, **kwargs):
        env = env or os.environ.get("ENV", "develop")
        self.cfg = Config(f"app.config.{env}")
        self.ENV = env
        if os.path.exists("app/config/local.py") and not env == "tests":
            self.cfg.update_from_modules("app.config.local")

        super().__init__(
            self.cfg.BOT_NAME,
            bot_token=self.cfg.BOT_TOKEN,
            api_id=self.cfg.BOT_API_ID,
            api_hash=self.cfg.BOT_API_HASH,
            plugins=dict(root="app/handlers")
        )


uvloop.install()

bot = Bot()
