import html
import random
import EmikoRobot.modules.kelvinstring.py as kelvinstring
from EmikoRobot import dispatcher
from telegram import ParseMode, Update, Bot
from EmikoRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


def kevin(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(kelvinstring.KELVIN))
   
KEVIN_HANDLER = DisableAbleCommandHandler("kevin", kevin, run_async=True)

dispatcher.add_handler(KEVIN_HANDLER)
