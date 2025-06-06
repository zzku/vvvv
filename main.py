from pyrogram import Client
from pytgcalls import PyTgCalls
import asyncio

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
userbot = Client("userbot", api_id=API_ID, api_hash=API_HASH)

async def main():
    await app.start()
    await userbot.start()
    call = PyTgCalls(userbot)
    await call.start()
    print("Bot and Userbot are running...")
    await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())