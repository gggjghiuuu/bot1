from random import randint
from telebot import TeleBot, types
import random

BOTAPI = '8310952722:AAFru9IGpWJOjygWUNxdQBCoYBVRfUAHwtA'

bot = TeleBot(BOTAPI)

reply_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
button1 = types.KeyboardButton("Случайное число")
reply_kb.add(button1)


@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id,
                     "🌟 Добро пожаловать в учебного бота! 🌟\n"
                     "Я умею повторять за тобой слова и выполнять команды.\n"
                     "📖 Для списка команд используй /help",
                     reply_markup=reply_kb)

@bot.message_handler(commands=['help'])
def help(m):
    bot.send_message(m.chat.id,
                     "Я умею повторять сообщения 🤖\n"
                     "Команды:\n"
                     "📋 /help - справка\n"
                     "📋 /start - пуск\n"
                     "📋 /info - информация о боте\n"
                     "📋 /random - создание случайного числа от 0 до 100\n",
                     reply_markup=reply_kb)


@bot.message_handler(commands=['info'])
def info(m):
    bot.send_message(m.chat.id, "🤖 Я учебный бот. Я умею эхо и команды", reply_markup=reply_kb)


@bot.message_handler(commands=['random'])
def random_cmd(m):
    random_number = randint(1, 100)
    bot.send_message(m.chat.id, f"🎲 Случайное число: {random_number}", reply_markup=reply_kb)

@bot.message_handler(commands=['doc'])
def cmdDoc(m):
    with open("test-pdf.pdf", "rb") as f:
        bot.send_document(m.chat.id, f)
@bot.message_handler(commands=['serg'])
def sendSerg(m):
    with open("image.png", "rb") as photo:
        bot.send_document(m.chat.id, photo)
@bot.message_handler(func=lambda message: message.text == "Случайное число")
def random_button(m):
    random_number = randint(1, 100)
    bot.send_message(m.chat.id, f"🎲 Случайное число: {random_number}", reply_markup=reply_kb)




def repeat(m):

    if m.text.startswith('/'):
        return


    if m.text == "Арсений":
        bot.send_message(m.chat.id, "Ты чо тут делаешь. Тебе сюда нельзя")
    elif m.text == 'AlexB':
        bot.send_message(m.chat.id, "Дядя Богдан ждёт")

    elif m.text != "Случайное число":
        bot.send_message(m.chat.id, m.text)



bot.infinity_polling(skip_pending=True)