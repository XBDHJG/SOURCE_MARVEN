import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from MarvenMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MarvenMusic.core.call import Marven
from MarvenMusic.utils.database import get_assistant

@app.on_message(filters.video_chat_started)
async def stcall(client: Client, message: Message): 
      Startt = "↯︙تم تشغيل ↫ ⦗ المحادثة المرئية ⦘"
      await message.reply_text(Startt)

@app.on_message(filters.video_chat_ended)
async def encall(client: Client, message: Message): 
      Enddd = "↯︙تم ايقاف ↫ ⦗ المحادثة المرئية ⦘"
      await message.reply_text(Enddd)

@app.on_message(filters.video_chat_members_invited)
async def mevegaa(client: Client, message: Message): 
           text = f"↯︙قام الشخص ↫ ⦗ {message.from_user.mention} ⦘"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"\n↯︙بدعوة شخص الى المحادثة المرئية ↫ ⦗ {user.first_name} ⦘"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass