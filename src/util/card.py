import enum
from PIL import Image, ImageEnhance, ImageFile, ImageDraw, ImageOps
import numpy as np

class CardType(enum.Enum): 
    NONE = 'Normal'
    LOWQ = 'Low Quality'
    FOIL = 'Foil'
    HOLO = 'Holographic'
    SHINY = 'Shiny'

class Card:

    __slots__ = ['name', 'card_type', 'image_path', 'image']

    def __init__(self, name:str="Unknown", image_path:str='') -> None: # TODO change default image path to some error image
        """
        name: name of the card\n
        card_type: foil, holo... etc\n
        image_path: path to card's image\n
        """
        self.name = name
        self.image_path = image_path
        self.card_type = CardType.NONE
        self.image = None

    def __str__(self) -> str:
        return f'{self.card_type.value} {self.name}'

class CardUtils:

    @staticmethod
    def holo(image: ImageFile) -> ImageFile:

        """
        Adds the holo effect for a card's image
        """

        width, height = image.size
        gradient = Image.new("RGBA", (width, height))
        pixels = gradient.load()
        for y in range(height):
            for x in range(width):
                r = int(128 + 127 * np.sin(2 * np.pi * x / width))
                g = int(128 + 127 * np.sin(2 * np.pi * y / height))
                b = int(128 + 127 * np.sin(2 * np.pi * (x + y) / (width + height)))
                pixels[x, y] = (r, g, b, 128)
        blended = Image.alpha_composite(image, gradient)
        enhancer = ImageEnhance.Color(blended)

        return enhancer.enhance(1.2)

    @staticmethod
    def foil(image: ImageFile) -> ImageFile: # TODO
        """
        Adds the foil effect for a card's image
        """
        
        image = image.convert("RGBA")
        width, height = image.size
        shiny_layer = Image.new("RGBA", (width, height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(shiny_layer)
        for i in range(height):
            alpha = int(100 * (1 - i / height))
            draw.line((0, i, width, i), fill=(85, 57, 204, alpha))
        shiny_image = Image.alpha_composite(image, shiny_layer)
        enhancer = ImageEnhance.Brightness(shiny_image)
        shiny_image = enhancer.enhance(1.5)

        return shiny_image

    @staticmethod
    def low_quality(image: ImageFile, pixel_size: int = 10) -> ImageFile:
        """
        Adds the low quality effect for a card's image
        """
        
        width, height = image.size
        small_width = max(1, width // pixel_size)
        small_height = max(1, height // pixel_size)
        small_image = image.resize((small_width, small_height), Image.NEAREST)

        return small_image.resize((width, height), Image.NEAREST)

    @staticmethod
    def shiny(image: ImageFile) -> ImageFile:
        """
        Adds the shiny effect for a card's image
        """

        r, g, b, a = image.split()
        inverted_rgb = ImageOps.invert(Image.merge("RGB", (r, g, b)))
        
        return Image.merge("RGBA", (*inverted_rgb.split(), a))


