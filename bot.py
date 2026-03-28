import asyncio
import logging
from threading import Thread
from flask import Flask

from pyrogram import Client, idle
from config import *

# ------------------ LOGGING ------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# ------------------ FLASK SERVER ------------------
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "✅ Bot is Running Successfully!"

def run_web():
    web_app.run(host="0.0.0.0", port=10000)

# ------------------ PYROGRAM BOT ------------------
app = Client(
    "support_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

# ------------------ MAIN FUNCTION ------------------
async def start_bot():
    try:
        await app.start()
        print("🚀 BOT STARTED SUCCESSFULLY")

        # Bot info print
        me = await app.get_me()
        print(f"🤖 Bot Name: {me.first_name}")
        print(f"🆔 Username: @{me.username}")

        await idle()

    except Exception as e:
        print(f"❌ BOT ERROR: {e}")

    finally:
        await app.stop()
        print("🛑 BOT STOPPED")

# ------------------ START EVERYTHING ------------------
if __name__ == "__main__":
    try:
        # Flask server start (background)
        Thread(target=run_web).start()

        # Bot start
        asyncio.run(start_bot())

    except Exception as e:
        print(f"🔥 FATAL ERROR: {e}")
