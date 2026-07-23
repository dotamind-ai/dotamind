from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)

from config import BOT_TOKEN

from handlers import start_command

from analyzer_handler import analyze_match

from callback_handler import player_selected



def main():

    if not BOT_TOKEN:

        print(
            "Ошибка: BOT_TOKEN не найден"
        )

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



    # Сообщения пользователя:
    # Match ID или номер игрока

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            analyze_match
        )
    )



    # Нажатие кнопок игроков

    app.add_handler(
        CallbackQueryHandler(
            player_selected
        )
    )



    print(
        "🤖 Dotamind AI Bot запущен"
    )



    app.run_polling()



if __name__ == "__main__":

    main()