from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8688671404:AAG__A8l8lU0dACFXNULcpLo9m8klUi4Rps"

users = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    users.add(update.effective_chat.id)
    await update.message.reply_text("✅ Bot aktif dan kamu sudah masuk list.")

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)

    for user_id in users:
        try:
            await context.bot.send_message(chat_id=user_id, text=text)
        except:
            pass

    await update.message.reply_text("✅ Broadcast selesai")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("broadcast", broadcast))

print("Bot jalan...")
app.run_polling()