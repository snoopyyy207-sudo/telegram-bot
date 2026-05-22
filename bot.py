from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8688671404:AAG__A8l8lU0dACFXNULcpLo9m8klUi4Rps"

ADMIN_ID = 8692377434

approved_users = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id

    if user_id not in approved_users:
        await update.message.reply_text(
            "❌ Akses ditolak.\n\n"
            "Hubungi admin untuk membeli akses bot."
        )
        return

    await update.message.reply_text(
        "✅ Selamat datang member VIP."
    )

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != ADMIN_ID:
        return

    try:
        user_id = int(context.args[0])
        approved_users.add(user_id)

        await update.message.reply_text(
            f"✅ User {user_id} berhasil ditambahkan."
        )

    except:
        await update.message.reply_text(
            "Contoh:\n/add 123456789"
        )

async def listusers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != ADMIN_ID:
        return

    text = "\n".join(str(x) for x in approved_users)

    if not text:
        text = "Belum ada user."

    await update.message.reply_text(text)

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != ADMIN_ID:
        return

    text = " ".join(context.args)

    for user_id in approved_users:
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text=text
            )
        except:
            pass

    await update.message.reply_text(
        "✅ Broadcast terkirim."
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("list", listusers))
app.add_handler(CommandHandler("broadcast", broadcast))

print("VIP Bot Running...")
app.run_polling()