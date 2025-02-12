import logging

import telegram, os
from telegram.ext import Dispatcher, MessageHandler, CommandHandler, Filters

from uuid import uuid4
import solver

def start(update, context):
    """Send a message when the command /start is issued."""
    update.effective_message.reply_text("""Hi! I solve wordle.
• https://www.nytimes.com/games/wordle
• https://wordle.belousov.one
[] means exact match, () means partial match (OR use = and - prefixes):
(a)bout f(l)[a](s)(h) [s][h][a]l[l] OR -about f-l=a-s-h =s=h=al=l
The best starting words are "salet", "trace", and "crate".
The bot is stateless, each input string should countain all tries.
"""
    )

def echo(update, context):
    #update.effective_message.reply_text(update.effective_message.text)
    update.effective_message.reply_text(' '.join(solver.solve(*update.effective_message.text.split())) or "¯\_(ツ)_/¯")

def solve(update, context):
    update.effective_message.reply_text(' '.join(solver.solve(*context.args)) or "¯\_(ツ)_/¯")

def get_dispatcher(bot):
    """Create and return dispatcher instances"""
    dispatcher = Dispatcher(bot, None, workers=0)

    dispatcher.add_handler(CommandHandler("start", start))
    #dispatcher.add_handler(CommandHandler("solve", solve))
    dispatcher.add_handler(MessageHandler((Filters.text | Filters.update) & ~Filters.command, echo))
    return dispatcher
