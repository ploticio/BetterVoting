import discord
from discord.ext import commands
from discord import app_commands

class Voting(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command()
    async def hello(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="Hello!")

async def setup(bot: commands.Bot):
    await bot.add_cog(Voting(bot))