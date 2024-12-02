from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import re



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    match = re.search(r'\d+(\.\d+)?', user_message)

    if match:
        sum1 = match.group()
        await update.message.reply_text(f"Я нашел число: {sum1}")
    else:
        await update.message.reply_text("Я не нашел числа в вашем сообщении. Попробуйте еще раз!")



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Отправь мне сообщение с числом, и я найду его."
    )


def main():
    # Создаем приложение
    app = Application.builder().token("7661110067:AAFO7UqNFWS33VjcOWWTdzOvx_dZrJuBwGg").build()

    # Обработчики команд и сообщений
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    app.run_polling()


if __name__ == "__main__":
    main()
