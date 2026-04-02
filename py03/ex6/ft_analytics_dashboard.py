import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    names_list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                  'Gregory', 'john', 'kevin', 'Liam']

    print(f"Initial list of players: {names_list}")

    all_caps = [n.capitalize() for n in names_list]
    print(f"New list with all names capitalized: {all_caps}")

    only_caps = [n for n in names_list if n[0].isupper()]
    print(f"New list of capitalized names only: {only_caps}")


    scores = {n: random.randint(0, 1000) for n in all_caps}
    print(f"Score dict: {scores}")

    avg = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg}")

    best_scores = {k: v for k, v in scores.items() if v > avg}
    print(f"High scores: {best_scores}")


if __name__ == "__main__":
    main()
