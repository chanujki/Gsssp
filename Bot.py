from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

TOKEN = os.getenv("7547250445:AAFsCQoCQxhpUKz-dEM4VT_Meq4e6veELNM")

def start(update, context):
    update.message.reply_text("Bot is running ✔")

def reply_handler(update, context):
    text = update.message.text
    update.message.reply_text(f"You said: {text}")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_handler))

updater.start_polling()
updater.idle()
