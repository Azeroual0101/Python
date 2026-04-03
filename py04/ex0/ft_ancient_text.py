import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>\n")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file = None
    try:
        file = open(filename, "r")
        print("---\n")
        print(file.read(), end="")
        print()
        print("\n---")

    except Exception as e:
        print(f"Error opening file '{filename}': {e}\n")

    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
