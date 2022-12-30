import telebot
from cfg import TOKEN
from bot_func import *
import random

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Список доступных команд:\n\
/gamerules\n\
/startnewgame")

@bot.message_handler(commands=['gamerules'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Условие игры: На столе лежит 117 конфет. \
Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\
За один ход можно забрать не более чем 28 конфет. \
Все конфеты оппонента достаются сделавшему последний ход.")
    
game = False

@bot.message_handler(commands=['startnewgame'])
def send_welcome(message):
    global first_player
    global count
    global game
    first_player = find_first_player()
    count = 117
    game = True
    if first_player == "Игрок":
	    bot.send_message(message.chat.id, f"Игра началась, удачи! \n\
Первым ходит игрок \n\
Остаток конфет: {count}\n\
Сколько конфет возьмешь?")
    elif first_player == "Бот":
        choice = random.randint(1,28)
        count = count - choice
        bot.send_message(message.chat.id, f"Игра началась, удачи! \n\
Первым ходит бот")
        bot.send_message(message.chat.id, f"Бот взял {choice} конфет(ы) \n\
Остаток конфет: {count} \n\
Сколько конфет возьмешь?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global count
    global first_player
    global game
    if game == True:
        try:
            if int(message.text) > 0 and int(message.text) < 29:
                count = count - int(message.text)
                if count <= 28:
                    bot.send_message(message.chat.id, f"Бот забрал последние конфеты! ({count}) \n\
Победа бота :( \n\
Для начала новой игры используйте команду: /startnewgame")
                    count = 117
                    first_player = find_first_player()
                    game = False
                else:
                    bot.send_message(message.chat.id, f"Остаток конфет: {count}")
                    choice = random.randint(1,28)
                    count = count - choice
                    bot.send_message(message.chat.id, f"Бот взял {choice} конфет(ы)")
                    if count <= 28:
                        bot.send_message(message.chat.id, f"Игрок забрал последние конфеты! ({count}) \n\
Победа игрока! \n\
Для начала новой игры используйте команду: /startnewgame")
                        count = 117
                        first_player = find_first_player()
                        game = False
                    else:
                        bot.send_message(message.chat.id, f"Остаток конфет: {count} \n\
Сколько конфет возьмешь?")
            else:
                bot.send_message(message.chat.id, "Можно взять от 1 до 28 конфет")
        except ValueError:
            bot.send_message(message.chat.id, "Неверный ввод. Введите цифрами количество конфет.")
    else:
        bot.send_message(message.chat.id, "Для отображения доступных команд введите /help")


bot.infinity_polling()

