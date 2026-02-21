import random
import os
from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Get the token from environment variable
TOKEN = "8199719416:AAGxiXB9ex6yEfbjYJnGahSPOymiduVMVYQ"

# --- Predefined random messages ---
MESSAGES = [
    "اخیراً چه چیزی باعث خوشحالی شما شد؟",
    "زندگی متعادل برای شما چه شکلی دارد؟",
    "چقدر ایمان یا باورهای معنوی در زندگی روزمره‌تان نقش دارد؟",
    "یک آخر هفته معمولی شما چه شکلی است؟",
    "زندگی در شهری شلوغ را ترجیح می‌دهید یا جایی آرام‌تر؟",
    "آیا بیشتر اهل برنامه‌ریزی هستید یا اتفاقات را به صورت خودجوش تجربه می‌کنید؟",
    "ترجیح می‌دهید در خانه آشپزی کنید یا بیشتر بیرون غذا بخورید؟",
    "خانواده‌تان در زندگی مشترک آینده شما چه نقشی خواهند داشت؟",
    "برای خوشبختی، چه چیزی در ازدواج برایتان مهم‌ترین است؟",
    "وقتی استرس دارید، بیشتر به چه کاری پناه می‌برید؟",
    "یکی از فیلم‌هایی که باعث شد گریه کنید را نام ببرید.",
    "اگر می‌توانستید یک روز را دوباره تجربه کنید، کدام روز را انتخاب می‌کردید و چرا؟",
    "چه عادتی در زندگی روزمره دارید که فکر می‌کنید شریک آینده باید آن را بداند؟",
    "اگر زندگی شما یک کتاب بود، چه عنوانی برای فصل فعلی انتخاب می‌کردید؟",
    "اگر می‌توانستید یک روز را با شخصیت تاریخی یا معاصر تجربه کنید، چه کسی و چرا؟"
]

# --- Fixed links ---
LINKS = {
    "1": "https://docs.google.com/forms/d/e/1FAIpQLSd6HmzKVZZ4Uk-vPGi9ANfVDcRny8Hp3XoIQ49cUWbkBQFjgg/viewform?usp=header",
    "2": "https://docs.google.com/forms/d/e/1FAIpQLSe04YrCLVaDAkEk3TUHeEUYyN0UVyl9Ef60DaJI5KxbKwPPhQ/viewform?usp=header",
    "3": "https://docs.google.com/forms/d/e/1FAIpQLSdk9PZPQ2uv9CH0FiWXFiHQDFZJxaNwjwSYKE2Qy04C757Imw/viewform?usp=header",
}

# --- Command Handlers ---
async def random_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random message"""
    await update.message.reply_text(random.choice(MESSAGES))

async def send_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a fixed link based on command"""
    cmd = update.message.text.replace("/", "")
    if cmd in LINKS:
        await update.message.reply_text(LINKS[cmd])

# --- Main bot ---
def main():
    # Build the application
    app = ApplicationBuilder().token(TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("random", random_message))
    for key in LINKS.keys():
        app.add_handler(CommandHandler(key, send_link))

    # Register commands with Telegram so they show in `/` menu
    # app.bot.set_my_commands([
    #     BotCommand("random", "Send a random message"),
    #     BotCommand("1", "Send Link 1"),
    #     BotCommand("2", "Send Link 2"),
    #     BotCommand("3", "Send Link 3")
    # ])

    print("Bot is running...")
    # Run polling directly (no asyncio.run)
    app.run_polling()

# Run bot
if __name__ == "__main__":
    main()
