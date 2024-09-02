import asyncio
import telegram
import codecs

TOKEN = "7475058039:AAG6T4XJp8gLje-AeDpxnPuJeHg_AxknV80"
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
                links = f"{data[3]}\n\n{data[4]}\n\n{data[5]}\n\n{data[6]}"
                text = f"<b>{data[1]}</b>\n\n{data[2]}\n\n{links}"
                if data[6]:
                    asyncio.run(send_photo(photo=data[6], chat_id=chat_id))
                asyncio.run(send_message(text=text, chat_id=chat_id))


