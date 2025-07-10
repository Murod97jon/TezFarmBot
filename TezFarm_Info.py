from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
print("Python fayli ishlayapti")
TOKEN = "7574390957:AAERXidjGgTvqyFPBdWzEXv7IeL5DwGpZVA"
malumotlar = {"tirozin": "L-tirozin suvda yomon eriydi, ishqoriy eritmalarda yaxshi eriydi.", "tsistein": "L-tsistein suvda yaxshi eriydi, spirtlarda yomon eriydi.", "aspartat": "L-asparagin kislotasi ~0.5 g/100 ml suvda eriydi. Erish harorati ~270°C.",}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Men TezFarm_Info botman Substansiya yoki texnologiya haqida so'rang.")

async def subs(update:Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if args:
        nom = args [0].lower()
        info = malumotlar.get(nom, "Bu substansiya haqida maʼlumot topilmadi.")
        await update.message.reply_text(info)
    else:
        await update.message.reply_text("Iltomos substansiya nomini yozing.")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("subs", subs))
    print("Bot ishga tushdi...")
    await app.run_polling()

if __name__ == "__main__":
    import nest_asyncio
    import asyncio

    nest_asyncio.apply()
    asyncio.run(main())