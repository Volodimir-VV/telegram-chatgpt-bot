import logging
import openai
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

openai.api_key = os.environ["OPENAI_API_KEY"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("�����! � AI-���. ������ ��� ����-��!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "�� ������ ���������� �������."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message.content
        await update.message.reply_text(reply)
    except Exception as e:
        await update.message.reply_text("��, ������� ������� ??")

if __name__ == "__main__":
    TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("��� ��������!")
    app.run_polling()