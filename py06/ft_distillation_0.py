from alchemy import potions

def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print("Testing strength_potion:", potions.strength_potion())
    print("Testing healing_potion:", potions.healing_potion())
    print()

if __name__ == "__main__":
    main()
