# =========================================
# MYCA | FH APP PREM 
# =========================================

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

TOKEN = "8688671404:AAG__A8l8lU0dACFXNULcpLo9m8klUi4Rps"

ADMIN = "@mycaelish"

# =========================================
# START
# =========================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
ㅤㅤ⠀( sun melts softly between the quiet sky. )
ㅤㅤ⠀small things, warm feelings —
ㅤㅤ⠀welcome to [ MYCA | FH APP PREM ] 89’s 🦴✨
ㅤㅤ⠀your safe place for premium apps with tiny prices.

Ketik /pricelist untuk melihat semua produk ✨
"""

    await update.message.reply_text(text)

# =========================================
# PRICELIST
# =========================================

async def pricelist(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
━━━━━━━━━━━━━━━
🎬 STREAMING APPS
━━━━━━━━━━━━━━━

/netflix
/disney
/viu
/iqiyi
/youtube
/bstation
/youku
/loklok

━━━━━━━━━━━━━━━
🎨 EDITING APPS
━━━━━━━━━━━━━━━

/capcut
/canva
/alightmotion
/picsart
/meitu
/wink
/remini

━━━━━━━━━━━━━━━
🎵 LISTENING APPS
━━━━━━━━━━━━━━━

/spotify
/applemusic

━━━━━━━━━━━━━━━
📱 NOKOS
━━━━━━━━━━━━━━━

/nokostele
/nokoswa
/nokosapk

━━━━━━━━━━━━━━━
⭐ TELEGRAM PREMIUM
━━━━━━━━━━━━━━━

/teleprem

━━━━━━━━━━━━━━━
📈 SOCIAL SERVICES
━━━━━━━━━━━━━━━

/social

━━━━━━━━━━━━━━━
💳 STORE MENU
━━━━━━━━━━━━━━━

/payment
/admin
"""

    await update.message.reply_text(text)

# =========================================
# NETFLIX
# =========================================

async def netflix(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎬 NETFLIX

⟢ 1d1u : 1.5OO
⟢ 3d1u : 3.5OO
⟢ 7d1u : 7.5OO
⟢ 1month 1u : 17.OOO

⟢ 1d2u : 1.2OO
⟢ 3d2u : 2.5OO
⟢ 7d2u : 6.5OO
⟢ 1month 2u : 16.OOO

⟢ 1d semipriv : 3.OOO
⟢ 3d semipriv : 4.5OO
⟢ 7d semipriv : 8.5OO
⟢ 1month semipriv : 23.OOO

⟢ 7d private : 5O.OOO
⟢ 1month private : 1O5.OOO
"""

    await update.message.reply_text(text)

# =========================================
# DISNEY
# =========================================

async def disney(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎬 DISNEY+

⟢ sharing 1d : 3.500
⟢ sharing 1w 10u : 8.500
⟢ sharing 1b 6u : 26.000
⟢ private 1b : 126.000
"""

    await update.message.reply_text(text)

# =========================================
# VIU
# =========================================

async def viu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📺 VIU

⟢ private anti limit 1b : 500p
⟢ private anti limit 3b : 1.500
⟢ private anti limit 1y : 2.000
⟢ viu+ 1b : 7.500
⟢ viu lifetime : 2.500
"""

    await update.message.reply_text(text)

# =========================================
# IQIYI
# =========================================

async def iqiyi(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📺 IQIYI

⟢ premium 1b : 4.000
⟢ premium 3b : 9.000
⟢ premium 1y : 11.000

⟢ std 1b : 3.500
⟢ std 3b : 8.000
⟢ std 1y : 9.000
"""

    await update.message.reply_text(text)

# =========================================
# YOUTUBE
# =========================================

async def youtube(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """

⟢ famplan 1b : 1.500
⟢ famplan 2b : 3.000
⟢ famplan 3b : 4.500
⟢ indplan 1b : 2.500
⟢ famphead 1b : 5.000
"""

    await update.message.reply_text(text)

# =========================================
# CAPCUT
# =========================================

async def capcut(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎬 CAPCUT

⟢ sharing 1day : 9OOp
⟢ sharing 7day : 1.5OO
⟢ sharing 1month : 5.OOO

━━━━━━━━━━━━━━━

⟢ private 7day : 4.OOO
⟢ private 14day : 5.OOO
⟢ private 21day : 6.5OO
⟢ private 28day : 1O.OOO
⟢ private 1month : 12.OOO
"""

    await update.message.reply_text(text)

# =========================================
# CANVA
# =========================================

async def canva(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎨 CANVA

⟢ 1d member : 40p
⟢ 7d member : 100p
⟢ 1b member : 250p
⟢ 2b : 600p
⟢ 3b : 1.000
⟢ 6b : 1.300

⟢ 1y renew : 2.000
⟢ 1y no renew : 3.000
⟢ 1y member gar8m : 6.OOO
⟢ 1y member fullgar : 8.OOO

⟢ lifetime : 3.800
"""

    await update.message.reply_text(text)

# =========================================
# SPOTIFY
# =========================================

async def spotify(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎵 SPOTIFY [ full gar ]

⟢ fampl 7d : 7.500
⟢ fampl 14d : 9.000
⟢ fampl 1b : 13.000
⟢ fampl 2b : 24.000

⟢ indpl 7d : 8.000
⟢ indpl 1b : 14.000

━━━━━━━━━━━━━━━

🎵 SPOTIFY [ no gar ]

⟢ fampl 1b : 5.000
⟢ indpl 1b : 6.000
⟢ indpl 3b : 16.000
"""

    await update.message.reply_text(text)

# =========================================
# TELEGRAM PREMIUM
# =========================================

async def teleprem(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
⭐ TELEGRAM PREMIUM

via login

⟢ 1 bulan no indo : 52.000
⟢ 1 bulan no luar : 55.000
⟢ 3 bulan : 208.000
⟢ 6 bulan : 277.000
⟢ 1 tahun : 371.000

━━━━━━━━━━━━━━━

via gift

⟢ 3 bulan : 206.000
⟢ 6 bulan : 274.000
⟢ 1 tahun : 498.000
"""

    await update.message.reply_text(text)

# =========================================
# SOCIAL SERVICES
# =========================================

async def social(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📈 SOCIAL SERVICES

INSTAGRAM FOLLOWERS
› 100 : 2.000
› 500 : 4.500
› 1000 : 9.000

━━━━━━━━━━━━━━━

TIKTOK FOLLOWERS
› 100 : 3.000
› 500 : 9.000
› 1000 : 16.000

━━━━━━━━━━━━━━━

YOUTUBE SUBSCRIBE
› 10 sub : 4.300
› 50 sub : 16.300
› 100 sub : 31.300

━━━━━━━━━━━━━━━

WHATSAPP MEMBER SALURAN
› 10 : 1.800
› 50 : 5.000
› 100 : 9.000
"""

    await update.message.reply_text(text)

# =========================================
# ADMIN
# =========================================

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
👑 ADMIN STORE

OWNER:
@mycaelish
@mycuddlee
"""

    await update.message.reply_text(text)
# ============================================
# DONE COMMAND
# ============================================

async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message.reply_to_message:
        await update.message.reply_text(
            "Reply chat customer lalu ketik /d"
        )
        return

    user_id = update.message.reply_to_message.from_user.id

    try:

        # mute user
        await context.bot.restrict_chat_member(
            chat_id=-1003924200293,
            user_id=user_id,
            permissions=ChatPermissions(
                can_send_messages=False
            )
        )

        # notif
        await update.message.reply_text(
f"""
👋 Hallo {update.message.reply_to_message.from_user.mention_html()} Silakan isi rnk disini:

https://t.me/mycapyla/23

dan anda akan di lepas hukuman setelah mengisi rnk!

-- BOT VIP MYCA --
""",
            parse_mode="HTML"
        )

    except Exception as e:
        await update.message.reply_text(str(e))


# ============================================
# DETECT RNK
# ============================================

async def detect_rnk(update: Update, context: ContextTypes.DEFAULT_TYPE):

    CHANNEL_ID = -1003977810960

    if update.effective_chat.id == CHANNEL_ID:

        user_id = update.effective_user.id

        try:

            await context.bot.restrict_chat_member(
                chat_id=-1003924200293,
                user_id=user_id,
                permissions=ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_add_web_page_previews=True
                )
            )

            await update.message.reply_text(
f"""
✅ @{update.effective_user.username} sudah mengisi RnK dan telah di lepas hukuman.

-- BOT VIP MYCA --
"""
            )

        except:
            pass

# =========================================
# RUN BOT
# =========================================

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pricelist", pricelist))

app.add_handler(CommandHandler("netflix", netflix))
app.add_handler(CommandHandler("disney", disney))
app.add_handler(CommandHandler("viu", viu))
app.add_handler(CommandHandler("iqiyi", iqiyi))
app.add_handler(CommandHandler("youtube", youtube))

app.add_handler(CommandHandler("capcut", capcut))
app.add_handler(CommandHandler("canva", canva))

app.add_handler(CommandHandler("spotify", spotify))
app.add_handler(CommandHandler("teleprem", teleprem))

app.add_handler(CommandHandler("social", social))

app.add_handler(CommandHandler("admin", admin))

app.add_handler(CommandHandler("d", done))
app.add_handler(MessageHandler(filters.ALL, detect_rnk))
print("MYCA STORE RUNNING...")

app.run_polling()

# =========================================
# DATABASE
# =========================================

group_members = set()
rnk_users = set()

GROUP_ID = -3924200293
RNK_CHANNEL_ID = -1003977810960

# =========================================
# SAVE MEMBER
# =========================================

async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):

    for user in update.message.new_chat_members:

        group_members.add(user.id)

# =========================================
# DETECT RNK CHANNEL
# =========================================

async def detect_rnk(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_chat.id != RNK_CHANNEL_ID:
        return

    user_id = update.effective_user.id

    # save user yg udh isi RnK
    rnk_users.add(user_id)

    try:

        # unmute
        await context.bot.restrict_chat_member(
            chat_id=GROUP_ID,
            user_id=user_id,
            permissions=ChatPermissions(
                can_send_messages=True
            )
        )

        # notif
        await context.bot.send_message(
            chat_id=GROUP_ID,
            text=f"""
✅ @{update.effective_user.username} sudah mengisi RnK dan telah di lepas hukuman.

-- BOT VIP MYCA --
"""
        )

    except:
        pass

# =========================================
# DONE COMMAND
# =========================================

async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message.reply_to_message:

        await update.message.reply_text(
            "Reply chat customer lalu ketik /d"
        )
        return

    user_id = update.message.reply_to_message.from_user.id

    # kalau belum isi RnK
    if user_id not in rnk_users:

        try:

            # mute
            await context.bot.restrict_chat_member(
                chat_id=GROUP_ID,
                user_id=user_id,
                permissions=ChatPermissions(
                    can_send_messages=False
                )
            )

            # notif
            await update.message.reply_text(
                f"""
👋 Hallo {update.message.reply_to_message.from_user.mention_html()} Silakan isi rnk disini [ t.me/mycapyla/23 ] dan anda akan di lepas hukuman setelah mengisi rnk!

-- BOT VIP MYCA --
""",
                parse_mode="HTML"
            )

        except Exception as e:

            await update.message.reply_text(str(e))

    else:

        await update.message.reply_text(
            "✅ Customer sudah isi RnK."
        )

        # reset supaya next order wajib isi lagi
        rnk_users.remove(user_id)

# =========================================
# HANDLER
# =========================================

app.add_handler(
    MessageHandler(
        filters.StatusUpdate.NEW_CHAT_MEMBERS,
        new_member
    )
)

app.add_handler(
    MessageHandler(filters.ALL, detect_rnk)
)

app.add_handler(CommandHandler("d", done))

print("MYCA STORE RUNNING...")

app.run_polling()