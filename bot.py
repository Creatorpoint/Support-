from pyrogram import Client
from config import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler

app = Client(
    "support_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

# Optional cron job
scheduler = AsyncIOScheduler()

async def auto_msg():
    pass  # keep empty or use later

scheduler.start()

app.run()
