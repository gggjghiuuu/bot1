
from openai import OpenAI
import telebot

TELEGRAM_TOKEN = "8310952722:AAFru9IGpWJOjygWUNxdQBCoYBVRfUAHwtA"


bot = telebot.TeleBot(TELEGRAM_TOKEN)


client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key="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"
)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот с нейросетью. Напиши мне что-нибудь")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:

        completion = client.chat.completions.create(
            model="moonshotai/Kimi-K2-Thinking:novita",
            messages=[
                {
                    "role": "user",
                    "content": message.text
                }
            ],
        )


        bot_reply = completion.choices[0].message.content


        bot.send_message(message.chat.id, bot_reply)

    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {str(e)}")



print("Бот запущен...")
bot.polling(none_stop=True)