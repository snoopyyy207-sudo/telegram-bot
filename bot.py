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
/youtube
/disney
/viu
/iqiyi
/loklok
/bstation
/youku

🎨 EDITING
/capcut
/canva
/alightmotion
/picsart
/meitu
/wink
/remini

🤖 AI
/chatgpt
/gptgo
/gemini

🎮 TOPUP
/topup
/telestars
"""

    await update.message.reply_text(text)

# =========================================
# SPOTIFY
# =========================================

async def spotify(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . SPOTIFY
───────

⟢ 1b indp fullgar
🌷 IDR 14.000

⟢ 1b indp garansi 20d
🌷 IDR 12.000

⟢ 1b indp nogar
🌷 IDR 5.500
"""

    await update.message.reply_text(text)

# =========================================
# NETFLIX
# =========================================

async def netflix(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . NETFLIX
───────

⟢ sharing 1u 1 day
🌷 IDR 3.800

⟢ sharing 1u 3 day
🌷 IDR 5.800

⟢ sharing 1u 7 day
🌷 IDR 8.800
"""

    await update.message.reply_text(text)

# =========================================
# DISNEY
# =========================================

async def disney(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . DISNEY+
───────

⟢ sharing 1d
🌷 IDR 3.500

⟢ sharing 1b
🌷 IDR 26.000
"""

    await update.message.reply_text(text)

# =========================================
# VIU
# =========================================

async def viu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . VIU
───────

⟢ viu+ 1b
🌷 IDR 7.500

⟢ viu lifetime
🌷 IDR 2.500
"""

    await update.message.reply_text(text)

# =========================================
# IQIYI
# =========================================

async def iqiyi(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . IQIYI
───────

⟢ premium 1b
🌷 IDR 4.000

⟢ premium 3b
🌷 IDR 9.000
"""

    await update.message.reply_text(text)

# =========================================
# LOKLOK
# =========================================

async def loklok(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . LOKLOK
───────

⟢ sharing basic
🌷 IDR 12.350

⟢ private standar
🌷 IDR 65.350
"""

    await update.message.reply_text(text)

# =========================================
# BSTATION
# =========================================

async def bstation(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . BSTATION
───────

⟢ sharing 1b
🌷 IDR 4.000

⟢ private 1b
🌷 IDR 29.000
"""

    await update.message.reply_text(text)

# =========================================
# YOUKU
# =========================================

async def youku(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . YOUKU
───────

⟢ sharing 1b
🌷 IDR 5.000
"""

    await update.message.reply_text(text)

# =========================================
# CAPCUT
# =========================================

async def capcut(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . CAPCUT
───────

⟢ sharing 1month
🌷 IDR 5.000

⟢ private 1month
🌷 IDR 12.000
"""

    await update.message.reply_text(text)

# =========================================
# CANVA
# =========================================

async def canva(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . CANVA
───────

⟢ 1b member
🌷 IDR 250p

⟢ lifetime
🌷 IDR 3.800
"""

    await update.message.reply_text(text)

# =========================================
# ALIGHT MOTION
# =========================================

async def alightmotion(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . ALIGHT MOTION
───────

⟢ sharing 1b
🌷 IDR 400p
"""

    await update.message.reply_text(text)

# =========================================
# PICSART
# =========================================

async def picsart(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . PICSART
───────

⟢ sharing 1b
🌷 IDR 2.500
"""

    await update.message.reply_text(text)

# =========================================
# MEITU
# =========================================

async def meitu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . MEITU
───────

⟢ sharing 1b
🌷 IDR 14.000
"""

    await update.message.reply_text(text)

# =========================================
# WINK
# =========================================

async def wink(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . WINK
───────

⟢ private andro 7d
🌷 IDR 6.500
"""

    await update.message.reply_text(text)

# =========================================
# REMINI
# =========================================

async def remini(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
:¨ ·.· ¨: ──────
`· . REMINI
───────

⟢ web 1b
🌷 IDR 5.000
"""

    await update.message.reply_text(text)