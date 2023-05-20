import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# Set your bot token here
TELEGRAM_BOT_TOKEN = "6276398338:AAGmAh2_g8gMc-JS-Lhmif2GVhPzEARpwYQ"
# Set your admin user ID here
ADMIN_USER_ID = 6270279846

logging.basicConfig(level=logging.INFO)

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f"Hello, {user.first_name}! Welcome to the chat bot.")

def chat(update: Update, context: CallbackContext) -> None:
    message = update.message.text
    user_id = update.message.from_user.id

    # Reply to the user's message
    update.message.reply_text(f"You said: {message}")

    # Forward the message to the admin
    context.bot.send_message(chat_id=ADMIN_USER_ID, text=f"Message from {user_id}: {message}")

def ban(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_USER_ID:
        return

    user_id = int(context.args[0])
    context.bot.send_message(chat_id=user_id, text="You have been banned by the admin.")
    context.bot.send_message(chat_id=ADMIN_USER_ID, text=f"User {user_id} has been banned.")

def broadcast(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_USER_ID:
        return

    message = " ".join(context.args)
    # Replace the following list with the IDs of all users you want to send the message to
    user_ids = [123456789, 987654321]

    for user_id in user_ids:
        context.bot.send_message(chat_id=user_id, text=message)

def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))
    dispatcher.add_handler(CommandHandler("ban", ban))
    dispatcher.add_handler(CommandHandler("broadcast", broadcast))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
