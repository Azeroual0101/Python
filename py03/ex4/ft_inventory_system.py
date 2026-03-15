import sys


def ft_atoi(value: str) -> int:
    digits = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }
    pos: int = 0
    sign: int = 1
    number: int = 0
    if value and (value[0] == '-' or value[0] == '+'):
        if value[0] == '-':
            sign = -1
        pos = 1
    for ch in value[pos:]:
        if ch not in digits:
            raise ValueError("Not valid number")
        number = number * 10 + digits[ch]
    return number * sign


def ft_split(entry: str, delimiter: str) -> list[str]:
    parts: list[str] = []
    i: int = 0
    for ch in entry:
        if ch == delimiter:
            parts += [entry[:i]]
            parts += [entry[i + 1:]]
            break
        i += 1
    return parts


def lookup(inventory: dict, target: str) -> bool:
    for key in inventory:
        if key == target:
            return True
    return False


def get_max(inventory: dict) -> str:
    champion: str
    for first in inventory:
        champion = first
        break
    for entry in inventory:
        if inventory[entry] > inventory[champion]:
            champion = entry
    return champion


def get_min(inventory: dict) -> str:
    weakest: str
    for first in inventory:
        weakest = first
        break
    for entry in inventory:
        if inventory[entry] < inventory[weakest]:
            weakest = entry
    return weakest


def compute_ratio(inventory: dict, name: str) -> float:
    grand_total: int = 0
    for entry in inventory:
        grand_total += inventory[entry]
    return inventory[name] / grand_total * 100


def display_dict(inventory: dict, mode: str) -> None:
    size: int = len(inventory.keys())
    cursor: int = 0
    if mode == "keys":
        for key in inventory:
            cursor += 1
            if cursor == size:
                print(key)
            else:
                print(key, end=", ")
    elif mode == "values":
        for val in inventory.values():
            cursor += 1
            if cursor == size:
                print(val)
            else:
                print(val, end=", ")
    else:
        print("Invalid mode")


if __name__ == "__main__":
    try:
        print("=== Inventory System Analysis ===")
        inventory: dict = dict()
        for arg in sys.argv[1:]:
            segments = ft_split(arg, ":")
            if len(segments) != 2:
                raise ValueError(f"Invalid argument format: {arg}")
            inventory[segments[0]] = ft_atoi(segments[1])

        grand_total: int = 0

        buckets: dict = {
            "moderate": dict(),
            "scarce": dict()
        }

        restock_list: list = []

        for entry in inventory:
            grand_total += inventory[entry]
            ratio = compute_ratio(inventory, entry)
            if ratio > 40:
                buckets["moderate"].update({entry: inventory[entry]})
            else:
                buckets["scarce"].update({entry: inventory[entry]})
            if inventory[entry] < 2:
                restock_list += [entry]

        print(f"Total items in inventory: {grand_total}")
        print(f"Unique item types: {len(inventory.keys())}")

        print("\n=== Current Inventory ===")
        expected: list = ["potion", "armor", "shield", "sword", "helmet"]
        for item in expected:
            if item not in inventory.keys():
                raise KeyError(f"KeyError: '{item}'")
            ratio: float = compute_ratio(inventory, item)
            qty = inventory.get(item)
            if qty != 1:
                print(f"{item}: {qty} units ({ratio:.1f}%)")
            else:
                print(f"{item}: {qty} unit ({ratio:.1f}%)")

        print("\n=== Inventory Statistics ===")
        top: str = get_max(inventory)
        bottom: str = get_min(inventory)
        print(f"Most abundant: {top} ({inventory[top]} units)")
        print(f"Least abundant: {bottom} ({inventory[bottom]} unit)")

        print("\n=== Item Categories ===")
        print(f"Moderate: {buckets['moderate']}")
        print(f"Scarce: {buckets['scarce']}")

        print("\n=== Management Suggestions ===")
        print("Restock needed: ", end="")
        total_restock: int = len(restock_list)
        cursor: int = 0
        for need in restock_list:
            cursor += 1
            if cursor == total_restock:
                print(f"{need}")
            else:
                print(f"{need}, ", end="")

        print("\n=== Dictionary Properties Demo ===")
        print("Dictionary keys: ", end="")
        display_dict(inventory, "keys")
        print("Dictionary values: ", end="")
        display_dict(inventory, "values")
        print(
            f"Sample lookup - 'sword' in inventory: {lookup(
                inventory, 'sword')}")
    except Exception as e:
        print(e)
