import discord

from discord.ext import commands
from util.roller import RollerUtils
from util.card import CardType, CardUtils
from PIL import Image

import io

class Roll(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(name= 'roll', description = 'Roll for a card')
    async def roll(self, interaction: discord.Interaction) -> None:

        card = RollerUtils.gen_card()
        color = discord.Color.light_grey()

        with Image.open(card.image_path).convert("RGBA") as image:
            card.image = image
            match card.card_type:
                case CardType.LOWQ:
                    image = CardImageUtils.low_quality(image)
                    color = discord.Color.dark_grey()
                case CardType.FOIL:
                    image = CardImageUtils.foil(image)
                    color = discord.Color.blurple()
                case CardType.HOLO:
                    image = CardImageUtils.holo(image)
                    color = discord.Color.green()
                case CardType.SHINY:
                    image = CardImageUtils.shiny(image)
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
