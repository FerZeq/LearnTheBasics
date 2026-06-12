def burglar_alarm(func):
    print("squeak")
    return func

@burglar_alarm
def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    final: dict[str, int] = {}
    if ("gold_ingots" not in purse) or (purse["gold_ingots"] + 1 < 0):
        final["gold_ingots"] = 1
    else:
        final["gold_ingots"] = purse["gold_ingots"] + 1

    return final

@burglar_alarm
def get_ingot(purse: dict[str, int]) -> dict[str, int]:
    final: dict[str, int] = {}
    if ("gold_ingots" in purse) or (purse["gold_ingots"] > 1):
        final["gold_ingots"] = purse["gold_ingots"] - 1

    return final

@burglar_alarm
def empty(purse: dict[str, int]) -> dict[str, int]:
    final: dict[str, int] = {}
    if ("gold_ingots" in purse) and (purse["gold_ingots"] > 0):
        final["gold_ingots"] = 0

    return final

if __name__ == "__main__":
    purse1: dict[str, int] = {'gold_ingots': 1}
    print(add_ingot(get_ingot(add_ingot(empty(purse1)))))