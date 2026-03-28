from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import add_user
from config import FORCE_CHANNEL

async def joined(client, user_id):
    try:
        await client.get_chat_member(FORCE_CHANNEL, user_id)
        return True
    except:
        return False

@Client.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id

    if not await joined(client, user_id):
        return await message.reply(
            "🔒 Please join our channel first",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Join Channel", url=f"https://t.me/{FORCE_CHANNEL}")]
            ])
        )

    await add_user(user_id)

    await message.reply(
        "👋 Welcome to Support Bot",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📞 Contact Support", callback_data="support")],
            [InlineKeyboardButton("📢 Updates", url=f"https://t.me/{FORCE_CHANNEL}")]
        ])
    )
