import asyncio
import telegram
import codecs
import os


TOKEN = os.environ.get("BOT_TOKEN")
chat_id = '-1002171838106'

bot = telegram.Bot(token=TOKEN)

async def send_message(text, chat_id):
    async with bot:
        await bot.sendMessage(text=text, chat_id=chat_id, parse_mode="HTML")

async def send_photo(photo, chat_id):
    async with bot:
        await bot.send_photo(photo=photo, chat_id=chat_id)

def send_msg(csv):
    with codecs.open(csv, encoding='utf-8') as file:
        content = file.readlines()
        for line in content[1:]:
            data = line.strip().split(",")
            title = data[0] if data[0] else ""
            subtitle = data[1] if data[1] else ""
            link = data[2] if data[2] else ""
            link2 = data[3] if data[3] else ""
            link3 = data[4] if data[4] else ""
            image = data[5] if data[5] else ""
            text = f"<b>{title}</b>\n\n{subtitle}\n\n{link}\n\n{link2}\n\n{link3}"
            if image:
                asyncio.run(send_photo(photo=image, chat_id=chat_id))
            asyncio.run(send_message(text=text, chat_id=chat_id))
