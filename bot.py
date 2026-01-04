from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os

TOKEN = os.getenv("8230458260:AAEeVWX0lxf3gR1YKpN_LRdl5gXil3w8A_4")
CHANNEL_ID = os.getenv("@mmmesh1")
PORT = int(os.getenv("PORT", "8443"))  # Render يوفر PORT تلقائيًا

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        await context.bot.send_photo(chat_id=CHANNEL_ID,
                                     photo=update.message.photo[-1].file_id,
                                     caption=update.message.caption)
    elif update.message.text:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=update.message.text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))

# Webhook
URL = os.getenv("RENDER_EXTERNAL_URL")  # Render يعطيك هذا المتغير تلقائيًا
app.run_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN, webhook_url=f"{URL}/{TOKEN}")
