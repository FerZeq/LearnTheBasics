def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    final: dict[str, int] = {}
    if ("gold_ingots" not in purse) or (purse["gold_ingots"] + 1 < 0):
        final["gold_ingots"] = 1
    else:
        final["gold_ingots"] = purse["gold_ingots"] + 1

    return final

def get_ingot(purse: dict[str, int]) -> dict[str, int]:
    final: dict[str, int] = {}
    if ("gold_ingots" in purse) or (purse["gold_ingots"] > 1):
        final["gold_ingots"] = purse["gold_ingots"] - 1

    return final

def empty(purse: dict[str, int]) -> dict[str, int]:


    return purse