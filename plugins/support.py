from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMINS

tickets = {}
user_ticket = {}

# 📞 Support Menu
@Client.on_callback_query(filters.regex("support_menu"))
async def support_menu(client, query):
    await query.message.edit_text(
        "📞 Support Center",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Open Ticket", callback_data="open_ticket")],
            [InlineKeyboardButton("⬅️ Back", callback_data="home")]
        ])
    )

# ➕ Open Ticket
@Client.on_callback_query(filters.regex("open_ticket"))
async def open_ticket(client, query):
    user_id = query.from_user.id

    if user_id in user_ticket:
        return await query.answer("❌ Ticket already open!", show_alert=True)

    user_ticket[user_id] = True

    await query.message.edit_text(
        "✉️ Send your issue now...",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("❌ Cancel", callback_data="close_ticket")]
        ])
    )

# 📩 User Message
@Client.on_message(filters.private & ~filters.command("start"))
async def handle_msg(client, message):
    user_id = message.from_user.id

    if user_id not in user_ticket:
        return

    for admin in ADMINS:
        msg = await message.copy(admin)
        tickets[msg.id] = user_id

# 🔁 Admin Reply
@Client.on_message(filters.reply & filters.user(ADMINS))
async def reply_user(client, message):
    if message.reply_to_message.id in tickets:
        user = tickets[message.reply_to_message.id]
        await message.copy(user)

# ❌ Close Ticket
@Client.on_callback_query(filters.regex("close_ticket"))
async def close_ticket(client, query):
    user_id = query.from_user.id
    user_ticket.pop(user_id, None)

    await query.message.edit_text(
        "✅ Ticket Closed",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🏠 Home", callback_data="home")]
        ])
    )
