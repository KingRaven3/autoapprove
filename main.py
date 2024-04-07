from pyrogram import Client , filters
from pyrogram.types import ChatJoinRequest
import os , time

bot = Client(
    "autoapprove",
    api_id=6,
    api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e",
    bot_token=os.environ['BOT_TOKEN']
)

@bot.on_chat_join_request(filters.channel)
def auto(_,m:ChatJoinRequest):
    chat_id = m.chat.id
    user_id = m.from_user.id
    time.sleep(3)
    bot.approve_chat_join_request(chat_id , user_id)
    print(f"APPROVED {user_id} in {chat_id}")


bot.run()
