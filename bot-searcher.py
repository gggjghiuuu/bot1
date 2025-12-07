import requests
from telebot import TeleBot, types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import Test2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BOTAPI = '8021201752:AAEA_mGILUMOItvUU2sGRMdDpvte11XohvA'

bot = TeleBot(BOTAPI)

# Создаем клавиатуру
reply_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
button1 = types.KeyboardButton("Начать")
button2 = types.KeyboardButton("Искать")
reply_kb.add(button1, button2)


@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id,
                     "🌟 Добро пожаловать в поискового бота! 🌟\n"
                     "Я умею искать цены на любой сайт по продаже электроники в интернете.\n"
                     "📖 Для поиска нажмите кнопку 'Искать' или напишите /search",
                     reply_markup=reply_kb)


@bot.message_handler(commands=['search'])
def search(m):
    bot.send_message(m.chat.id, "🔍 Введи название товара, у которого хочешь узнать цену:")


@bot.message_handler(func=lambda message: message.text == "Начать")
def handle_start_button(m):
    start(m)


@bot.message_handler(func=lambda message: message.text == "Искать")
def handle_search_button(m):
    search(m)


@bot.message_handler(content_types=['text'])
def text(m):
    # Проверяем, не являются ли сообщения командами или кнопками
    if m.text in ["Начать"]:
        start(m)
    elif m.text in ["Искать"]:
        search(m)
    else:
        # Отправляем сообщение о начале поиска
        search_msg = bot.send_message(m.chat.id, "🔎 *Поиск товаров...* Пожалуйста, подождите ⏳",
                                      parse_mode='Markdown')

        try:
            # Выполняем поиск
            result = Test2.dns_search_uc(m.text)

            if not result:
                bot.edit_message_text("❌ *Товары не найдены*\n\nПопробуйте изменить запрос и повторить поиск.",
                                      m.chat.id, search_msg.message_id, parse_mode='Markdown')
                return

            # Форматируем красивое сообщение с результатами
            message_text = f"🎯 *Результаты поиска по запросу:* `{m.text}`\n\n"

            for i, (title, price, url) in enumerate(result, 1):
                # Обрезаем длинные названия
                short_title = title[:80] + "..." if len(title) > 80 else title

                message_text += f"**{i}. {short_title}**\n"
                message_text += f"💰 *Цена:* `{price}`\n"
                message_text += f"🔗 [Ссылка на товар]({url})\n\n"

            # Добавляем итоговую информацию
            message_text += f"📊 *Найдено товаров:* {len(result)}"

            # Отправляем отформатированное сообщение
            bot.edit_message_text(message_text, m.chat.id, search_msg.message_id,
                                  parse_mode='Markdown', disable_web_page_preview=True)

        except Exception as e:
            # Обработка ошибок
            error_msg = f"❌ *Произошла ошибка при поиске*\n\nОшибка: `{str(e)}`\n\nПопробуйте позже или измените запрос."
            bot.edit_message_text(error_msg, m.chat.id, search_msg.message_id,
                                  parse_mode='Markdown')


bot.infinity_polling(skip_pending=True)