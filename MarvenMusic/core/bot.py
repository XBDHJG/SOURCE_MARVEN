from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen
import config
from ..logging import LOGGER


class Marven(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="MarvenMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )
    bot = Client(
    "mo",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    devail = "XB_DV"
    await bot.send_message(zombie, "**تم تشغيل ال صانع عزيزي المطور ،**")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور💎.")
    await idle()
