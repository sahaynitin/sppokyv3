from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Alpha = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("WhatsApp", url="https://chat.whatsapp.com/FOALYW6PMitLo9jntxEGqi")],
        [InlineKeyboardButton("Telegram", url="https://t.me/telegrm_music9")],
        [InlineKeyboardButton("Youtube", url="https://youtube.com/channel/UC6ZgCl_f6YPxAsrzWhApPow")],
        [InlineKeyboardButton("SourceCode", url="https://github.com/HansakaBro/Spooky")]

    ])
    thumbnail_url = "https://telegra.ph/file/8d6150fac7f5e1341b02a.jpg"
    await message.reply_photo(thumbnail_url, caption=f"**Hi <b>{message.from_user.first_name}**</b>\n\n<br>__ð I Can Download YT Videos For You ð__</br>\n\n<b>`Instructions for use..`</b>\nâ¢ **âType /help to get instructins.**\n \nâââââ â **Lets Play** â âââââ\n ", reply_markup=Alpha)
    raise StopPropagation
