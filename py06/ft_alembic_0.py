import elements

def main() -> None:
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print("Testing create_fire:", elements.create_fire())
    print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)