import sys


def parse_args(args: list[str]) -> dict[str, int]:
    stock: dict[str, int] = {}

    for element in args:
        parts = element.split(':')

        if len(parts) != 2:
            print(f"Error - invalid parameter '{element}'")
            continue

        name = parts[0]
        value_str = parts[1]

        if name in stock:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            value = int(value_str)
            stock[name] = value
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")

    return stock


def display_inventory(data: dict[str, int]) -> None:
    print(f"Got inventory: {data}")

    items = list(data.keys())
    print(f"Item list: {items}")

    total = sum(data.values())
    count = len(data)
    print(f"Total quantity of the {count} items: {total}")

    for key in data.keys():
        qty = data[key]
        percent = round((qty / total) * 100, 1)
        print(f"Item {key} represents {percent}%")

    max_item = ""
    max_val = -1
    min_item = ""
    min_val = float('inf')

    for key in data.keys():
        qty = data[key]

        if qty > max_val:
            max_val = qty
            max_item = key

        if qty < min_val:
            min_val = qty
            min_item = key

    print(f"Item most abundant: {max_item} with quantity {max_val}")
    print(f"Item least abundant: {min_item} with quantity {min_val}")


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: python3 ft_inventory_system.py <item_name>:<quantity>")
        return

    print("=== Inventory System Analysis ===")

    inventory_data = parse_args(sys.argv[1:])

    if len(inventory_data) == 0:
        return

    display_inventory(inventory_data)

    inventory_data.update({"magic_item": 1})
    print(f"Updated inventory: {inventory_data}")


if __name__ == "__main__":
    main()