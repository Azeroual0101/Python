import alchemy.transmutation.recipes

def main() -> None:
    print("=== Transmutation 0 ===")
    print("Testing lead to gold: Recipe transmuting Lead to Gold:",alchemy.transmutation.recipes.lead_to_gold())
    print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)