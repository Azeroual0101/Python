def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    seed_type = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed_type} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")


def main():
    ft_seed_inventory("tomato", 15, "packets")
    print("-----------")
    ft_seed_inventory("carrot", 8, "grams")
    print("-----------")
    ft_seed_inventory("lettuce", 12, "area")
    print("-----------")
    ft_seed_inventory("lettuce", 12, "areaaa")

if __name__ == "__main__":
    main()