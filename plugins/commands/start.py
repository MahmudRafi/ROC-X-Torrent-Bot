from pyrogram import Client, filters
from pyrogram.types import Message

from config import START_MESSAGE


@Client.on_message(filters.command("start"))
async def start_message(c: Client, m: Message):
     welcomed = f"\nHi! l am ROC-X TORRENT BOT.\nI Will Help You To Find Your Items From The Torrent Sites.\nAll You Have To Do Is Just Send Me What You Want To Search For And I Will Find That For You. Don't Spam Me By Sending Continuous Messages.\n\n⚠️Pornographic contents are strictly prohibited and we will leads to ban without any warning !⚠️"
    await m.reply_text(welcomed, START_MESSAGE, reply_to_message_id=m.message_id)
