import telebot
from telebot import types


bot = telebot.TeleBot("8310952722:AAFru9IGpWJOjygWUNxdQBCoYBVRfUAHwtA")

#m.chat.id
#m.form_user.id
#m.form_user.username
#m.form_user.first_name
#m.form_user.last_name
#m.form_user.language_code
#m.location
#m.sticker
#m.contact
@bot.message_handler(commands=['sticker'])
def cmdTest(m):
    bot.send_sticker(m.chat.id, "CAACAgIAAxkBAAEPheho4qei7lUKnIs6VyioUVc1I6XedQACGnIAAkXioEtdnfqb4whRNDYE")
bot.infinity_polling(skip_pending=True)
