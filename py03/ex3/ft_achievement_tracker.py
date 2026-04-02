import random

ACH_LIST = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Unstoppable", "Speed Runner", "Survivor",
    "Treasure Hunter", "First Steps", "Sharp Mind", "Hidden Path Finder"
]


def gen_player_achievements() -> set[str]:
    n = random.randint(5, 9)
    picks = random.sample(ACH_LIST, n)
    return set(picks)


def main() -> None:
    print("=== Achievement Tracker System ===")

    p1 = gen_player_achievements()
    p2 = gen_player_achievements()
    p3 = gen_player_achievements()
    p4 = gen_player_achievements()

    players = {
        "Alice": p1,
        "Bob": p2,
        "Charlie": p3,
        "Dylan": p4
    }

    for name in players:
        print(f"Player {name}: {players[name]}")

    all_ach = p1.union(p2, p3, p4)
    print(f"All distinct achievements: {all_ach}")


    common_ach = p1.intersection(p2, p3, p4)
    print(f"Common achievements: {common_ach}")

    for name in players:
        others = set()
        for other in players:
            if other != name:
                others = others.union(players[other])

        unique = players[name].difference(others)
        print(f"Only {name} has: {unique}")


    total = set(ACH_LIST)
    for name in players:
        missing = total.difference(players[name])
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()