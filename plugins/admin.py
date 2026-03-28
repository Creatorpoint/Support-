from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMINS
from database import get_users

@Client.on_callback_query(filters.regex("admin_menu"))
async def admin_menu(client, query):
    if query.from_user.id not in ADMINS:
        return

    await query.message.edit_text(
        "⚙️ Admin Panel",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📊 Stats", callback_data="stats")],
            [InlineKeyboardButton("📢 Broadcast", callback_data="broadcast")],
            [InlineKeyboardButton("⬅️ Back", callback_data="home")]
        ])
    )

@Client.on_callback_query(filters.regex("stats"))
async def stats(client, query):
    users = await get_users()
    await query.answer(f"👥 Users: {len(users)}", show_alert=True)
