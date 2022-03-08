from pyrogram import Client, Filters

@Client.on_message(Filters.command(["help"]))

async def start(client, message):

    helptxt = f"⚙ඔබට downlod කිරීමට අවශ්‍ය Youtube ලින්කුව send කරන්න.   ⚙Playlist downlod කිරීමට නොහැක."

    await message.reply_text(helptxt)
