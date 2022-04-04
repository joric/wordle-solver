import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from uuid import uuid4
import solver

def start(update, context):
    update.effective_message.reply_text("""Hi! I solve wordle.
• https://www.nytimes.com/games/wordle
• https://wordle.belousov.one
Examples:
/solve (a)bout f(l)[a](s)(h) [s][h][a]l[l]
/solve -about f-l=a-s-h =s=h=al=l
"""
    )

def echo(update, context):
    update.effective_message.reply_text(update.effective_message.text)

def solve(update, context):
    update.effective_message.reply_text(' '.join(solver.solve(*context.args)) or "¯\_(ツ)_/¯")

if __name__ == "__main__":
    TOKEN = os.environ.get('TELEGRAM_TOKEN','12345:abcde')
    URL = os.environ.get('HEROKU_URL','https://appname.herokuapp.com')
    PORT = os.environ.get('PORT', 80)

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('solve', solve))

    dp.add_handler(MessageHandler((Filters.text | Filters.update) & ~Filters.command, echo))

    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN, webhook_url=f"{URL}/{TOKEN}")
    updater.idle()
