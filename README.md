Telegram Translator Bot

A multilingual Telegram bot built with Python that helps users translate words and sentences between Uzbek, Turkish, and English. It uses the `translators` library to access Google translation functionality.

Features

- Translate words and sentences
- Support for Uzbek, Turkish, and English
- Translation through a Telegram bot interface
- Integration with the `translators` library
- Secure bot token management using `python-dotenv`

Technologies Used

- Python
- pyTelegramBotAPI
- translators
- python-dotenv

Configuration

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:

   ```env
   TOKEN=your_telegram_bot_token_here
   ```

5. Load the bot token using `python-dotenv`.
6. Run the Python script and open the bot in Telegram.

Environment Variables

The Telegram bot token is stored in `.env` and loaded at runtime. The actual token should never be committed to GitHub.

Purpose

This project demonstrates Telegram bot development, multilingual text processing, and the use of a translation library to provide translation functionality through a chat interface.