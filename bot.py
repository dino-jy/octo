import telegram 


from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import redis
import logging
import telegram 


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Telegram bot token 
BOT_TOKEN = '6276398338:AAGmAh2_g8gMc-JS-Lhmif2GVhPzEARpwYQ'

# Redis host and port 
REDIS_HOST = 'redis-16860.c16.us-east-1-3.ec2.cloud.redislabs.com'
REDIS_PORT = 16860

# Database number for bot 
DB_NUM = 0 

# Create the EventHandler and pass it your bot's token.
updater = Updater(BOT_TOKEN)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Create Redis connection 
redis_conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=DB_NUM)

# Utility function to get user details from database
def get_user(user_id):
    return redis_conn.hgetall(user_id)

# Utility function to save user details to database
def save_user(user_id, username, balance):
    redis_conn.hmset(user_id, {'username': username, 'balance': balance})

# Start command 
def start(update, context):
    chat_id = update.message.chat_id
    username = update.message.from_user['username']
    
    # Check if user exists in database
    user = get_user(chat_id)
    
    # If user does not exist, add them
    if not user: 
        balance = 0  # Set default balance to 0
        save_user(chat_id, username, balance)
        
    # Send welcome message
    message = """Welcome {}! 
I'm a Telegram bot for managing in-bot payments and subscriptions.
You can send me /buy, /gift or /chat commands to use the bot.
Your current balance is {}""".format(username, balance)
    context.bot.send_message(chat_id=chat_id, text=message)

# Buy command  
def buy(update, context):
    ...

# Gift command
def gift(update, context): 
    ...  
    
# Chat command 
def chat(update, context):
    ...
    
# Error handler 
def error(update, context):
   ...
   
# Add handlers 
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('buy', buy))
dispatcher.add_handler(CommandHandler('gift', gift))
dispatcher.add_handler(CommandHandler('chat', chat)) 
dispatcher.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT, 
# SIGTERM or SIGABRT
updater.idle()
