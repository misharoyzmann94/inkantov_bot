import os
import random
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8344105309:AAFs_r2ItZOp2lTAp4KtVxInOEldm_JUR-g"

# --- Telegram логика ---

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
    if random.random() < 0.5:   # 50% шанс ответа
        await update.message.reply_text("это вопрос")
    return

    if text.endswith("."):
    await update.message.reply_text("это не вопрос")
    return

    if text.endswith("!"):
    if random.random() < 0.5:   # 50% шанс ответа
        await update.message.reply_text("не ори")

# --- Flask сервер для Render ---

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Запускаем Flask в фоне
    threading.Thread(target=run_flask, daemon=True).start()

    # Бот запускаем в ГЛАВНОМ потоке
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle_message))
    print("BOT STARTED")
    app.run_polling()

