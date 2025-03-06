# Discord Chess Bot 🤖♟️

Welcome to the **Discord Chess Bot**! Ever wanted to challenge your friends to a game of chess, but too lazy to set up a board? Well, now you can play chess directly in Discord, without moving a single piece! 🧠💥

This bot allows users to challenge each other to a game of chess, accept/decline challenges, and track their game state with fancy chessboard displays. Prepare for epic duels 🏆, unexpected checkmates 👑, and friendly resignations 🏳️!

## Features

- **Challenge your friends** 🕹️: Send a challenge to a friend to start a game.
- **Accept or Decline** ✅❌: The person who is challenged can accept or decline the game.
- **Chess game state management**: Keep track of your game state, and let the bot display the chessboard in all its Unicode glory! ♟️
- **Resign from the game** 🏳️: Don't want to play anymore? Resign and admit defeat in style!

## Commands 📜

### `/challenge <@opponent>`
Challenge someone to a chess game! Be careful, they might beat you. 😏

- **Example**: `/challenge @Player2`

### `/resign`
Resign from the current game. It’s okay to admit defeat — we all have bad days! 🏳️

- **Example**: `/resign`

## Requirements 💻

Before you begin, make sure you have the following:

- Python 3.8+ 🐍
- The `discord.py` library to make the magic happen ✨
- The `python-chess` library to keep track of the board 🎯
- A `.env` file with your bot’s **secret token** (no peeking! 🕵️)

## Setup ⚙️

Here’s how to set up the bot and get it running:

1. **Clone the repository** to your local machine:

   ```bash
   git clone https://github.com/your-username/discord-chess-bot.git
   cd discord-chess-bot
2.**Install the required dependencies:**

bash
Copy
pip install -r requirements.txt
3.**Create a .env file in the root directory of the project and add your Discord bot token:**

ini
Copy
DISCORD_BOT_TOKEN=your-bot-token-here
4.**Run the bot:**

bash
Copy
python bot.py
Now, go to your Discord server, and start challenging everyone to a game! 🥳

Libraries Used 📚
discord.py - The powerhouse that brings the bot to life! ⚡
python-chess - The chess wizardry behind the scenes that keeps the board intact! 🧙‍♂️


**Now, go ahead and start playing chess! And remember, checkmate is only a few moves away... 😉♟️**
