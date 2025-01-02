import discord
import os
import logging

from discord.ext import commands

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
        await self.load_extensions()
        await bot.tree.sync()
 
bot = CardCollectorBot()
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
bot.run(os.environ.get("APIKEY"), log_handler=handler)

