from PIL import Image, ImageEnhance, ImageFile
import numpy as np

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
    return enhancer.enhance(1.5)

def foil(image: ImageFile) -> ImageFile: # TODO
    return image

def low_quality(image: ImageFile) -> ImageFile:
    return image

def shiny(image: ImageFile) -> ImageFile:
    return image




