import discord
from discord.ext import commands
import settings

def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"{bot.user} is now running")

        # for cogfile in settings.COGS_DIR.glob("*.py"):
        #     if cogfile.name != "__init__.py":
        #         await bot.load_extension(f"cogs.{cogfile.name[:-3]}")

        await bot.load_extension("cogs.voting")
        synced = await bot.tree.sync()
        print(f"CMDs synced: {len(synced)}")


    @bot.command(aliases=["p"], hidden=True)
    async def ping(ctx):
        await ctx.send(f"{round(bot.latency * 1000, 1)}ms")


    async def is_developer(ctx):
        return ctx.author.id == 147917812482965504


    @bot.command(hidden=True)
    @commands.check(is_developer)
    async def load(ctx, cog: str):
        await bot.load_extension(f"cogs.{cog}")


    @bot.command(hidden=True)
    @commands.check(is_developer)
    async def unload(ctx, cog: str):
        await bot.unload_extension(f"cogs.{cog}")


    @bot.command(hidden=True)
    @commands.check(is_developer)
    async def reload(ctx, cog: str):
        await bot.reload_extension(f"cogs.{cog}")


    bot.run(settings.TOKEN)