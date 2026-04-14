import alchemy


def main() -> None:
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    print("Testing lead to gold:", alchemy.lead_to_gold())
    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
