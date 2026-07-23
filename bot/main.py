from telegram.ext import (
    Application,
    CommandHandler
)

from config import BOT_TOKEN
from handlers import start_command
from analyzer_handler import analyze_match


def main():

    app = Application.builder() \
        .token(BOT_TOKEN) \
        .build()

    app.add_handler(
        CommandHandler(
            "start",
            start_command
        )
    )

    print("Dotamind bot started")

    app.run_polling()


if __name__ == "__main__":
    main()