import google.generativeai as genai
from telegram import Update
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import os
# Replace with your keys
load_dotenv()

# Get API keys from environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# Initialize Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")  

async def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    await update.message.reply_text("Hello! Ask me anything, and I'll reply using  🤖")

async def handle_message(update: Update, context: CallbackContext) -> None:
    """Handle user messages and generate AI responses."""
    user_message    = update.message.text

    try:
        response = model.generate_content(user_message)
        ai_reply = response.text.strip() if response else "Sorry, I couldn't generate a response."
    except Exception as e:
        ai_reply = f"Error: {str(e)}"

    await update.message.reply_text(ai_reply)

def main():
    """Start the bot."""
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
