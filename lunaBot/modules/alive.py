import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from lunaBot.events import register as MEMEK
from lunaBot import telethn as tbot

PHOTO = "https://telegra.ph/file/c43a142d8fbd4cd86aa74.mp4"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**Hoi Darling 🥲, I'm [Sofia🧚‍♀️](https://t.me/Sofia_op_bot)!** \n\n"
  LUNA += "🥀 **I'm Working Properly** \n\n"
  LUNA += "🥀 **My Master : [Miss-Vidhi🤍](https://t.me/Legend_Vidhi_Vrs)** \n\n"
  LUNA += f"🥀 **Telethon Version : {tlhver}** \n\n"
  LUNA += f"🥀 **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Help", "http://t.me/Sofia_op_bot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/SOFIASUPPORT")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  LUNA = "✅ **bot restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/SOFIASUPPORT")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
