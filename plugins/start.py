from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel✿", url="https://t.me/botcompany1")],
        [InlineKeyboardButton("Group✇", url="https://t.me/botcopagroup")],
        [InlineKeyboardButton("Join This😇", url="https://t.me/songparadise1")],
        [InlineKeyboardButton("Owner🍁", url="https://t.me/GarfieldXofficial")]
        
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
