from random import randint

import pandas
from telebot import TeleBot, types
import random
import threading
from datetime import datetime
import time

import Test2

BOTAPI = '8310952722:AAFru9IGpWJOjygWUNxdQBCoYBVRfUAHwtA'

bot = TeleBot(BOTAPI)



users = set()

days_of_week ={
    1:"Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье",
}

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_sticker(m.chat.id, "CAACAgIAAxkBAAEPwBdpEqiSxlRd_H20g8brjTsUU9nWFAACBQADwDZPE_lqX5qCa011NgQ")
    bot.send_message(m.chat.id,
                     "🌟 Добро пожаловать! 🌟\n"
                     "Я - Бот очень очень очень чела.\n"
                     "📖 Для списка команд используй /info")



@bot.message_handler(commands=['info'])
def info(m):
    kb1 = types.InlineKeyboardMarkup()
    kb2 = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("/notice", callback_data="notice")
    btn2 = types.InlineKeyboardButton("/unsub", callback_data="unsub")
    btn3 = types.InlineKeyboardButton("/image",callback_data="image")
    btn4 = types.InlineKeyboardButton("/parser", callback_data="parser")

    btn5 = types.KeyboardButton("/notice")
    btn6 = types.KeyboardButton("/unsub")
    btn7 = types.KeyboardButton("/image")
    btn8 = types.KeyboardButton("/parser")

    kb1.add(btn1, btn2, btn3, btn4)
    kb2.add(btn5, btn6, btn7, btn8)

    bot.send_message(m.chat.id, "Список команд😇", reply_markup=kb1)
    bot.send_message(m.chat.id, "/start - привествие\n"
                                "/info - меню бота\n"
                                "/notice - подписаться на уведомления\n"
                                "/unsub - отписаться от уведомлений\n"
                                "/image - создание изображений\n"
                                "/parser - подборка товаров с DNS", reply_markup=kb2)

@bot.message_handler(commands=["notice"])
def notice(m):
    users.add(m.chat.id)
    bot.send_message(m.chat.id, "Вы подписались на уведомления✅")

@bot.message_handler(commands=["unsub"])
def unsub(m):
    users.discard(m.chat.id)
    bot.send_message(m.chat.id, "Вы отписались от уведомления❌")
def setNotification(user):
    currentWeekDay = 3 # currentWeekDay = datetime.today.weekday() +1

    if currentWeekDay == 6 or currentWeekDay == 7:
        bot.send_message(user, "седня выходной")
    df = pandas.read_excel("shedule.xlsx")
    today_schedule = df[df['День'] == currentWeekDay]
    responce = f"Расписание на {days_of_week[currentWeekDay]}"
    for i in today_schedule:
        bot.send_message(user, i)
def check_time():
    while True:
        now = datetime.now()
        if now.hour == 20 and now.minute ==50:
            for user in list(users):
                print("Уведомления работают")
                setNotification(user)
            time.sleep(10)
        else:
            time.sleep(1)
@bot.message_handler(commands=['parser'])
def parser(m):
    prompt = m.text.partition(' ')[2].strip()
    result = Test2.dns_search_uc(prompt)
    bot.send_message(m.chat.id, result)

def notification():
    scheduler_thread = threading.Thread(target=check_time)
    scheduler_thread.daemon = True  # фоновый поток
    scheduler_thread.start()

if __name__ == "__main__":
    print("Бот запущен...")
    notification()              # Запуск фоновых уведомлений
    bot.polling(none_stop=True)    # Основной цикл бота









