import logging 
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Token 
TOKEN = '6276398338:AAGmAh2_g8gMc-JS-Lhmif2GVhPzEARpwYQ'

# Database to store user info 
db = {}

# Admin info 
ADMINS = [6270279846]  

# Currency name
CURRENCY = 'uwu' 

# Subscription plans
plans = {
    'daily': {
        'price': 5,
        'period': 1 
    },
    'weekly': {
        'price': 25,
        'period': 7
    },
    'monthly': {
        'price': 100,
        'period': 30
    }
}

# Initialize bot  
updater = Updater(TOKEN)
bot = updater.bot
dispatcher = updater.dispatcher

# Welcome message  
def start(bot, update): 
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    name = update.message.from_user.first_name
    db[chat_id] = {
        'user_id': user_id,
        'name': name,
        'bal': 0,
        'sub': None 
    }
    text = f'Hello {name}! Welcome to the {bot.name} bot. Type /help to know more.'
    bot.send_message(chat_id, text)

# Help message
def help(bot, update):
   ...  

# Fortune teller
def fortune(bot, update):
   ... 

# Admin features  
def ban(bot, update, args): 
   ...   

# Chat 
def chat(bot, update):
   ...  

# Subscription plans  
def subscribe(bot, update): 
   ...

# Send uwu 
def send(bot, update, args):
   ...  

# Profile  
def profile(bot, update):
   ...   

# Error handler 
def error(bot, update):
   ...

# Add handlers  
dispatcher.add_handler(CommandHandler('start', start))  
dispatcher.add_handler(CommandHandler('help', help))      
dispatcher.add_handler(CommandHandler('fortune', fortune)) 
dispatcher.add_handler(CommandHandler('ban', ban, pass_args=True))    
dispatcher.add_handler(MessageHandler(Filters.text, chat))
dispatcher.add_handler(CommandHandler('subscribe', subscribe)) 
dispatcher.add_handler(CommandHandler('send', send, pass_args=True))  
dispatcher.add_handler(CommandHandler('profile', profile))
dispatcher.add_error_handler(error)  

# Run the bot  
updater.start_polling()
updater.idle()
