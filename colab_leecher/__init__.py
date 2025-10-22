# copyright 2023 © Xron Trix | https://github.com/Xrontrix10

import logging, json
from uvloop import install
from pyrogram.client import Client
import asyncio
import os

# ---- Fix: ensure a running event loop before Pyrogram Client ----
# Disable uvloop because it's not yet compatible with Python 3.12 in Colab
os.environ["PYROGRAM_DISABLE_UVLOOP"] = "1"

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())
# -----------------------------------------------------------------

from pyrogram import Client


# Read the dictionary from the txt file
with open("/content/Telegram-Leecher/credentials.json", "r") as file:
    credentials = json.loads(file.read())

API_ID = credentials["API_ID"]
API_HASH = credentials["API_HASH"]
BOT_TOKEN = credentials["BOT_TOKEN"]
OWNER = credentials["USER_ID"]
DUMP_ID = credentials["DUMP_ID"]


logging.basicConfig(level=logging.INFO)

install()

colab_bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
