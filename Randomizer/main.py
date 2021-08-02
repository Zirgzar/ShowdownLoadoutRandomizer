import random_weapons
import random_tools
import random_consumable
import json
import sys


def player_level():
    # Get player level to limit random items to ones that are available
    return int(input("Enter your bloodline level: "))


def reroll():
    # Reroll if don't have the advanced items or don't like loadout
    answer = input("Would you like to reroll? Y/N: ").lower()
    if answer == "y":
        return start()
    else:
        sys.exit()


def start():
    # Load in the config data..
    weapons = json.loads(open("weapons.json").read())
    tools = json.loads(open("tools.json").read())
    consumables = json.loads(open("consumables.json").read())
    playerLevel = player_level()
    weapons = [x for x in weapons if x.get("level") <= playerLevel]
    tools = [x for x in tools if x.get("level") <= playerLevel]
    consumables = [x for x in consumables if x.get("level") <= playerLevel]

    # Build the loadout..
    loadout = dict()

    # Start with weapons..
    loadout = build_weapons(loadout=loadout, weapons=weapons)

    # Then build tools..
    loadout = build_tools(loadout=loadout, weapons=weapons, tools=tools)

    # Next, consumables..
    loadout = build_consumables(loadout=loadout, consumables=consumables)
    # Print the loadout
    print(json.dumps(loadout, indent=4))

    return reroll()


def build_weapons(loadout: dict, weapons: list):
    # Pick the weapons..
    loadout["slot_one_weapon"] = random_weapons.get_slot_one_weapon(weapons=weapons)
    loadout["slot_two_weapon"] = random_weapons.get_slot_two_weapon(
        weapons=weapons,
        slot_one_weapon_size=loadout["slot_one_weapon"].get("size"),
        slot_one_weapon_name=loadout["slot_one_weapon"].get("name"),
    )
    return loadout


def build_tools(loadout: dict, weapons: list, tools: list):
    # Pick the tools..
    loadout["slot_one_tool"] = random_weapons.get_melee_weapon(weapons=weapons)
    loadout["slot_two_tool"] = {"name": "First Aid Kit", "cost": "30"}
    loadout["slot_three_tool"] = random_tools.randomly_pick_tools(tools=tools)
    # Remove the tool it selected for the first slot.
    to_pop_index = tools.index(loadout.get("slot_three_tool"))
    tools.pop(to_pop_index)
    loadout["slot_four_tool"] = random_tools.randomly_pick_tools(tools=tools)
    return loadout


def build_consumables(loadout: dict, consumables: list):
    # Pick Consumables..
    loadout["slot_one_consumable"] = random_consumable.randomly_pick_consumable(
        consumables=consumables
    )
    loadout["slot_two_consumable"] = random_consumable.randomly_pick_consumable(
        consumables=consumables
    )
    loadout["slot_three_consumable"] = random_consumable.randomly_pick_consumable(
        consumables=consumables
    )
    loadout["slot_four_consumable"] = random_consumable.randomly_pick_consumable(
        consumables=consumables
    )
    return loadout


if __name__ in "__main__":
    start()
