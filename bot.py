from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *

app = ApplicationBuilder().token("").build()
app.run_polling()
