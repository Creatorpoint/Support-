from pyrogram import Client, filters
from config import ADMINS
from database import get_users, ban_user

@Client.on_message(filters.command("stats") & filters.user(ADMINS))
async def stats(client, message):
    users = await get_users()
    await message.reply(f"👥 Total Users: {len(users)}")

@Client.on_message(filters.command("ban") & filters.user(ADMINS))
async def ban(client, message):
    user_id = int(message.text.split()[1])
    await ban_user(user_id)
    await message.reply("🚫 User Banned")
