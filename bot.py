import asyncio
from threading import Thread
from flask import Flask
from pyrogram import Client, filters, idle

import os

# -------- CONFIG --------
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# -------- FLASK --------
web = Flask(__name__)

@web.route("/")
def home():
    return "Bot Running ✅"

def run_web():
    web.run(host="0.0.0.0", port=10000)

# -------- BOT --------
app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    print("✅ START COMMAND RECEIVED")
    await message.reply_text("🔥 Finally Bot Working!")

@app.on_message()
async def all_msg(client, message):
    print("📩 MSG:", message.text)

# -------- MAIN --------
async def main():
    await app.start()
    print("🚀 BOT STARTED SUCCESSFULLY")
    await idle()

if __name__ == "__main__":
    Thread(target=run_web).start()
    asyncio.run(main())
