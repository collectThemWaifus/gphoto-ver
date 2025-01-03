import discord
import os

from discord.ext import commands
from db import db

class CardCollectorBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned_or('\0'),
            description='Card collection bot for sagg.in server',
            intents=discord.Intents.all(),
            application_id = int(os.getenv("APPLICATIONID")))
        
    async def load_extensions(self) -> None: 
        for filename in os.listdir("src/cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")

    async def setup_hook(self) -> None:
        self.remove_command('help')
        db.setup()
        await self.load_extensions()
        await bot.tree.sync()
 
bot = CardCollectorBot()
bot.run(os.getenv("APIKEY"))

