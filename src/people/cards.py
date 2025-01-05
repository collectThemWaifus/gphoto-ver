from util.card import Card

people_list = ["Sangmin", "Neil", "Rishabh", "Ernest", "Brian",
            "Umar", "Frank", "Erick", "Chris", "Dylan",
            "Aaron", "Ryan", "David McSwain", "Jaydon Malin", "Cohen",
            "Ronak","Tarik", "Alex Lopez", "Ken", "Vihari"]

people = { # add list of their cards here as Card objects
    "Sangmin": [Card('Sangmin', 'src/images/a.webp')],
    "Neil": [Card('Neil', 'src/images/a.webp')],
}

special_people = { #list of special / rare cards for each person
    "Sangmin": [Card('Devious Sangmin', 'src/images/a.webp')],
    "Neil": [Card('Devious Neil', 'src/images/a.webp')],
}

all_people_cards = [
    Card('Sangmin', 'src/images/a.webp'),
    Card('Neil', 'src/images/a.webp')
]

all_special_cards = [
    Card('Devious Sangmin', 'src/images/a.webp'),
    Card('Devious Neil', 'src/images/a.webp')
]