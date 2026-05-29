from telegram import Update, ChatPermissions
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)

TOKEN = "8688671404:AAG__A8l8lU0dACFXNULcpLo9m8klUi4Rps"

GROUP_ID = -1003924200293
RNK_CHANNEL_ID = -1003977810960

app = ApplicationBuilder().token(TOKEN).build()

# =========================================
# START
# =========================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
𐙚 MYCA STORE BOT

gunakan /pricelist untuk melihat semua menu 🎀
"""

    await update.message.reply_text(text)

# =========================================
# PRICELIST
# =========================================

async def pricelist(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎬 STREAMING
/netflix
/spotify
/applemusic
/youtube
/disney
/viu
/iqiyi
/loklok
/bstation
/youku
/wetv
/vidio

🎨 EDITING
/capcut
/canva
/alightmotion
/picsart
/meitu
/wink
/remini

📱 NOKOS
/nokostele
/nokoswa
/nokosapk

🤖 AI
/chatgpt
/gptgo
/gemini

🎮 TOPUP
/topup
/telestars

📈 SERVICES
/kebsos
"""

    await update.message.reply_text(text)

# =========================================
# SPOTIFY
# =========================================

async def spotify(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . SPOTIFY
───────

˳ ✉️ ྀི  soft (&.) heart ___;3
.° price list 𓈆 ₊˚ 🎀

⟢ 1b indp fullgar
🌷 ⠖ ◞ 🕊️˚ IDR 14.000 ༝ ꒱ა

⟢ 1b indp garansi 20d
🌷 ⠖ ◞ 🕊️˚ IDR 12.000 ༝ ꒱ა

⟢ 1b indp nogar
🌷 ⠖ ◞ 🕊️˚ IDR 5.500 ༝ ꒱ა

⟢ 1b indp garansi 24 jam
🌷 ⠖ ◞ 🕊️˚ IDR 8.000 ༝ ꒱ა

⟢ 2b fullgar
🌷 ⠖ ◞ 🕊️˚ IDR 21.700 ༝ ꒱ა

⟢ 2b famplan garansi 25d
🌷 ⠖ ◞ 🕊️˚ IDR 17.000 ༝ ꒱ა

⟢ 3b indplan fullgar
🌷 ⠖ ◞ 🕊️˚ IDR 32.000 ༝ ꒱ა

⁺ִ ∝ꞌꞋ ࣪ 🍓 note ₎

. Ი𐑼 tanyakan stok terlebih dahulu
. Ი𐑼 fast respon jika tidak ada antrian
. Ი𐑼 wajib ss log untuk claim
. Ი𐑼 max ss 5 jam
"""

    await update.message.reply_text(text)

# =========================================
# APPLE MUSIC
# =========================================

async def applemusic(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . APPLE MUSIC
───────

˳ ✉️ ྀི soft (&.) heart ___;3
.° price list 𓈆 ₊˚ 🎀

⟢ 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 4.000 ༝ ꒱ა

⟢ 3 month
🌷 ⠖ ◞ 🕊️˚ IDR 10.000 ༝ ꒱ა

⁺ִ ∝ꞌꞋ ࣪ 🍓 note ₎

. Ი𐑼 wajib email fresh
. Ი𐑼 garansi sesuai ketentuan
. Ი𐑼 wajib ss log untuk claim
"""

    await update.message.reply_text(text)

# =========================================
# NETFLIX
# =========================================

async def netflix(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . NETFLIX
───────

🎬 STRONG AKUN

⟢ sharing 1u 1 day
🌷 ⠖ ◞ 🕊️˚ IDR 3.800 ༝ ꒱ა

⟢ sharing 1u 3 day
🌷 ⠖ ◞ 🕊️˚ IDR 5.800 ༝ ꒱ა

⟢ sharing 1u 7 day
🌷 ⠖ ◞ 🕊️˚ IDR 8.800 ༝ ꒱ა

⟢ sharing 1u 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 29.000 ༝ ꒱ა

⟢ sharing 2u 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 19.000 ༝ ꒱ა

⟢ semipriv 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 33.000 ༝ ꒱ა

⟢ private 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 111.000 - 152.000 ༝ ꒱ა

🍓 NO STRONG AVAILABLE

⟢ sharing mulai
🌷 ⠖ ◞ 🕊️˚ IDR 800 - 25.000 ༝ ꒱ა

⁺ִ ∝ꞌꞋ ࣪ 🍓 note ₎

. Ი𐑼 no strong tidak strong akun
. Ი𐑼 wajib ss log untuk claim
. Ი𐑼 garansi sesuai keterangan
"""

    await update.message.reply_text(text)

# =========================================
# LOKLOK
# =========================================

async def loklok(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . LOKLOK
───────

⟢ sharing basic 8 users
🌷 ⠖ ◞ 🕊️˚ IDR 12.350 ༝ ꒱ა

⟢ sharing basic 3 users
🌷 ⠖ ◞ 🕊️˚ IDR 15.350 ༝ ꒱ა

⟢ sharing standar 8 users
🌷 ⠖ ◞ 🕊️˚ IDR 17.850 ༝ ꒱ა

⟢ sharing standar 3 users
🌷 ⠖ ◞ 🕊️˚ IDR 20.850 ༝ ꒱ა

⟢ private basic
🌷 ⠖ ◞ 🕊️˚ IDR 50.850 ༝ ꒱ა

⟢ private standar
🌷 ⠖ ◞ 🕊️˚ IDR 65.350 ༝ ꒱ა

⁺ִ ∝ꞌꞋ ࣪ 🍓 note ₎

. Ი𐑼 basic tidak bisa akses tv
. Ი𐑼 standar bisa akses tv
"""

    await update.message.reply_text(text)

# =========================================
# YOUTUBE PREMIUM
# =========================================

async def youtube(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . YOUTUBE PREMIUM
───────

˳ ✉️ ྀི soft (&.) heart ___;3
.° price list 𓈆 ₊˚ 🎀

⟢ famplan 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 1.000 ༝ ꒱ა

⟢ famplan 2 month
🌷 ⠖ ◞ 🕊️˚ IDR 3.000 ༝ ꒱ა

⟢ famplan 3 month
🌷 ⠖ ◞ 🕊️˚ IDR 4.000 ༝ ꒱ა

⟢ indplan 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 4.000 ༝ ꒱ა

⟢ indplan 2 month
🌷 ⠖ ◞ 🕊️˚ IDR 15.800 ༝ ꒱ა

⟢ indplan 3 month
🌷 ⠖ ◞ 🕊️˚ IDR 18.800 ༝ ꒱ა

⟢ mixplan 2 month
🌷 ⠖ ◞ 🕊️˚ IDR 11.000 ༝ ꒱ა

⟢ famhead 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 3.000 ༝ ꒱ა

⁺ִ ∝ꞌꞋ ࣪ 🍓 note ₎

. Ი𐑼 jaspay email buyer wajib fresh
. Ი𐑼 wajib ss log untuk claim
. Ი𐑼 garansi sesuai ketentuan
"""

    await update.message.reply_text(text)

# =========================================
# DISNEY+
# =========================================

async def disney(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . DISNEY+
───────

⟢ sharing 1d
🌷 ⠖ ◞ 🕊️˚ IDR 3.500 ༝ ꒱ა

⟢ sharing 1w 10u
🌷 ⠖ ◞ 🕊️˚ IDR 8.500 ༝ ꒱ა

⟢ sharing 1b 6u
🌷 ⠖ ◞ 🕊️˚ IDR 26.000 ༝ ꒱ა

⟢ private 1b
🌷 ⠖ ◞ 🕊️˚ IDR 126.000 ༝ ꒱ა

⁺ִ ∝ꞌꞋ ࣪ 🍓 note ₎

. Ი𐑼 sharing sesuai slot
. Ი𐑼 wajib ss log untuk claim
"""

    await update.message.reply_text(text)

# =========================================
# VIU
# =========================================

async def viu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . VIU
───────

⟢ private anti limit 1b
🌷 ⠖ ◞ 🕊️˚ IDR 500p ༝ ꒱ა

⟢ private anti limit 3b
🌷 ⠖ ◞ 🕊️˚ IDR 1.500 ༝ ꒱ა

⟢ viu+ 1b
🌷 ⠖ ◞ 🕊️˚ IDR 7.500 ༝ ꒱ა

⟢ viu lifetime
🌷 ⠖ ◞ 🕊️˚ IDR 2.500 ༝ ꒱ა
"""

    await update.message.reply_text(text)# =========================================
# IQIYI
# =========================================

async def iqiyi(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . IQIYI
───────

⟢ premium 1b
🌷 ⠖ ◞ 🕊️˚ IDR 4.000 ༝ ꒱ა

⟢ premium 3b
🌷 ⠖ ◞ 🕊️˚ IDR 9.000 ༝ ꒱ა

⟢ premium 1y
🌷 ⠖ ◞ 🕊️˚ IDR 11.000 ༝ ꒱ა

⟢ std 1b
🌷 ⠖ ◞ 🕊️˚ IDR 3.500 ༝ ꒱ა
"""

    await update.message.reply_text(text)

# =========================================
# BSTATION
# =========================================

async def bstation(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . BSTATION
───────

⟢ sharing 1b
🌷 ⠖ ◞ 🕊️˚ IDR 4.000 ༝ ꒱ა

⟢ sharing 3b
🌷 ⠖ ◞ 🕊️˚ IDR 8.500 ༝ ꒱ა

⟢ sharing 1y
🌷 ⠖ ◞ 🕊️˚ IDR 11.000 ༝ ꒱ა

⟢ private 1b
🌷 ⠖ ◞ 🕊️˚ IDR 29.000 ༝ ꒱ა
"""

    await update.message.reply_text(text)

# =========================================
# YOUKU
# =========================================

async def youku(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . YOUKU
───────

⟢ sharing 1b
🌷 ⠖ ◞ 🕊️˚ IDR 5.000 ༝ ꒱ა

⟢ sharing 3b
🌷 ⠖ ◞ 🕊️˚ IDR 8.000 ༝ ꒱ა

⟢ sharing 1y
🌷 ⠖ ◞ 🕊️˚ IDR 11.000 ༝ ꒱ა
"""

    await update.message.reply_text(text)

# =========================================
# WETV
# =========================================

async def wetv(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . WETV
───────

˳ ✉️ ྀི soft (&.) heart ___;3
.° price list 𓈆 ₊˚ 🎀

⟢ sharing 6u 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 5.000 ༝ ꒱ა

⟢ sharing 3u 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 9.000 ༝ ꒱ა

⟢ sharing 3u 3 month
🌷 ⠖ ◞ 🕊️˚ IDR 16.000 ༝ ꒱ა

⟢ sharing 2u 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 12.000 ༝ ꒱ა

⟢ private 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 24.800 ༝ ꒱ა

⁺ִ ∝ꞌꞋ ࣪ 🍓 note ₎

. Ი𐑼 private bebas pake nomor sendiri
. Ი𐑼 wajib ss log untuk claim
"""

    await update.message.reply_text(text)

# =========================================
# VIDIO
# =========================================

async def vidio(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . VIDIO
───────

˳ ✉️ ྀི soft (&.) heart ___;3
.° price list 𓈆 ₊˚ 🎀

⟢ sharing harian 1 day
🌷 ⠖ ◞ 🕊️˚ IDR 3.000 ༝ ꒱ა

⟢ sharing harian 3 day
🌷 ⠖ ◞ 🕊️˚ IDR 5.000 ༝ ꒱ა

⟢ sharing harian 7 day
🌷 ⠖ ◞ 🕊️˚ IDR 8.000 ༝ ꒱ა

⟢ sharing bulanan mobile
🌷 ⠖ ◞ 🕊️˚ IDR 15.000 ༝ ꒱ა

⟢ sharing bulanan alldev
🌷 ⠖ ◞ 🕊️˚ IDR 19.000 ༝ ꒱ა

⟢ diamond 2u 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 33.000 ༝ ꒱ა

⟢ diamond private 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 51.000 ༝ ꒱ა
"""

    await update.message.reply_text(text)

# =========================================
# CAPCUT
# =========================================

async def capcut(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . CAPCUT
───────

⟢ sharing 1 day
🌷 ⠖ ◞ 🕊️˚ IDR 900p ༝ ꒱ა

⟢ sharing 7 day
🌷 ⠖ ◞ 🕊️˚ IDR 1.500 ༝ ꒱ა

⟢ sharing 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 5.000 ༝ ꒱ა

⟢ private 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 12.000 ༝ ꒱ა
"""

    await update.message.reply_text(text)

# =========================================
# CANVA
# =========================================

async def canva(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . CANVA
───────

⟢ 1d member
🌷 ⠖ ◞ 🕊️˚ IDR 40p ༝ ꒱ა

⟢ 7d member
🌷 ⠖ ◞ 🕊️˚ IDR 100p ༝ ꒱ა

⟢ 1b member
🌷 ⠖ ◞ 🕊️˚ IDR 250p ༝ ꒱ა

⟢ lifetime
🌷 ⠖ ◞ 🕊️˚ IDR 3.800 ༝ ꒱ა
"""

    await update.message.reply_text(text)

# =========================================
# ALIGHT MOTION
# =========================================

async def alightmotion(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . ALIGHT MOTION
───────

⟢ sharing 1b
🌷 ⠖ ◞ 🕊️˚ IDR 400p ༝ ꒱ა

⟢ sharing 1y
🌷 ⠖ ◞ 🕊️˚ IDR 500p ༝ ꒱ა

⟢ private 1y
🌷 ⠖ ◞ 🕊️˚ IDR 1.000 ༝ ꒱ა

⟢ avail acc b
🌷 ⠖ ◞ 🕊️˚ IDR 1.500 ༝ ꒱ა
"""

    await update.message.reply_text(text)

# =========================================
# PICSART
# =========================================

async def picsart(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . PICSART
───────

⟢ sharing 1b
🌷 ⠖ ◞ 🕊️˚ IDR 2.500 ༝ ꒱ა

⟢ private 1b
🌷 ⠖ ◞ 🕊️˚ IDR 5.000 ༝ ꒱ა
"""

    await update.message.reply_text(text)

# =========================================
# MEITU
# =========================================

async def meitu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . MEITU
───────

˳ ✉️ ྀི soft (&.) heart ___;3
.° price list 𓈆 ₊˚ 🎀

⟢ sharing 1b
🌷 ⠖ ◞ 🕊️˚ IDR 14.000 ༝ ꒱ა

⟢ private 1b
🌷 ⠖ ◞ 🕊️˚ IDR 31.000 ༝ ꒱ა
"""

    await update.message.reply_text(text)

# =========================================
# WINK
# =========================================

async def wink(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . WINK
───────

⟢ private andro 7d
🌷 ⠖ ◞ 🕊️˚ IDR 6.500 ༝ ꒱ა

⟢ sharing andro 7d
🌷 ⠖ ◞ 🕊️˚ IDR 3.500 ༝ ꒱ა
"""

    await update.message.reply_text(text)

# =========================================
# REMINI
# =========================================

async def remini(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . REMINI
───────

⟢ web 1b
🌷 ⠖ ◞ 🕊️˚ IDR 5.000 ༝ ꒱ა
"""

    await update.message.reply_text(text)

# =========================================
# NOKOS TELEGRAM
# =========================================

async def nokostele(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . NOKOS TELEGRAM
───────

🌷 indo fs : 4.600 - 5.900
🌷 usa : 7.500 - 9.000
🌷 canada : 7.000 - 8.500
🌷 malaysia : 8.000 - 9.500
🌷 myanmar : 8.000 - 9.500
🌷 vietnam : 8.000 - 9.500
"""

    await update.message.reply_text(text)

# =========================================
# NOKOS WHATSAPP
# =========================================

async def nokoswa(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . NOKOS WHATSAPP
───────

🌷 indo no gar : 3.500 - 4.500
🌷 indo gar : 9.000 - 12.000
"""

    await update.message.reply_text(text)

# =========================================
# NOKOS APK
# =========================================

async def nokosapk(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . NOKOS APK
───────

🌷 shopee : 2.500
🌷 lazada : 2.200
🌷 gojek : 2.200
🌷 grab : 2.200
🌷 alfagift : 2.500
🌷 indomaret : 2.500
🌷 viber : 3.000
🌷 maxim : 2.500
"""

    await update.message.reply_text(text)

# =========================================
# CHATGPT
# =========================================

async def chatgpt(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . CHATGPT
───────

⟢ gpt go 6b garansi 15h
🌷 ⠖ ◞ 🕊️˚ IDR 18.000 ༝ ꒱ა

⟢ gpt go 8b garansi 7d
🌷 ⠖ ◞ 🕊️˚ IDR 22.000 ༝ ꒱ა
"""

    await update.message.reply_text(text)

# =========================================
# GEMINI
# =========================================

async def gemini(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . GEMINI AI
───────

⟢ shar 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 6.000 ༝ ꒱ა

⟢ head 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 8.000 ༝ ꒱ა

⟢ invt 1 month
🌷 ⠖ ◞ 🕊️˚ IDR 4.000 ༝ ꒱ა
"""

    await update.message.reply_text(text)

# =========================================
# TELESTARS
# =========================================

async def telestars(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . TELESTARS
───────

˳ ✉️ ྀི soft (&.) heart ___;3
.° price list 𓈆 ₊˚ 🎀

୨୧ via top up

🌷 50s : 14.500
🌷 75s : 21.500
🌷 100s : 28.500
🌷 150s : 42.500
🌷 dst.

୨୧ via gift

🌷 15s : 4.500
🌷 25s : 7.500
🌷 50s : 14.500
🌷 dst.

⁺ִ ∝ꞌꞋ ࣪ 🍓 note ₎

. Ი𐑼 wajib send username/id
. Ი𐑼 proses 1-10 menit
. Ი𐑼 no refund jika salah id
"""

    await update.message.reply_text(text)

# =========================================
# TOPUP GAME
# =========================================

async def topup(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . TOP UP GAME
───────

୨୧ FREE FIRE MAX

🌷 70dm : 10.500
🌷 140dm : 19.500
🌷 355dm : 48.700

୨୧ FREE FIRE BIASA

🌷 70dm : 10.400
🌷 100dm : 14.000
🌷 210dm : 29.000
🌷 355dm : 48.000
🌷 510dm : 67.500

୨୧ MOBILE LEGEND

🌷 44dm : 11.000
🌷 74dm : 19.500
🌷 85dm : 20.500
🌷 170dm : 41.800

୨୧ PUBG

🌷 60uc : 16.300
🌷 325uc : 76.200
🌷 660uc : 151.800

⁺ִ ∝ꞌꞋ ࣪ 🍓 note ₎

. Ი𐑼 wajib kirim id + server
. Ი𐑼 proses fast jika tidak ramai
. Ი𐑼 no refund salah id
"""

    await update.message.reply_text(text)

# =========================================
# KEBSOS
# =========================================

async def kebsos(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨:  ──────
`· . KEBSOS
───────

୨୧ INSTAGRAM SERVICES

followers refill 30h
🌷 100 : 2.000
🌷 200 : 2.800
🌷 500 : 4.500
🌷 1000 : 9.000

likes no refill
🌷 1000 : 2.500
🌷 5000 : 7.500
🌷 10k : 15.500

views
🌷 1000 : 1.600
🌷 100k : 6.000

୨୧ TIKTOK SERVICES

followers no refill
🌷 100 : 3.000
🌷 500 : 9.000
🌷 1000 : 16.000

likes
🌷 1000 : 2.500
🌷 5000 : 6.500
🌷 10k : 10.500

views
🌷 1000 : 2.250
🌷 10k : 8.500

୨୧ YOUTUBE SERVICES

subscribe refill 30h
🌷 10 sub : 4.300
🌷 50 sub : 16.300
🌷 100 sub : 31.300

views permanen
🌷 100 : 3.500
🌷 500 : 12.500

comments
🌷 100 : 2.500
🌷 1000 : 14.500
"""

    await update.message.reply_text(text)

# =========================================
# HANDLER
# =========================================

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pricelist", pricelist))

# STREAMING
app.add_handler(CommandHandler("spotify", spotify))
app.add_handler(CommandHandler("applemusic", applemusic))
app.add_handler(CommandHandler("netflix", netflix))
app.add_handler(CommandHandler("youtube", youtube))
app.add_handler(CommandHandler("disney", disney))
app.add_handler(CommandHandler("viu", viu))
app.add_handler(CommandHandler("iqiyi", iqiyi))
app.add_handler(CommandHandler("loklok", loklok))
app.add_handler(CommandHandler("bstation", bstation))
app.add_handler(CommandHandler("youku", youku))
app.add_handler(CommandHandler("wetv", wetv))
app.add_handler(CommandHandler("vidio", vidio))

# EDITING
app.add_handler(CommandHandler("capcut", capcut))
app.add_handler(CommandHandler("canva", canva))
app.add_handler(CommandHandler("alightmotion", alightmotion))
app.add_handler(CommandHandler("picsart", picsart))
app.add_handler(CommandHandler("meitu", meitu))
app.add_handler(CommandHandler("wink", wink))
app.add_handler(CommandHandler("remini", remini))

# NOKOS
app.add_handler(CommandHandler("nokostele", nokostele))
app.add_handler(CommandHandler("nokoswa", nokoswa))
app.add_handler(CommandHandler("nokosapk", nokosapk))

# AI
app.add_handler(CommandHandler("chatgpt", chatgpt))
app.add_handler(CommandHandler("gptgo", gptgo))
app.add_handler(CommandHandler("gemini", gemini))

# TOPUP
app.add_handler(CommandHandler("topup", topup))
app.add_handler(CommandHandler("telestars", telestars))

print("MYCA STORE RUNNING...")

app.run_polling()