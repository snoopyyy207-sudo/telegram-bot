from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8688671404:AAG__A8l8lU0dACFXNULcpLo9m8klUi4Rps"

ADMIN_ID = 8692377434

approved_users = set()

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id

    if user_id not in approved_users:
        await update.message.reply_text(
            "❌ Akses ditolak.\n\n"
            "Ketik /sewa untuk membeli akses bot."
        )
        return

    await update.message.reply_text(
        "✅ Selamat datang member VIP."
    )

# MENU SEWA
async def sewa(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "📞 Hubungi Admin",
                url="https://t.me/mycaelish"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo="https://i.imgur.com/2yaf2wb.jpeg",
        caption=(
            "💎 SEWA BOT VIP 💎\n\n"
            "Harga : Rp10.000 / bulan\n\n"
            "Transfer ke QRIS di atas lalu kirim bukti transfer ke admin."
        ),
        reply_markup=reply_markup
    )

# ADD USER VIP
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_chat.id != ADMIN_ID:
        return

    try:
        user_id = int(context.args[0])

        approved_users.add(user_id)

        await update.message.reply_text(
            f"✅ User {user_id} berhasil ditambahkan ke VIP."
        )

    except:
        await update.message.reply_text(
            "Contoh:\n/add 123456789"
        )

# LIST USER
async def listusers(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_chat.id != ADMIN_ID:
        return

    text = "\n".join(str(x) for x in approved_users)

    if not text:
        text = "Belum ada user VIP."

    await update.message.reply_text(text)

# BROADCAST
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

# RUN BOT
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sewa", sewa))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("list", listusers))
app.add_handler(CommandHandler("broadcast", broadcast))

print("VIP BOT RUNNING...")
app.run_polling()