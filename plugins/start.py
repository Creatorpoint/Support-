from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import FORCE_CHANNEL, ADMINS

# ---------------- JOIN CHECK ----------------
async def joined(client, user_id):
    try:
        await client.get_chat_member(FORCE_CHANNEL, user_id)
        return True
    except:
        return False

# ---------------- HOME MENU ----------------
def home_menu(user_id):
    buttons = [
        [InlineKeyboardButton("📞 Support", callback_data="support")],
        [InlineKeyboardButton("📢 Updates", url=f"https://t.me/{FORCE_CHANNEL.replace('@','')}")]
    ]

    if user_id in ADMINS:
        buttons.append([InlineKeyboardButton("⚙️ Admin Panel", callback_data="admin")])

    return InlineKeyboardMarkup(buttons)

# ---------------- START COMMAND ----------------
@Client.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id

    # Force Join Check
    if FORCE_CHANNEL:
        if not await joined(client, user_id):
            return await message.reply(
                "🔒 Please Join Channel First",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Join Channel", url=f"https://t.me/{FORCE_CHANNEL.replace('@','')}")]
                ])
            )

    await message.reply(
        "🏠 Welcome to Support Bot 🚀",
        reply_markup=home_menu(user_id)
    )

# ---------------- SUPPORT BUTTON ----------------
@Client.on_callback_query(filters.regex("support"))
async def support(client, query):
    await query.message.edit_text(
        "📞 Send your message, admin will reply soon."
    )

# ---------------- ADMIN PANEL ----------------
@Client.on_callback_query(filters.regex("admin"))
async def admin_panel(client, query):
    if query.from_user.id not in ADMINS:
        return await query.answer("❌ Not allowed", show_alert=True)

    await query.message.edit_text("⚙️ Admin Panel Coming Soon...")
