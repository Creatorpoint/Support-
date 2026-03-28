from pyrogram import Client, filters
from config import ADMINS
from database import get_users

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def broadcast(client, message):
    if not message.reply_to_message:
        return await message.reply("Reply to message")

    users = await get_users()
    sent = 0

    for user in users:
        try:
            await message.reply_to_message.copy(user)
            sent += 1
        except:
            pass

    await message.reply(f"✅ Sent to {sent}")
