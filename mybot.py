import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Replace YOUR_TOKEN with your Telegram bot's token
TOKEN = '6276398338:AAGmAh2_g8gMc-JS-Lhmif2GVhPzEARpwYQ'
bot = telegram.Bot(token=TOKEN)

# Replace ADMIN_CHAT_ID with your Telegram chat ID
ADMIN_CHAT_ID = '6270279846'

# Define the start command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi there! I'm a bot. How can I help you?")

# Define the echo message handler
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Define the ban command handler
def ban(update, context):
    user_id = int(context.args[0])
    context.bot.kick_chat_member(chat_id=update.effective_chat.id, user_id=user_id)
    context.bot.send_message(chat_id=update.effective_chat.id, text="User has been banned.")

# Define the broadcast command handler
def broadcast(update, context):
    if str(update.effective_chat.id) == ADMIN_CHAT_ID:
        message = ' '.join(context.args)
        for member in bot.get_chat_members_count(update.effective_chat.id):
            if member['user']['is_bot'] == False:
                context.bot.send_message(chat_id=member['user']['id'], text=message)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Broadcast message has been sent.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You are not authorized to use this command.")

# Define the message handler
def message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that. Please enter a valid command.")

# Define the error handler
def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ban", ban))
    dp.add_handler(CommandHandler("broadcast", broadcast))

    # Add message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message))

    # Add error handler
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
