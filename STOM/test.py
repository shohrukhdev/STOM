# import telebot
#
# bot = telebot.TeleBot("1390309702:AAEDv79F-RG23_k3hS9fodHUek9S81c5bTk")
#
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
# 	print(message.from_user)
#
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
#
#
# bot.infinity_polling()

