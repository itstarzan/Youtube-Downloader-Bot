from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Just send me a YouTube video link 🔗 and see magic"
    await message.reply_text(helptxt)
