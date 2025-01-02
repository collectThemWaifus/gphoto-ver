import enum

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


