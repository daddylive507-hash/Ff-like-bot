import os
import requests
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")
API_URL = "https://example.com" 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("⚡ **Free Fire Auto-Like Bot Active!**\n\nUID message karein, bot automatic likes bhejna shuru kar dega!")

async def handle_uid(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid = update.message.text.strip()
    if not uid.isdigit() or len(uid) < 5:
        await update.message.reply_text("❌ Kripya ek valid Free Fire UID bhejein.")
        return
        
    await update.message.reply_text(f"🚀 UID: {uid} par Auto-Like Process shuru ho gaya hai...")
    
    for i in range(1, 11): 
        try:
            payload = {"uid": uid, "count": "10"}
            requests.get(API_URL, params=payload, timeout=10)
        except:
            pass
        await asyncio.sleep(4) 
        
    await update.message.reply_text(f"✅ UID: {uid} par Auto-Like round poora ho gaya!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_uid))
    
    print("Bot is running...")
    app.run_polling(close_loop=False)
