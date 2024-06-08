#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @SOURCE_MARVEN
#𝙳𝙴𝚅 DEVAIL : @XB_DV
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @D3M_MARVEN
#DRVAIL MarvenMusic تم التعديل بواسطة 🎸 ⋅
import asyncio
from asyncio import gather
import os
import time
import requests
from pyrogram import enums
from pyrogram import types
import aiohttp
from pyrogram.types import CallbackQuery
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from MarvenMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MarvenMusic import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait



##############################################################
##############################################################
          
     
@app.on_message(filters.command(["سورس","السورس","مصنع","صانع"], ""), group=221213)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d7f84f3abf21196ccd7e5.jpg",
        caption=f"""╭── • [⌯𝐃𝐞𝐕 𝐃𝐞𝐕𝐞𝐋⌯](https://t.me/XB_DV) • ──╮\n[⌯𝐃𝐞𝐕 𝐍𝐚𝐑𝐮𝐓𝐨⌯](https://t.me/GGCQU)\n[⌯𝐒𝐨𝐔𝐫𝐂𝐞 𝐌𝐚𝐑𝐯𝐞𝐍⌯](https://t.me/SOURCE_MARVEN)\n╰── • [⌯𝐃𝐞𝐕 𝐒𝐨𝐔𝐫𝐂𝐞⌯](https://t.me/DEV_MARVEN) • ──╯""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ 𝐃𝐞𝐕 𝐃𝐞𝐕𝐞𝐋 › ", url=f"https://t.me/XB_DV"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝐃𝐞𝐕 𝐍𝐚𝐑𝐮𝐓𝐨 ›", url=f"https://t.me/GGCQU"), 
                    InlineKeyboardButton(
                        "‹ 𝐒𝐨𝐔𝐫𝐂𝐞 𝐌𝐚𝐑𝐯𝐞𝐍 ›", url=f"https://t.me/SOURCE_MARVEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"https://t.me/{bot_username}?startgroup=True"),
            ]
        ]
         ),parse_mode=enums.ParseMode.MARKDOWN)



@app.on_message(filters.command(["مطور السورس","ناروتو"], ""), group=221212)
async def huhh(client: Client, message: Message):
    usr = await client.get_chat("FFPEX")
    name = usr.first_name
    photo = await client.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"الاسم:- {name}\nاليوزر : @{usr.username}\nالايدي `{usr.id}`\nالبايو : {usr.bio}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    
@app.on_message(filters.command(["مبرمج السورس","ديڤل"], ""), group=221212)
async def huhh(client: Client, message: Message):
    usr = await client.get_chat("XB_DV")
    name = usr.first_name
    photo = await client.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"الاسم:- {name}\nاليوزر : @{usr.username}\nالايدي `{usr.id}`\nالبايو : {usr.bio}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    
@app.on_message(filters.command(["اسمي","اسمي اي","قول اسمي"], ""), group=123222)
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""- اسمك » ⦗ {message.from_user.mention} ⦘ 💘 ⋅""") 


##############################################################
##############################################################
##############################################################
  


#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @SOURCE_MARVEN
#𝙳𝙴𝚅 DEVAIL : @XB_DV
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @D3M_MARVEN
#DRVAIL MarvenMusic تم التعديل بواسطة 🎸 ⋅
