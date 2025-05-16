
🤖 A Telegram bot for sending messages to contacts

This bot allows you to send messages to a list of contacts (via chat_id or username). Built with Python and the python-telegram-bot library.

🔧 Installation & Setup
1. Prerequisites
Python 3.8+

python-telegram-bot library (v20.x or higher)

A Telegram bot token (obtained from @BotFather)

2. Installation
Clone this repository:

bash
git clone https://github.com/Uxxxsr1/Auto-account-surrender.git
cd telegram-message-bot
Install dependencies:

bash
pip install python-telegram-bot
Add your bot token:

Open config.py (or the main script) and replace "YOUR_TELEGRAM_BOT_TOKEN" with your actual bot token.

🚀 Usage
1. Start the Bot
Run the bot:

bash
python telegram-bot.py
2. Available Commands
/start - Welcome message and instructions.

/id - Get the current chat ID.

/send <contact1>,<contact2> <message> - Send a message to specified contacts.
Example:

/send 123456789,@example Hello, world!
3. How It Works
The bot can only message users who have started a chat with it or added it to contacts.

For groups/channels, ensure the bot has admin permissions.

📂 Project Structure
telegram-message-bot/
├── telegram-bot.py            # Main bot script
├── config.db         # Configuration (e.g., bot token)
└── README.md         # This file
⚠️ Limitations
Telegram restricts bots from messaging users who haven't interacted with them first.

Avoid spamming to prevent bot bans.

📜 License
MIT License. See LICENSE for details.

📬 Contact
For questions or improvements, open an issue or contact telegram @gimranov_timur.
