import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8230458260:AAEeVWX0lxf3gR1YKpN_LRdl5gXil3w8A_4"
CHANNEL_ID = "@mmmesh1"

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    if update.message.photo:
        await context.bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=update.message.photo[-1].file_id,
            caption=update.message.caption
        )
    elif update.message.text:
        await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=update.message.text
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()
