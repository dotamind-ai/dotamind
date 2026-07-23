from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)

from config import BOT_TOKEN
from handlers import start_command
from analyzer_handler import analyze_match


def main():

    if not BOT_TOKEN:
        print("Ошибка: BOT_TOKEN не найден")
        return

    app = Application.builder() \
        .token(BOT_TOKEN) \
        .build()


    # Команда /start
    app.add_handler(
        CommandHandler(
            "start",
            start_command
        )
    )


    # Любой текст после /start
    # будет отправляться в анализатор
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            analyze_match
        )
    )


    print("🤖 Dotamind AI Bot запущен")


    # Запуск ожидания сообщений
    app.run_polling()


if __name__ == "__main__":
    main()