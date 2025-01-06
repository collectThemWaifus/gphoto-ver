import discord

from discord.ext import commands
from util.roller import RollerUtils
from util.card import CardType, CardUtils
from util.inventory import InventoryUtils
from PIL import Image
from io import BytesIO
from random import randint

class Roll(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.sad_messages = [
            "Unlucky!",
            "Better luck next time!",
            "That is unfortunate.",
            "Skull.",
            "Maybe... Don't do that next time."
        ]
        self.happy_messages = [
            "Nice!",
            "Amazing!",
            "Lucky!"
        ]

    @discord.app_commands.command(name= 'roll', description = 'Roll for a card')
    async def roll(self, interaction: discord.Interaction) -> None:

        card = RollerUtils.gen_card()
        color = discord.Color.light_grey()
        duplicate_str = ''
        flavor_text = self.happy_messages[randint(0, len(self.happy_messages) - 1)]

        if InventoryUtils.add(interaction.user, card):
            duplicate_str = '**duplicate** '
            flavor_text = self.sad_messages[randint(0, len(self.sad_messages) - 1)]
            

        with Image.open(card.image_path).convert("RGBA") as image:
            card.image = image
            match card.card_type:
                case CardType.LOWQ:
                    image = CardUtils.low_quality(image)
                    color = discord.Color.dark_grey()
                case CardType.FOIL:
                    image = CardUtils.foil(image)
                    color = discord.Color.blurple()
                case CardType.HOLO:
                    image = CardUtils.holo(image)
                    color = discord.Color.green()
                case CardType.SHINY:
                    image = CardUtils.shiny(image)
                    color = discord.Color.pink()
            buffer = BytesIO()
            image.save(buffer, format="PNG")
            buffer.seek(0)

        file = discord.File(buffer, "card.png")
        
            
        embed = discord.Embed(
            description=f'You just rolled a... {duplicate_str}{card}',
            color=color
        )
        embed.set_image(url="attachment://card.png")
        embed.set_footer(text=flavor_text)
        await interaction.response.send_message(embed=embed, file=file)

async def setup(bot: commands.Bot):
    await bot.add_cog(Roll(bot))
