from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Just send me the YouTube video link dude and see magic"
    await message.reply_text(helptxt)
