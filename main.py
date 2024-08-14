import os
import telebot 
from dotenv import load_dotenv 

load_dotenv()

my_token = os.getenv('TOKEN')
reading_timeout = os.getenv('READ_TIMEOUT')
update_time = os.getenv('UPDATE_AFTER_TIMEOUT')

bot = telebot.TeleBot(my_token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! نردانلم. لطفا پیام خود را بگذارید!")


bot.infinity_polling()