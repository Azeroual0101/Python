import alchemy.elements

def main() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print("Testing create_earth:",alchemy.elements.create_earth())
    print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
