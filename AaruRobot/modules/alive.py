import random
from pyrogram import __version__ as pyrover
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from AaruRobot import OWNER_USERNAME, SUPPORT_CHAT, dispatcher
from AaruRobot.events import register
from AaruRobot import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/704c748282e91d831f127.jpg",
    "https://telegra.ph/file/b89143d3480604740fdff.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ 🦇Vค𝔪pıre 🦇 ✘ ʀᴏʙᴏᴛ​**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [⏤͟͟͞͞x𝐃🥀| 𓆩 LEGENDX 𓆪 |∘𖣘︎⃞⃟🔥°](https://t.me/ll_OFFICIAL_LEGENDBOY_ll)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", f"https://t.me/II_VAMPIRE_II_II_MUSIC_II_BOT?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", f"https://t.me/SPARTANBOT_XD"),
        ]
    ]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)
  
  ##AARU ALIVE MOD
