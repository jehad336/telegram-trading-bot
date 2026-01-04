from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8230458260:AAEeVWX0lxf3gR1YKpN_LRdl5gXil3w8A_4"
CHANNEL_ID = "@mmmesh1"

async def forward_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        photo = update.message.photo[-1].file_id
        caption = update.message.caption
        await context.bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=photo,
            caption=caption
        )

    elif update.message.text:
        await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=update.message.text
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward_to_channel))
app.run_polling()
