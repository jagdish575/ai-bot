import asyncio
import threading
import google.generativeai as genai
from telegram import Update
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from fastapi import FastAPI

import os

# Load environment variables
load_dotenv()

# Get API keys from environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini AI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Initialize FastAPI
app = FastAPI()

# Telegram bot application
telegram_app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Define bot commands
async def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    await update.message.reply_text("Hello! Ask me anything, and I'll reply using 🤖")

async def handle_message(update: Update, context: CallbackContext) -> None:
    """Handle user messages and generate AI responses."""
    user_message = update.message.text

    try:
        response = model.generate_content(user_message)
        ai_reply = response.text.strip() if response else "Sorry, I couldn't generate a response."
    except Exception as e:
        ai_reply = f"Error: {str(e)}"

    await update.message.reply_text(ai_reply)

# Add handlers
telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Background task to keep bot running
def run_telegram_bot():
    """Create a new event loop and run the bot in it."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    print("🤖 Bot is running...")
    loop.run_until_complete(telegram_app.run_polling())

@app.on_event("startup")
async def start_bot():
    """Start the bot when the FastAPI server starts."""
    thread = threading.Thread(target=run_telegram_bot, daemon=True)
    thread.start()

@app.get("/")
async def root():
    """Root endpoint to check if the server is running."""
    return {"message": "Telegram bot is running with FastAPI"}
