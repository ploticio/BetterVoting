import discord
from discord.ext import commands
from typing import Optional, Literal
import settings

def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready() -> None:
        print(f"{bot.user} is now running")

    @bot.event
    async def setup_hook() -> None:
        for cogfile in settings.COGS_DIR.glob("*.py"):
            if cogfile.name != "__init__.py":
                await bot.load_extension(f"cogs.{cogfile.name[:-3]}")


    @bot.command(aliases=["p"], hidden=True)
    async def ping(ctx: commands.Context) -> None:
        await ctx.send(f"{round(bot.latency * 1000, 1)}ms")


    async def is_developer(ctx: commands.Context) -> None:
        return ctx.author.id == 147917812482965504


    @bot.command(hidden=True)
    @commands.check(is_developer)
    async def load(ctx: commands.Context, cog: str) -> None: 
        await bot.load_extension(f"cogs.{cog}")


    @bot.command(hidden=True)
    @commands.check(is_developer)
    async def unload(ctx: commands.Context, cog: str) -> None:
        await bot.unload_extension(f"cogs.{cog}")


    @bot.command(hidden=True)
    @commands.check(is_developer)
    async def reload(ctx: commands.Context, cog: str) -> None:
        await bot.reload_extension(f"cogs.{cog}")

    @bot.command(hidden=True)
    @commands.check(is_developer)
    async def sync(ctx: commands.Context, opt: Optional[Literal["*", "^", "~"]] = None):
        if opt == "*":
            synced = await bot.tree.sync()
        elif opt == "^":
            bot.tree.clear_commands(guild=ctx.guild)
            await bot.tree.sync(guild=ctx.guild)
            synced = []
        elif opt == "~":
            synced = await bot.tree.sync(guild=ctx.guild)
        else:
            bot.tree.copy_global_to(guild=ctx.guild)
            synced = await bot.tree.sync(guild=ctx.guild)
        
        await ctx.send(f"Synced {len(synced)} commands {'globally' if opt == '*' else 'locally'}")


    bot.run(settings.TOKEN)