from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from AaruRobot import pbot as client


Aaru = "https://telegra.ph/file/b571926f287c281f4d5cd.jpg"

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Ayra,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [🦇Vค𝔪pıre 🦇 ✘ ʀᴏʙᴏᴛ-🇮🇳](t.me/ll_OFFICIAL_LEGENDBOY_ll)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [⏤͟͟͞͞x𝐃🥀| 𓆩 LEGENDX𓆪 |∘𖣘︎⃞⃟🔥](tg://user?id=2004027195)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**🦇Vค𝔪pıre 🦇 ✘ ʀᴏʙᴏᴛ sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴅᴇᴠᴇʟᴏᴘᴇʀ •", url="tg://user?id=2004027195"), 
                    InlineKeyboardButton(
                        "• sᴏᴜʀᴄᴇ •", url="https://github.com/LEGEND-LX")
                ]
            ]
        )
    )

__mod_name__ = "Rᴇᴩᴏ"
