from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Application
import logging

# Настройка логгирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # Замените на ваш токен

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Я бот для отправки сообщений. Используй /send.")

async def send_message(update: Update, context: CallbackContext):
    try:
        args = update.message.text.split(' ', 2)
        if len(args) < 3:
            await update.message.reply_text("Формат: /send номер1,номер2 текст")
            return

        contacts = args[1].split(',')
        message_text = args[2]

        for contact in contacts:
            try:
                await context.bot.send_message(chat_id=contact, text=message_text)
                await update.message.reply_text(f"Отправлено {contact} ✅")
            except Exception as e:
                await update.message.reply_text(f"Ошибка для {contact}: {e}")

    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")

def main():
    # Создаем экземпляр Application
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("send", send_message))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()