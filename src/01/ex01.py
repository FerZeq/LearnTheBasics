def split_booty(*args: dict[str, int]) -> tuple[dict[str, int], dict[str, int], dict[str, int]]:
    final_one: dict[str, int] = {}
    final_two: dict[str, int] = {}
    final_three: dict[str, int] = {}
    gold_ingots_total: int = 0
    for arg in args:
        if ("gold_ingots" in arg) and (arg["gold_ingots"] >= 0):
            gold_ingots_total += arg["gold_ingots"]

    if gold_ingots_total >= 0:
        avg = gold_ingots_total // 3
        r = gold_ingots_total % 3

        if r >= 1:
            final_one["gold_ingots"] = avg + 1
        else:
            final_one["gold_ingots"] = avg

        if r == 2:
            final_two["gold_ingots"] = avg + 1
        else:
            final_two["gold_ingots"] = avg

        final_three["gold_ingots"] = avg

    return final_one, final_two, final_three

if __name__ == "__main__":
    print(split_booty({"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 3}, {"rocks": 20}))