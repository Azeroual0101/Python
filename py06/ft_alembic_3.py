from alchemy.elements import create_air

def main() -> None:
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using 'from ... import ...' structure")
    print("Testing create_air:", create_air())
    print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
