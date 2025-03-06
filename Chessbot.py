import discord
import chess
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
games = {}  # Store games as {player_id: chess.Board()}
pending_challenges = {}  # Store pending challenges {challenger_id: opponent_id}


class ChallengeView(discord.ui.View):
    """A view with Accept/Decline buttons for chess challenges."""

    def __init__(self, challenger, opponent):
        super().__init__()
        self.challenger = challenger
        self.opponent = opponent

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.success)
    
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.opponent:
            await interaction.response.send_message("❌ Only the challenged player can accept!", ephemeral=True)
            return

        # Start the game
        games[self.challenger.id] = chess.Board()
        games[self.opponent.id] = games[self.challenger.id]  # Both share the same board

        await interaction.response.send_message(f"✅ {self.opponent.mention} accepted the challenge!\nGame started!\n{display_board(games[self.challenger.id])}")
        del pending_challenges[self.challenger.id]  # Remove pending challenge

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.danger)
    async def decline(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.opponent:
            await interaction.response.send_message("❌ Only the challenged player can decline!", ephemeral=True)
            return

        await interaction.response.send_message(f"🚫 {self.opponent.mention} declined the challenge.")
        del pending_challenges[self.challenger.id]  # Remove pending challenge


@bot.tree.command(name="challenge", description="Challenge another user to a chess game.")
async def challenge(interaction: discord.Interaction, opponent: discord.Member):
    """Starts a challenge that must be accepted before the game begins."""

    if interaction.user.id in games or opponent.id in games:
        await interaction.response.send_message("❌ One of you is already in a game!", ephemeral=True)
        return

    if interaction.user.id in pending_challenges:
        await interaction.response.send_message("❌ You already sent a challenge!", ephemeral=True)
        return

    pending_challenges[interaction.user.id] = opponent.id

    view = ChallengeView(interaction.user, opponent)
    await interaction.response.send_message(f"🎯 {interaction.user.mention} challenged {opponent.mention} to a chess game!\n{opponent.mention}, do you accept?", view=view)


def display_board(board):
    """Creates a wide-spaced 8×8 chessboard table with perfectly aligned pieces."""
    PIECES = {
        "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
        "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙",
        ".": " "  # Empty squares as spaces
    }

    board_str = str(board)

    # Replace pieces with Unicode symbols
    for letter, symbol in PIECES.items():
        board_str = board_str.replace(letter, symbol)

    lines = board_str.split("\n")

    result = "```\n        a       b       c       d       e       f       g       h  \n"  # Column labels
    result += "    +-------+-------+-------+-------+-------+-------+-------+-------+\n"  # Table border

    for i, line in enumerate(lines):
        row_pieces = line.split()
        row = " | ".join(f"  {p}  " if p != " " else "     " for p in row_pieces)  # Extra spaces

        result += f" {8 - i}  | {row} |\n"  # Add row labels
        result += "    +--------+--------+--------+--------+-------+--------+--------+--------+\n"  # Table separator

    result += "```"
    return result
@bot.tree.command(name="resign", description="Resign from the current game.")
async def resign(interaction: discord.Interaction):
    """Allows a player to resign and removes the game for both players."""
    
    if interaction.user.id not in games:
        await interaction.response.send_message("❌ You're not in a game!", ephemeral=True)
        return

    # Find the opponent (both players share the same board)
    board = games[interaction.user.id]
    opponent_id = None

    for player_id, game_board in games.items():
        if game_board == board and player_id != interaction.user.id:
            opponent_id = player_id
            break

    # Remove both players from the game
    del games[interaction.user.id]
    if opponent_id:
        del games[opponent_id]

    await interaction.response.send_message(f"🏳 {interaction.user.mention} resigned! Game over.")



bot.run(TOKEN)
