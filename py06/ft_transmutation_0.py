import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    result = alchemy.transmutation.recipes.lead_to_gold()
    print("Testing lead to gold:", result)
    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
