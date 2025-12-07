from telebot import TeleBot, types
from urllib.parse import quote_plus
BOTAPI = '8021201752:AAEA_mGILUMOItvUU2sGRMdDpvte11XohvA'
import random
import requests
bot = TeleBot(BOTAPI)

@bot.message_handler(commands=['image'])
def cmdImage(m):
    prompt = m.text.partition(' ')[2].strip()
    bot.send_message(m.chat.id, "Чёто делаю")
    seed = random.randint(0, 2_000_000_000)
    q = quote_plus(f"{prompt}, high quality, detailed, soft light")
    url = f"https://image.pollinations.ai/prompt/{q}?width=768&height=768&seed={seed}&n=1"
    res = requests.get(url, timeout=30, allow_redirects=True)
    bot.send_photo(m.chat.id, res.content)


bot.infinity_polling(skip_pending=True)
