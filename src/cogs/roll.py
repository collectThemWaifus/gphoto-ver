import discord
import io
from discord.ext import commands
import util.roller as roller
import util.image as modifier
from util.card import CardType
from PIL import Image

class Roll(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(name= 'roll', description = 'Roll for a card')
    async def roll(self, interaction: discord.Interaction) -> None:

        card = roller.gen_card()
        color = discord.Color.light_grey()

        with Image.open(card.image_path).convert("RGBA") as image:
            card.image = image
            match card.card_type:
                case CardType.LOWQ:
                    image = modifier.low_quality(image)
                    color = discord.Color.dark_grey()
                case CardType.FOIL:
                    image = modifier.foil(image)
                    color = discord.Color.blue()
                case CardType.HOLO:
                    image = modifier.holo(image)
                    color = discord.Color.green()
                case CardType.SHINY:
                    image = modifier.shiny(image)
                    color = discord.Color.pink()
            buffer = io.BytesIO()
            image.save(buffer, format="PNG")
            buffer.seek(0)

        file = discord.File(buffer, "card.png")
            
        embed = discord.Embed(
            description=f'You just rolled a... {card} Nice!',
            color=color
        )
        embed.set_image(url="attachment://card.png")
        await interaction.response.send_message(embed=embed, file=file)

async def setup(bot: commands.Bot):
    await bot.add_cog(Roll(bot))
