import random
from player_level import playerLevel


def randomly_pick_consumable(consumables: list):
    """
    Randomly picks out a consumable
    """
    # Get only consumables player has level for
    consumables = [x for x in consumables if x.get("level") <= playerLevel]
    random_index = random.randint(0, len(consumables) - 1)
    return consumables[random_index]
