from os import listdir, environ

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

def generate_all_people_cards () -> [Card]:
    list_of_cards = []

    list_of_people = listdir('src/images')
    for person in list_of_people:
        try:
            list_of_photos = listdir(f'src/images/{person}')
            if len(list_of_photos) == 1:
                # If in production, raise an error about no photos
                if environ.get('PROD'):
                    raise Exception('Missing Photos Error', f'No Photos detected in {person}\'s folder!')
                else:
                    print('Info: Missing Photos, Ignoring... adding test photo')
                    list_of_cards.append(Card(person, f'src/images/a.webp'))
            else:
                for funnyEpithet in list_of_photos:
                    list_of_cards.append(Card(person, f'src/images/{person}/{funnyEpithet}'))
        except NotADirectoryError:
            pass
    return list_of_cards

all_people_cards = generate_all_people_cards()
print(all_people_cards)

all_special_cards = [
    Card('Devious Sangmin', 'src/images/a.webp'),
    Card('Devious Neil', 'src/images/a.webp')
]
