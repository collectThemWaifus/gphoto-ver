from util.card import Card, CardType
import discord
from db.db import db_cursor

class InventoryUtils:
    """
    A class of inventory utilities
    """

    @staticmethod
    def add(user: discord.User, card: Card) -> bool:
        """
        user: discord user
        card: card to be added

        returns: True on duplicate, False on unique
        """

        user_id = str(user.id)
        found_duplicate = False
        points = 0

        with db_cursor() as cur:
            cur.execute("INSERT INTO users (id, points, duplicates, achievements) VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING",
                (user_id, 0, 0, 0))
            
            # check duplicates 
            cur.execute("SELECT 1 FROM cards WHERE name = %s AND owner_id = %s AND type = %s",
                (card.name, user_id, card.card_type))
            
            if cur.fetchone():
                cur.execute("UPDATE users SET duplicates = duplicates + 1 WHERE id = %s",
                (user_id, ))
                found_duplicate = True
            
            # For now: SHINY = 100, HOLO = 20, FOIL = 10, NONE = 1, LOWQ = 0
            match card.card_type:
                case CardType.SHINY:
                    points = 100
                case CardType.HOLO:
                    points = 20
                case CardType.FOIL:
                    points = 10
                case CardType.NONE:
                    points = 1
            cur.execute("UPDATE users SET points = points + %s WHERE id = %s",
                (points, user_id))

            # insert
            cur.execute("INSERT INTO cards (name, type, owner_id) VALUES (%s, %s, %s)",
                (card.name, card.card_type, user_id))
        
        return found_duplicate
            
        

        




