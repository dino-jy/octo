import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging 
import time

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Token and username 
bot_token = '6276398338:AAGmAh2_g8gMc-JS-Lhmif2GVhPzEARpwYQ'
bot_username = '@Blackhawk24_bot'

# List of banned users 
banned_users = [] 

# Dictionary of admin users
admins = {'6270279846':True, 'ADMIN_2_USER_ID':True}

# Start telegram bot
updater = Updater(token=bot_token, use_context=True)
dp = updater.dispatcher

# Welcome message 
def start(update, context):
    update.message.reply_text(
        'Hi! Welcome to the chat. I\'m a bot created by Anthropic to be helpful, harmless, and honest.'
    )

# Ban command 
def ban(update, context):
    if update.message.from_user.id in admins:
        user_id = update.message.reply_to_message.from_user.id
        banned_users.append(user_id)
        update.message.reply_text(f'Banned user {user_id}')
    else: 
        update.message.reply_text('You do not have permission to ban users.')

# Broadcast command     
def broadcast(update, context):
    if update.message.from_user.id in admins:
        msg = update.message.reply_to_message.text 
        for user_id in list(set(banned_users)):
            context.bot.send_message(chat_id=user_id, text=msg)
        update.message.reply_text(f'Message sent to {len(banned_users)} users.')
    else: 
        update.message.reply_text('You do not have permission to broadcast messages.')

# Error handler 
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Message handler 
def echo(update, context):
    if update.message.from_user.id not in banned_users: 
        update.message.reply_text(update.message.text)

# Add handlers 
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("ban", ban)) 
dp.add_handler(CommandHandler("broadcast", broadcast))
dp.add_error_handler(error)
dp.add_handler(MessageHandler(Filters.text, echo))

# Start the Bot  
updater.start_polling() 
updater.idle()
