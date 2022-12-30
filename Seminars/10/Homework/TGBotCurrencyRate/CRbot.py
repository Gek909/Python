import telebot
from cfg import TOKEN
from model import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['USD'])
def send_welcome(message):
    currency_name = "USD_RUB"
    cur_rate = get_currency_rate(currency_name)
    bot.send_message(message.chat.id, f'Валютная пара {currency_name}:\n\
{cur_rate}')

@bot.message_handler(commands=['EUR'])
def send_welcome(message):
    currency_name = "EUR_RUB"
    cur_rate = get_currency_rate(currency_name)
    bot.send_message(message.chat.id, f'Валютная пара {currency_name}:\n\
{cur_rate}')

@bot.message_handler(commands=['CAD'])
def send_welcome(message):
    currency_name = "CAD_RUB"
    cur_rate = get_currency_rate(currency_name)
    bot.send_message(message.chat.id, f'Валютная пара {currency_name}:\n\
{cur_rate}')

@bot.message_handler(commands=['CHF'])
def send_welcome(message):
    currency_name = "CHF_RUB"
    cur_rate = get_currency_rate(currency_name)
    bot.send_message(message.chat.id, f'Валютная пара {currency_name}:\n\
{cur_rate}')

@bot.message_handler(commands=['GBP'])
def send_welcome(message):
    currency_name = "GBP_RUB"
    cur_rate = get_currency_rate(currency_name)
    bot.send_message(message.chat.id, f'Валютная пара {currency_name}:\n\
{cur_rate}')

@bot.message_handler(commands=['JPY'])
def send_welcome(message):
    currency_name = "JPY_RUB"
    cur_rate = get_currency_rate(currency_name)
    bot.send_message(message.chat.id, f'Валютная пара {currency_name}:\n\
{cur_rate}')

@bot.message_handler(commands=['CNY'])
def send_welcome(message):
    currency_name = "CNY_RUB"
    cur_rate = get_currency_rate(currency_name)
    bot.send_message(message.chat.id, f'Валютная пара {currency_name}:\n\
{cur_rate}')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.send_message(message.chat.id, "Данный бот отображает актуальный биржевой курс основных валют по отношению к рублю. \n\
Список доступных валют:\n\
/USD - Доллар США \n\
/EUR - Евро \n\
/CAD - Канадский доллар \n\
/CHF - Швейцарский франк \n\
/GBP - Британский фунт \n\
/JPY - Японская йена \n\
/CNY - Китайский юань")

bot.infinity_polling()