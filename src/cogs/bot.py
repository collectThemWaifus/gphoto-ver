import discord
from discord.ext import commands

class Bot(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print('Bot is online')

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        """
        not sure if we still want this, but leaving it in anyways
        """
        pass

    @discord.app_commands.command(name= 'help', description = 'help command')
    async def help(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Very helpful help message")

async def setup(bot: commands.Bot):
    await bot.add_cog(Bot(bot))
