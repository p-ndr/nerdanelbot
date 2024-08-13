import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv 

load_dotenv()

my_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _text = "سلام! من نردانلم. لطفا پیام خود را بگذارید!"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=_text)

if __name__ == '__main__':
    application = ApplicationBuilder().token(my_token).read_timeout(15).get_updates_read_timeout(42).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()
