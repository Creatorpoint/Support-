from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import add_user
from config import FORCE_CHANNEL, ADMINS

# Force Join Check
async def joined(client, user_id):
    try:
        await client.get_chat_member(FORCE_CHANNEL, user_id)
        return True
    except:
        return False

# 🏠 Home Menu
def home_menu(user_id):
    buttons = [
        [InlineKeyboardButton("📞 Support", callback_data="support_menu")],
        [InlineKeyboardButton("📢 Updates", url=f"https://t.me/{FORCE_CHANNEL}")]
    ]

    if user_id in ADMINS:
        buttons.append([InlineKeyboardButton("⚙️ Admin Panel", callback_data="admin_menu")])

    return InlineKeyboardMarkup(buttons)

@Client.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id

    if not await joined(client, user_id):
        return await message.reply(
            "🔒 Join Channel First",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Join Channel", url=f"https://t.me/{FORCE_CHANNEL}")]
            ])
        )

    await add_user(user_id)

    await message.reply(
        "🏠 **Welcome to Support Bot Dashboard**",
        reply_markup=home_menu(user_id)
    )
