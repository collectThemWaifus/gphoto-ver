from util.card import Card, CardType
from random import randint
from people.cards import people, special_people, people_list


def gen_card() -> Card:
    """
    method to be called when looking to generate a new card
    """

    is_special = randint(0, 1000) == 69
    person = people[people_list[randint(0, len(people) - 1)]] if not is_special else special_people[people_list[randint(0, len(special_people) - 1)]]
    card = person[randint(0, len(person) - 1)]
    return add_modifier(card)

def add_modifier(card: Card) -> Card:
    n = randint(0, 1000)

    if n == 1000: card.card_type = CardType.SHINY
    elif n > 990: card.card_type = CardType.HOLO
    elif n > 900: card.card_type = CardType.FOIL
    elif n > 700: card.card_type = CardType.LOWQ
    else: card.card_type = CardType.NONE

    return card




