import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv 

load_dotenv()

my_token = os.getenv('TOKEN')
reading_timeout = os.getenv('READ_TIMEOUT')
update_time = os.getenv('UPDATE_AFTER_TIMEOUT')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # print(context.user_data)
    _text = "سلام! من نردانلم. لطفا پیام خود را بگذارید!"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=_text)

# async def receive_message(update: Update,  context: ContextTypes.DEFAULT_TYPE):
#     msg = update 

if __name__ == '__main__':
    application = ApplicationBuilder().token(my_token).read_timeout(read_timeout=reading_timeout).get_updates_read_timeout(get_updates_read_timeout=update_time).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()
