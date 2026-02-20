import os
import random
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8344105309:AAFs_r2ItZOp2lTAp4KtVxInOEldm_JUR-g"

# --- Telegram bot logic ---

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    if update.message.from_user and update.message.from_user.id == context.bot.id:
        return

    text = (update.message.text or "").strip().lower()
    if not text:
        return

    if text.endswith("где?"):
        answer = random.choice(["я в инканто", "я в новом белграде"])
        await update.message.reply_text(answer)
        return

    if text.endswith("внизу?"):
        answer = random.choice(["я в инканто", "я в новом белграде"])
        await update.message.reply_text(answer)
        return

    if text.endswith("?"):
        await update.message.reply_text("это вопрос")
        return

    if text.endswith("."):
        await update.message.reply_text("это не вопрос")
        return

    if text.endswith("!"):
        await update.message.reply_text("не ори")

def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle_message))
    app.run_polling()

# --- Fake web server for Render ---

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running"

if name == "__main__":
    # Запускаем бота в отдельном потоке
    threading.Thread(target=run_bot).start()

    # Запускаем веб-сервер (Render требует порт)
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)
