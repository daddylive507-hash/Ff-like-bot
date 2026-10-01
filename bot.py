import os
import requests
import time
import telebot

# Environment variable se token load hoga
TOKEN = os.getenv("TELEGRAM_TOKEN")
API_URL = "https://example.com" # Dummy link

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "⚡ **Free Fire Auto-Like Bot Active!**\n\nUID message karein, bot automatic likes bhejna shuru kar dega!")

@bot.message_handler(func=lambda message: True)
def handle_uid(message):
    uid = message.text.strip()
    
    if not uid.isdigit() or len(uid) < 5:
        bot.reply_to(message, "❌ Kripya ek valid Free Fire UID bhejein.")
        return
        
    bot.reply_to(message, f"🚀 UID: {uid} par Auto-Like Process shuru ho gaya hai...")
    
    for i in range(1, 11): 
        try:
            payload = {"uid": uid, "count": "10"}
            requests.get(API_URL, params=payload, timeout=10)
        except:
            pass
        time.sleep(4) 
        
    bot.reply_to(message, f"✅ UID: {uid} par Auto-Like round poora ho gaya!")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
