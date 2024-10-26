from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome! Use /embed <url> to generate an embed code.")

def embed(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 0:
        update.message.reply_text("Please provide a URL.")
        return

    url = context.args[0]
    embed_code = f'<iframe src="{url}" width="600" height="400"></iframe>'
    update.message.reply_text(f"Here is your embed code:\n{embed_code}")

def main() -> None:
    TOKEN = os.getenv("7609207287:AAHNsu8KgFmicSN0aPIRcJe0DaeVeluV3hk")
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("embed", embed))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
