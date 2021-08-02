import random


def randomly_pick_consumable(consumables: list):
    """
    Randomly picks out a consumable
    """

    random_index = random.randint(0, len(consumables) - 1)
    return consumables[random_index]
