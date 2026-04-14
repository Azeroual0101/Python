from elements import create_water


def main() -> None:
    print("=== Alembic 1 ===")
    print("Using: 'import ...' structure to access elements.py")
    print("Testing create_water:", create_water())
    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
