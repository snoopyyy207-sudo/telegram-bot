import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)

# =========================================
# TOKEN BOT
# =========================================

TOKEN = "8688671404:AAG__A8l8lU0dACFXNULcpLo9m8klUi4Rps"

# =========================================
# ADMIN ID
# =========================================

ADMIN_ID = 8692377434

# =========================================
# DATABASE
# =========================================

approved_users = set{8692377434}
groups = set()

promo_text = None
promo_delay = 5
promo_type = "broadcast"
promo_status = False

# =========================================
# AUTO SAVE GROUP
# =========================================

async def savegroup(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat = update.effective_chat

    if chat.type in ["group", "supergroup"]:

        groups.add(chat.id)

        print(f"GROUP SAVED: {chat.id}")

# =========================================
# START
# =========================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_chat.id

    if user_id not in approved_users:

        await update.message.reply_text(
            "❌ Akses ditolak.\n\n"
            "Ketik /sewa untuk membeli akses."
        )

        return

    await update.message.reply_text(
        "✅ Selamat datang member VIP."
    )

# =========================================
# MENU SEWA
# =========================================

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
        photo="https://t.me/twinkaboo/3",
        caption=(
            "💎 SEWA BOT VIP 💎\n\n"
            "Harga : Rp4.000 / bulan\n\n"
            "Transfer ke QRIS di atas lalu kirim bukti transfer ke admin."
        ),
        reply_markup=reply_markup
    )

# =========================================
# ADD VIP USER
# =========================================

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

# =========================================
# LIST USER
# =========================================

async def listusers(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_chat.id != ADMIN_ID:
        return

    text = "\n".join(str(x) for x in approved_users)

    if not text:
        text = "Belum ada user VIP."

    await update.message.reply_text(text)

# =========================================
# SAVE PROMOSI
# =========================================

async def promosi(update: Update, context: ContextTypes.DEFAULT_TYPE):

    global promo_text
    global promo_delay
    global promo_type
    global promo_status

    if update.effective_chat.id != ADMIN_ID:
        return

    args = context.args

    if not args:
        return

    # =====================================
    # SAVE PROMOSI
    # =====================================

    if args[0] == "save":

        if update.message.reply_to_message:

            promo_text = update.message.reply_to_message.text

            await update.message.reply_text(
                "✅ Promosi berhasil disimpan."
            )

    # =====================================
    # DELAY
    # =====================================

    elif args[0] == "delay":

        promo_delay = int(args[1])

        await update.message.reply_text(
            f"✅ Delay diubah jadi {promo_delay} menit."
        )

    # =====================================
    # TYPE
    # =====================================

    elif args[0] == "type":

        promo_type = args[1]

        await update.message.reply_text(
            f"✅ Type promosi: {promo_type}"
        )

    # =====================================
    # ON
    # =====================================

    elif args[0] == "on":

        if promo_text is None:

            await update.message.reply_text(
                "❌ Belum ada promosi yang disimpan."
            )

            return

        promo_status = True

        await update.message.reply_text(
            "✅ Auto promosi diaktifkan."
        )

        while promo_status:

            sukses = 0

            for group_id in groups:

                try:

                    # ======================
                    # BROADCAST
                    # ======================

                    if promo_type == "broadcast":

                        await context.bot.send_message(
                            chat_id=group_id,
                            text=promo_text
                        )

                    sukses += 1

                except:
                    pass

            print(f"BERHASIL KIRIM KE {sukses} GROUP")

            await asyncio.sleep(
                promo_delay * 60
            )

    # =====================================
    # OFF
    # =====================================

    elif args[0] == "off":

        promo_status = False

        await update.message.reply_text(
            "⛔ Auto promosi dihentikan."
        )

# =========================================
# DELETE SAVE
# =========================================

async def delsave(update: Update, context: ContextTypes.DEFAULT_TYPE):

    global promo_text

    if update.effective_chat.id != ADMIN_ID:
        return

    promo_text = None

    await update.message.reply_text(
        "🗑 Promosi berhasil dihapus."
    )

# =========================================
# BROADCAST MANUAL
# =========================================

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_chat.id != ADMIN_ID:
        return

    text = " ".join(context.args)

    sukses = 0

    for group_id in groups:

        try:

            await context.bot.send_message(
                chat_id=group_id,
                text=text
            )

            sukses += 1

        except:
            pass

    await update.message.reply_text(
        f"✅ Broadcast terkirim ke {sukses} grup."
    )

# =========================================
# RUN BOT
# =========================================

app = ApplicationBuilder().token(TOKEN).build()

# =========================================
# HANDLER
# =========================================

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sewa", sewa))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("list", listusers))
app.add_handler(CommandHandler("promosi", promosi))
app.add_handler(CommandHandler("broadcast", broadcast))
app.add_handler(CommandHandler("delsave", delsave))

app.add_handler(
    MessageHandler(filters.ALL, savegroup)
)

# =========================================
# START BOT
# =========================================

print("VIP BOT RUNNING...")

app.run_polling()