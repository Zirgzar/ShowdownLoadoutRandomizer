import random
from player_level import playerLevel


def randomly_pick_tools(tools: list):
    """
    Randomly picks out a tool
    """
    # Get only tools player has level for
    tools = [x for x in tools if x.get("level") <= playerLevel]
    random_index = random.randint(0, len(tools) - 1)
    return tools[random_index]
