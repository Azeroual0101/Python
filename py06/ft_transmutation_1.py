import alchemy.transmutation

def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print("Testing lead to gold:", alchemy.transmutation.lead_to_gold())
    print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
