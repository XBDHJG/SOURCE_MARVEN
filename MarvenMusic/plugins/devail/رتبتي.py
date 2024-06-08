import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from MarvenMusic import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus




@app.on_message(
    command(["رتبتي"])
    & filters.group
)
async def rotba(client, message):
    dev = (OWNER_ID)
    ze = (5651614955)
    async def rotba(client, message):
    dev = (OWNER_ID)
    ze2 = (6403627774)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if int(message.from_user.id) == ze:
       rotba= "مّمٌَـبـ ـࢪمـج السوࢪس"
       if int(message.from_user.id) == ze2:
       rotba= "مطور السورس"
    elif message.from_user.id in dev:
        rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمــــن"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــــألك"
    else:
         rotba = "عضــو جميل"
    await message.reply_text(f"رتبتك في هذه المجموعه \nهــي ← «{rotba}»")