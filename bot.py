import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

NOME_CORRETO = ["ferreira"]

MENSAGEM_CERTA = (
    "Registro relevante identificado.\n\n"
    "Foi encontrada uma inconsistência objetiva. "
    "O caso deve ser reavaliado."
)

MENSAGEM_ERRADA = (
    "Nenhuma inconsistência objetiva foi reconhecida.\n\n"
    "Volte aos autos e continue analisando."
)

async def inicio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Foi encontrada alguma inconsistência?\n"
        "Se sim, escreva o nome."
    )

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if any(nome in texto for nome in NOME_CORRETO):
        await update.message.reply_text(MENSAGEM_CERTA)
    else:
        await update.message.reply_text(MENSAGEM_ERRADA)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", inicio))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
app.run_polling()
