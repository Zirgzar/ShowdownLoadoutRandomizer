import random


def get_slot_one_weapon(weapons: dict):
    """
    randomly picks out a primary weapon.
    :return: str
    """
    # Remove any "small" or "melee" for slot 1.
    weapons = [x for x in weapons if x.get("size").lower() != "small"]
    weapons = [x for x in weapons if x.get("size").lower() != "melee"]

    # Pick and return a random one, based on how many there are.
    random_index = random.randint(0, len(weapons) - 1)
    return weapons[random_index]


def get_slot_two_weapon(
    weapons: dict, slot_one_weapon_size: str, slot_one_weapon_name: str
):
    """
    randomly picks out a secondary weapon.
    :return: str
    """
    # Remove any weapon that matches the slot one weapon name.
    weapons = [
        x for x in weapons if x.get("name").lower() != slot_one_weapon_name.lower()
    ]
    # Remove any "large" or "melee" found.
    weapons = [x for x in weapons if x.get("size").lower() != "large"]
    weapons = [x for x in weapons if x.get("size").lower() != "melee"]

    # Remove "medium" if initial slot one weapon is "large".
    # Force "medium" if slot one weapon is "medium".
    if slot_one_weapon_size.lower() == "large":
        weapons = [x for x in weapons if x.get("size").lower() != "medium"]
    else:
        weapons = [x for x in weapons if x.get("size").lower() == "medium"]

    # Pick and return a random one, based on how many there are.
    random_index = random.randint(0, len(weapons) - 1)
    return weapons[random_index]


def get_melee_weapon(weapons: dict):
    """
    randomly picks out a melee weapon
    """
    # Remove any weapon that is not a "melee" size.
    weapons = [x for x in weapons if x.get("size").lower() == "melee"]
    random_index = random.randint(0, len(weapons) - 1)
    return weapons[random_index]
