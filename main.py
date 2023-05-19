# main.py
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from handlers import start, help_command, uwu_balance, gift_uwu, admin_send_uwu, chat, support

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace this with your own bot token
BOT_TOKEN = "6276398338:AAGmAh2_g8gMc-JS-Lhmif2GVhPzEARpwYQ"
ADMIN_USER_ID = 6270279846  # Replace with your admin user ID

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("balance", uwu_balance))
    dp.add_handler(CommandHandler("gift", gift_uwu))
    dp.add_handler(CommandHandler("send", admin_send_uwu))
    dp.add_handler(CommandHandler("chat", chat))
    dp.add_handler(CommandHandler("support", support))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
