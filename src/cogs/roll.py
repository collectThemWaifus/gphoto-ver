import discord
from discord.ext import commands
import util.roller as roller

class Roll(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(name= 'roll', description = 'Roll for a card')
    async def roll(self, interaction: discord.Interaction) -> None:
        card = roller.gen_card()

        await interaction.response.send_message(f"You just rolled... {card} Nice!")

async def setup(bot: commands.Bot):
    await bot.add_cog(Roll(bot))
