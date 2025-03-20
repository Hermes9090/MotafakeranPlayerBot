from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("کنترل") & filters.group)
async def show_controls(client, message):
    buttons = [
        [InlineKeyboardButton("▶️ پخش", callback_data="play"),
         InlineKeyboardButton("⏸️ توقف موقت", callback_data="pause")],
        [InlineKeyboardButton("⏹️ پایان", callback_data="stop"),
         InlineKeyboardButton("⏩ جلو +۱۰", callback_data="seek_10")],
        [InlineKeyboardButton("⏪ عقب -۱۰", callback_data="seek_-10")]
    ]
    await message.reply("کنترل‌های ربات:", reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query()
async def handle_buttons(client, callback_query):
    data = callback_query.data
    chat_id = callback_query.message.chat.id
    if data == "play":
        await client.send_message(chat_id, "/resume")
    elif data == "pause":
        await client.send_message(chat_id, "/pause")
    elif data == "stop":
        await client.send_message(chat_id, "/stop")
    elif data == "seek_10":
        await client.send_message(chat_id, "/seek 10")
    elif data == "seek_-10":
        await client.send_message(chat_id, "/seek -10")
    await callback_query.answer(f"در حال انجام: {data}")
