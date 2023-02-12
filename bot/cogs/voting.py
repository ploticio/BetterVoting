import discord
from discord.ext import commands
from discord import app_commands

class Voting(commands.GroupCog, name="vote"):
    
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    @app_commands.command(name="plurality", description="Plurality Voting: Candidates with most votes wins. (May result in low voter satisfaction)")
    async def plurality(self, interaction: discord.Interaction):
        await interaction.response.send_message("Plurality Vote")

    @app_commands.command(name="ranked", description="Ranked Choice Voting: Voters rank candidates by preference")
    async def rcv(self, interaction: discord.Interaction):
        await interaction.response.send_message("Ranked Choice Vote")

    @app_commands.command(name="star", description="STAR Voting: (Recommended for highest voter satisfaction)")
    async def star(self, interaction: discord.Interaction):
        await interaction.response.send_message("Star Vote")

async def setup(bot: commands.Bot):
    await bot.add_cog(Voting(bot))