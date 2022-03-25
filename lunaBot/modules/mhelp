"""
tai = event.sender.first_name
  LUNA = "** ──「 Basic Guide 」── ** \n\n"
  LUNA += "• /play **(song title) — To Play the song you requested via YouTube** \n"
  LUNA += "• /search ** (song/video title) – To search for links on YouTube with details** \n"
  LUNA += "• /playlist - **show the list song in queue** \n"
  LUNA += "•/lyric - ** (song name) lyrics scrapper** \n\n"
  LUNA += "** ──「 Admin CMD 」── ** \n\n"
  LUNA += "• /pause - **To Pause Song playback** \n"
  LUNA += "• /resume - **To resume playback of the paused Song** \n"
  LUNA += "• /skip - **To Skip playback of the song to the next Song** \n"
  LUNA += "• /end - **To Stop Song playback** \n"
  LUNA += "• /control - **open the player settings panel** \n"
  LUNA += "• /reload - **To Refresh admin list** \n"
"""

import random
import re
import os
import requests

from telegram import (
    ChatPermissions,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
)
from typing import List
from telegram.ext import CallbackContext, run_async
from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from lunaBot.events import register as MEMEK
from lunaBot import telethn as tbot
from lunaBot.modules.disable import DisableAbleCommandHandler

#PHOTO = "https://telegra.ph/file/7c3c26e0ed938aec91209.jpg"

MEME_STICKER = [
    "CAACAgUAAx0CYt4kYwACKp5iPWIPs1bTz845pTA-QyuPogUnfgACdQQAAoTOcFUe8m3_76viiiME",
    "CAACAgUAAx0CYt4kYwACKp1iPWIOop1W3R64NdUMmc8xzl2FXQACNQQAAk84aVVNKEfsfquoOSME",
    "CAACAgUAAx0CYt4kYwACKpdiPWIHZsUMtqBZHgEsJ-Vk3aeygQACGgMAAgEEWVUnEJR1saZrIyME",
    "CAACAgUAAx0CYt4kYwACKpZiPWIGQs8dsfQjQnkNXC8LV8QhjwACJwUAArDGWFU7Xr2JJzFXpSME",
    "CAACAgUAAx0CYt4kYwACKpViPWIFZV0zqoVAJQrCOe9AHBedoQACZwUAAlg_WFWLiAi3FnLHXSME",
    "CAACAgUAAx0CYt4kYwACKpRiPWIBDC5iPUKxP4apeAwBJ0XHGwAC_wIAAhNHWFVp6A_D2GnrhCME",
    "CAACAgUAAx0CYt4kYwACKpNiPWH_BmPUHqiW4zlMC9Xt5ieaQwACYgMAAiVKWFWbkw0u4Eac_yME",
    "CAACAgIAAx0CYt4kYwACKrBiPWL7xiYUWcbfT_oVr5Vg-u7ZzwACeBUAAq6O4UlqYf9FNzvvzSME",
    "CAACAgIAAx0CYt4kYwACKq1iPWLr2mKktso1oAzvbJkglshBPAACsBQAAvgD6UlWlIfaVWuw6yME",
]

@run_async
def xnxx(update: Update, context: CallbackContext):
    #msg = update.effective_message
    pingpong = random.choice(LETS_GO_OYO)

    update.effective_message.reply_sticker(
        MEME_STICKER, reply_markup=InlineKeyboardMarkup(
                            [
                                {
                                    InlineKeyboardButton(
                                        text="ᴄʀᴇᴀᴛᴏʀ🧚‍♀️",
                                        url="tg://user?id=5072650671"),
                                }
                            ]
                        ),
        parse_mode=ParseMode.MARKDOWN,
    )

MEME_HANDLER = DisableAbleCommandHandler("dc", xnxx)


dispatcher.add_handler(MEME_HANDLER)

__command_list__ = ["dc"]

__handlers__ = [MEME_HANDLER]

__mod_name__ = "Xtra-Fun"

__help__ = """Extra Funn Command (only for fun)\n\n✨ /dc : Use nd see. \n\n More command soon keep patients!!"""


