import random


def randomly_pick_tools(tools: list):
    """
    Randomly picks out a tool
    """
    random_index = random.randint(0, len(tools) - 1)
    return tools[random_index]
