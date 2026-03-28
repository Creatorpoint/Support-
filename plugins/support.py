from pyrogram import Client, filters
from config import ADMINS

support_map = {}

@Client.on_callback_query(filters.regex("support"))
async def support_btn(client, query):
    await query.message.reply("✉️ Send your message, admin will reply.")

@Client.on_message(filters.private & ~filters.command("start"))
async def user_msg(client, message):
    for admin in ADMINS:
        sent = await message.copy(admin)
        support_map[sent.id] = message.from_user.id

@Client.on_message(filters.reply & filters.user(ADMINS))
async def admin_reply(client, message):
    if message.reply_to_message.id in support_map:
        user = support_map[message.reply_to_message.id]
        await message.copy(user)
