import telebot
from cfg import TOKEN
from bot_func import del_abv_elem

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, del_abv_elem(message.text))


bot.infinity_polling()

