import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8344105309:AAFs_r2ItZOp2lTAp4KtVxInOEldm_JUR-g"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Не отвечает сам себе
    if update.message.from_user.id == context.bot.id:
        return

    text = update.message.text.strip().lower()

    if text.endswith("где?"):
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

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.run_polling()