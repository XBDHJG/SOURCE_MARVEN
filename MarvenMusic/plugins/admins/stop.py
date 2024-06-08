from pyrogram import filters
from pyrogram.types import Message

from MarvenMusic import app
from MarvenMusic.core.call import Marven
from MarvenMusic.utils.database import set_loop
from MarvenMusic.utils.decorators import AdminRightsCheck
from MarvenMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"]) & ~BANNED_USERS)
@app.on_message(filters.command(["انها","ايقاف","انهاء"],"") & ~BANNED_USERS, group=666)

@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Marven.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
