import asyncio
from pyrogram import Client, filters

import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    print("✅ START RECEIVED")
    await message.reply_text("🔥 Bot is finally working!")

@app.on_message()
async def echo(client, message):
    print("📩 MSG:", message.text)

app.run()
