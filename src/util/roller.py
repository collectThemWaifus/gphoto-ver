from util.card import Card, CardType
from random import randint
from people.cards import all_people_cards, all_special_cards


def gen_card() -> Card:
    """
    method to be called when looking to generate a new card
    """

    is_special = randint(0, 1000) == 69
    card = all_special_cards[randint(0, len(all_special_cards) - 1)] if is_special else all_people_cards[randint(0, len(all_people_cards) - 1)]
    return add_modifier(card)

def add_modifier(card: Card) -> Card:
    n = randint(0, 1000)

    if n == 1000: card.card_type = CardType.SHINY
    elif n > 990: card.card_type = CardType.HOLO
    elif n > 900: card.card_type = CardType.FOIL
    elif n > 700: card.card_type = CardType.LOWQ
    else: card.card_type = CardType.NONE

    return card




