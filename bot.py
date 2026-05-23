# =========================================
# MYCA | FH APP PREM 
# =========================================

from telegram import Update, ChatPermissions

from telegram.ext import (
    Application,
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
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
📌Gunakan command berikut untuk melihat pricelist:
/netflix
/disney
/viu
/iqiyi
/youtube
/bstation
/youku
/loklok
/wetv
/vidio
/capcut
/canva
/alightmotion
/picsart
/meitu
/wink
/remini
/spotify
/applemusic
/gemini
/chatgpt
/nokostele
/nokoswa
/nokosapk
/teleprem
/kebsos
"""

    await update.message.reply_text(text)

# =========================================
# NETFLIX
# =========================================

async def netflix(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎬 NETFLIX ( STRONG AKUN )

• Sharing 1u
• 1 Day : 3.800
• 3 Day : 5.800
• 7 Day : 8.800
• 1 Month : 29.000

• Sharing 2u
• 1 Day : 3.500
• 3 Day : 5.200
• 7 Day : 9.800
• 1 Month : 19.000
• Semipriv 1 Month : 33.000

• Private ( made by order )
• 1 Week : 61.000
• 1 Month : 111.000 – 152.000


🎬 NETFLIX ( NO STRONG )

• Sharing 1U
• 1d : 1.950(link) ➜ 2.800(code)
• 2d : 3.500(link) ➜ 4.350(code)
• 3d : 4.500(link) ➜ 5.350(code)
• 7d : 6.500(link) ➜ 7.350(code)
• 1 Month : 15.500(link) ➜ 25.000(code)

• Sharing 2U
• 1d : 1.800(link) ➜ 2.650(code)
• 2d : 2.800(link) ➜ 3.650(code)
• 3d : 4.000(link) ➜ 4.850(code)
• 7d : 5.800
• 1 Month : 10.500(link) ➜ 14.000(code)
• Semipriv 1 Month : 20.000(link) ➜ 30.000(code)

» Note
» GA STRONG AKUN
"""

    await update.message.reply_text(text)

# =========================================
# DISNEY
# =========================================

async def disney(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎬 DISNEY+

• Sharing 6 User
• 1 Day : 4.000
• 3 Day : 7.000
• 7 Day : 15.500
• 1 Month : 21.000

• Sharing 10 User
• 1 Day : 3.500
• 3 Day : 6.000
• 7 Day : 10.000
• 1 Month : 16.000
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
# YOUTUBE PREMIUM
# =========================================

async def youtube(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
▶️ YOUTUBE PREMIUM

• Famplan
• 1 Month : 1.000
• 2 Month : 3.000
• 3 Month : 4.000

• Indplan
• 1 Month : 4.000
• 2 Month : 15.800
• 3 Month : 18.800

• Mixplan
• 2 Month : 11.000

• Famhead
• 1 Month : 3.000
( jaspay email buyer wajib fresh )
"""

    await update.message.reply_text(text)

# =========================================
# LOKLOK
# =========================================

async def loklok(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📺 LOKLOK

• Sharing Basic 1 Month
• 8 Users : 12.350
• 3 Users : 15.350

• Sharing Standar 1 Month
• 8 Users : 17.850
• 3 Users : 20.850

• Private
• Basic : 50.850
• Standar : 65.350

• Note
• Basic tidak bisa akses TV
• Standar bisa akses TV
"""

    await update.message.reply_text(text)

# =========================================
# BSTATION
# =========================================

async def bstation(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📺 BSTATION

⟢ sharing 1b : 4.000
⟢ sharing 3b : 8.500
⟢ sharing 1y : 11.000
⟢ private 1b : 29.000
"""

    await update.message.reply_text(text)

# =========================================
# YOUKU
# =========================================

async def youku(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎞 YOUKU

⟢ sharing 1b : 5.000
⟢ sharing 3b : 8.000
⟢ sharing 1y : 11.000
"""

    await update.message.reply_text(text)

# =========================================
# WETV
# =========================================

async def wetv(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📺 WETV

• Sharing
• 6u 1 Month : 5.000
• 3u 1 Month : 9.000
• 3u 3 Month : 16.000
• 2u 1 Month : 12.000

• Private
• 1 Month : 24.800

1b priv bebas pake nomor klian
"""

    await update.message.reply_text(text)

# =========================================
# VIDIO
# =========================================

async def vidio(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📺 VIDIO PLATINUM

• Sharing Harian (only mobile)
• 1 Day : 3.000
• 3 Day : 5.000
• 7 Day : 8.000

• Sharing Bulanan
• 1 Month mobile : 15.000
• 1 Month alldev : 19.000
• 1 Years only tv : 2.500

• Private
• 1 Month mobile : 26.000
• 1 Month alldev : 31.000


💎 DIAMOND

• 2u 1 Month : 33.000
• Private 1 Month : 51.000
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

⟢ 1d member : 140p
⟢ 7d member : 400p
⟢ 1b member : 750p
⟢ 2b : 1.000
⟢ 3b : 1.400
⟢ 6b : 1.700

⟢ 1y renew : 3.000
⟢ 1y no renew : 4.000
⟢ 1y member gar8m : 7.OOO
⟢ 1y member fullgar : 9.OOO

⟢ lifetime : 4.800
"""

    await update.message.reply_text(text)

# =========================================
# ALIGHTMOTION
# =========================================

async def alightmotion(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎬 ALIGHT MOTION

⟢ sharing 1b : 400p
⟢ sharing 1y : 500p
⟢ private 1y : 1.000
⟢ avail acc b : 1.500
"""

    await update.message.reply_text(text)

# =========================================
# PICSART
# =========================================

async def picsart(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🖼 PICSART

⟢ sharing 1b : 2.500
⟢ private 1b : 5.000
"""

    await update.message.reply_text(text)


# =========================================
# MEITU
# =========================================

async def meitu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
💄 MEITU

⟢ private 7d : 1.500
⟢ private 1b : 4.500
"""

    await update.message.reply_text(text)


# =========================================
# WINK
# =========================================

async def wink(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
✨ WINK

⟢ private andro 7d : 6.500
⟢ sharing andro 7d : 3.500
"""

    await update.message.reply_text(text)


# =========================================
# REMINI
# =========================================

async def remini(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📸 REMINI

⟢ web 1b : 5.000
"""

    await update.message.reply_text(text)

# =========================================
# SPOTIFY
# =========================================

async def spotify(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎵 SPOTIFY

1B INDP FULLGAR : 14.000
1B INDP GARANSI 20D : 12.000
1B INDP NOGAR : 5.500
1B INDP GARANSI 24 JAM : 8.000

2B FULLGAR : 21.700
2B FAMPLAN GARANSI 25D : 17.000

3B INDPLAN FULLGAR : 32.000
"""

    await update.message.reply_text(text)

# =========================================
# APPLE MUSIC
# =========================================

async def applemusic(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎵 APPLE MUSIC

⟢ 1b : 4.000
⟢ 3b : 10.000
"""

    await update.message.reply_text(text)

# =========================================
# GEMINI AI
# =========================================

async def gemini(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🤖 GEMINI AI

• shar 1 Month : 6.000
• head 1 Month : 8.000
• invt 1 Month : 4.000
"""

    await update.message.reply_text(text)

# =========================================
# CHATGPT
# =========================================

async def chatgpt(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🤖 CHATGPT

• Gpt Go 6b garansi 15h : 20.000
• Gpt Go 8b garansi 7d : 24.000
"""

    await update.message.reply_text(text)

# =========================================
# NOKOS TELEGRAM
# =========================================

async def nokostele(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📱 NOKOS TELEGRAM

⟢ indo fs : 4.600 - 5.900
⟢ usa : 7.500 - 9.000
⟢ canada : 7.000 - 8.500
⟢ malaysia : 8.000 - 9.500
⟢ myanmar : 8.000 - 9.500
⟢ vietnam : 8.000 - 9.500
"""

    await update.message.reply_text(text)


# =========================================
# NOKOS WHATSAPP
# =========================================

async def nokoswa(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📱 NOKOS WHATSAPP

⟢ indo no gar : 3.500 - 4.500
⟢ indo gar : 9.000 - 12.000
"""

    await update.message.reply_text(text)


# =========================================
# NOKOS ALL APK
# =========================================

async def nokosapk(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📱 NOKOS ALL APK

⟢ shopee : 2.500
⟢ lazada : 2.200
⟢ gojek : 2.200
⟢ grab : 2.200
⟢ alfagift : 2.500
⟢ indomaret : 2.500
⟢ viber : 3.000
⟢ maxim : 2.500
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
# KEBSOS
# =========================================

async def kebsos(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📌 INSTAGRAM SERVICES

followers [ refill 30h ]
› 100 : 2.000
› 200 : 2.800
› 300 : 3.500
› 400 : 4.000
› 500 : 4.500
› 700 : 6.000
› 1000 : 9.000

likes [ no refill ]
› 1000 : 2.500
› 2000 : 3.800
› 3000 : 5.500
› 5000 : 7.500
› 7000 : 10.500
› 10k : 15.500

views
› 1000 : 1.600
› 2000 : 1.700
› 3000 : 1.800
› 100k : 6.000


📌 TIKTOK SERVICES

followers [ no refill ]
› 100 : 3.000
› 200 : 5.000
› 300 : 7.000
› 400 : 7.500
› 500 : 9.000
› 700 : 12.000
› 1000 : 16.000

followers [ refill 30h ]
› 100 : 4.000
› 250 : 7.500
› 500 : 10.500
› 700 : 13.500
› 1000 : 18.500

likes
› 1000 : 2.500
› 2000 : 3.500
› 3000 : 4.500
› 5000 : 6.500
› 8000 : 9.000
› 10k : 10.500

views
› 1000 : 2.250
› 2000 : 3.000
› 5000 : 5.100
› 8000 : 7.200
› 10k : 8.500


📌 YOUTUBE SERVICES

subscribe [ refill 30h ]
› 10 sub : 4.300
› 20 sub : 7.300
› 50 sub : 16.300
› 70 sub : 22.200
› 100 sub : 31.300

views permanen
› 100 : 3.500
› 200 : 5.500
› 500 : 12.500
› 700 : 16.600

comments
› 100 : 2.500
› 200 : 4.000
› 400 : 6.500
› 500 : 8.000
› 700 : 10.500
› 1000 : 14.500


📌 WHATSAPP SERVICES

member saluran
› 10 : 1.800
› 20 : 2.500
› 30 : 3.500
› 40 : 4.200
› 50 : 5.000
› 70 : 6.500
› 80 : 7.000
› 100 : 9.000
› 200 : 16.000
› 400 : 30.200

react saluran
› 100 : 3.000
› 200 : 4.700
› 300 : 6.000
› 500 : 9.500
› 700 : 12.800
› 1000 : 17.500
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

app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("netflix", netflix))
app.add_handler(CommandHandler("spotify", spotify))
app.add_handler(CommandHandler("youtube", youtube))
app.add_handler(CommandHandler("viu", viu))
app.add_handler(CommandHandler("iqiyi", iqiyi))
app.add_handler(CommandHandler("wetv", wetv))
app.add_handler(CommandHandler("vidio", vidio))
app.add_handler(CommandHandler("capcut", capcut))
app.add_handler(CommandHandler("canva", canva))
app.add_handler(CommandHandler("teleprem", teleprem))
app.add_handler(CommandHandler("loklok", loklok))
app.add_handler(CommandHandler("disney", disney))
app.add_handler(CommandHandler("bstation", bstation))
app.add_handler(CommandHandler("youku", youku))

app.add_handler(CommandHandler("alightmotion", alightmotion))
app.add_handler(CommandHandler("picsart", picsart))
app.add_handler(CommandHandler("meitu", meitu))
app.add_handler(CommandHandler("wink", wink))
app.add_handler(CommandHandler("remini", remini))

app.add_handler(CommandHandler("applemusic", applemusic))
app.add_handler(CommandHandler("gemini", gemini))
app.add_handler(CommandHandler("chatgpt", chatgpt))
app.add_handler(CommandHandler("nokostele", nokostele))
app.add_handler(CommandHandler("nokoswa", nokoswa))
app.add_handler(CommandHandler("nokosapk", nokosapk))
app.add_handler(CommandHandler("kebsos", kebsos))
app.add_handler(CommandHandler("d", done))

app.add_handler(MessageHandler(filters.ALL, detect_rnk))

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