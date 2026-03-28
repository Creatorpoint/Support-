from pyrogram import Client
from config import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database import get_users
import asyncio

app = Client(
    "support_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

scheduler = AsyncIOScheduler()

# Example cron job
async def auto_msg():
    users = await get_users()
    for user in users:
        try:
            await app.send_message(user, "🔥 Hello from bot")
        except:
            pass

scheduler.add_job(auto_msg, "interval", hours=24)

# ✅ Correct startup
async def main():
    await app.start()
    scheduler.start()   # अब event loop चल रहा है ✅
    print("✅ BOT STARTED")
    await idle()

from pyrogram import idle

if __name__ == "__main__":
    asyncio.run(main())
