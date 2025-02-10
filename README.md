# 🤖 Telegram Bot with Google Gemini AI

This is a **Telegram chatbot** that responds to user messages using **Google Gemini AI**. It utilizes the `python-telegram-bot` library for handling Telegram messages and `google-generativeai` for AI responses.

## 🚀 Features
- **AI-Powered Chat**: Uses Google Gemini API for generating responses.
- **Secure API Keys**: Uses `.env` file to store sensitive credentials.
- **Easy Deployment**: Simple setup and execution.

---

## 📌 Prerequisites

Before running the bot, ensure you have:
- Python **3.8+** installed
- A Telegram bot token from [BotFather](https://t.me/BotFather)
- A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)

---

## 🔧 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/telegram-gemini-bot.git
cd telegram-gemini-bot
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Create a `.env` File
Create a `.env` file in the project root and add:
```ini
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 📝 Usage

### 1️⃣ Run the Bot
```sh
python telegram_gemini_bot.py
```

### 2️⃣ Interact with the Bot
- **Start the bot**: Send `/start`
- **Ask any question**, and the bot will respond using Gemini AI.

---

## 🛠️ Code Structure

### `telegram_gemini_bot.py`
- **Loads API keys** from `.env`
- **Handles `/start` command**
- **Processes user messages** using Gemini AI

```python
import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize AI model
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! Ask me anything, and I'll reply using Gemini AI 🤖")

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = model.generate_content(user_message)
    ai_reply = response.text.strip() if response else "Sorry, I couldn't generate a response."
    await update.message.reply_text(ai_reply)

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
```

---

## 🚀 Deployment on Render

1️⃣ Create a **new repository** on GitHub and push your project.
```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/telegram-gemini-bot.git
git push -u origin main
```

2️⃣ Go to [Render](https://render.com/) and **create a new web service**.

3️⃣ **Connect GitHub Repo** → **Select your repository**.

4️⃣ Set environment variables in **Render Settings**:
   - `TELEGRAM_BOT_TOKEN` → Your bot token
   - `GEMINI_API_KEY` → Your Gemini API key

5️⃣ Set the **Start Command** to:
```sh
python telegram_gemini_bot.py
```

6️⃣ Click **Deploy**! 🚀

---

## 🛠️ Troubleshooting

- **Bot Not Responding?**
  - Ensure your bot is running in the terminal.
  - Check if the `TELEGRAM_BOT_TOKEN` is correct.
  - Verify that your **Google Gemini API key** is valid.

- **Module Not Found Error?**
  - Run `pip install -r requirements.txt` again.

---

## 📜 License
This project is licensed under the MIT License.

---

## 🌟 Contributing
Feel free to fork and contribute by submitting a pull request!

---

## ✨ Author
Developed by **Jagdish Prajapti**.

📧 Contact: your.jagdishprajapti573@gmail.com  
🔗 GitHub: [yourusername](https://github.com/yourusername)  

