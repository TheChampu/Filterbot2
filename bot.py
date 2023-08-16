import logging
from datetime import datetime
import asyncio
from config import *
from pyrogram import *

# Initialize logging
FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"),
              logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S",
)
LOGGER = logging.getLogger(__name__)

# Initialize clients
YaaraOP = Client(name="user", session_string=SESSION)
dbot = Client("testbot", api_id=API_ID,
              api_hash=API_HASH,
              bot_token=BOT_TOKEN)

class Bot(Client):
    def __init__(self):
        super().__init__(
            "bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"})
        self.user = YaaraOP  # Store User client as an attribute

    async def start(self):
        try:
            await super().start()
            await self.user.start()  # Start the User client
            LOGGER.info("Bot Started ⚡")
        except Exception as e:
            LOGGER.exception("Error while starting bot: %s", str(e))

    async def stop(self, *args):
        try:
            await super().stop()
            await self.user.stop()  # Stop the User client
            LOGGER.info("Bot Stopped")
        except Exception as e:
            LOGGER.exception("Error while stopping bot: %s", str(e))

User = Bot().user