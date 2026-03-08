def garden_operations(operation: str):
    if operation == "value":
        int("abc")

    elif operation == "zero":
        100 / 0

    elif operation == "file":
        open("missing.txt", "r")

    elif operation == "key":
        plantes = {"rose": "rouge", "tulipe": "jaune"}
        plantes["missing_plant"]


def test_error_types():
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError as e:
        print(f"Caught {e.__class__.__name__}: invalid literal for int()")
        print()

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print()

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught {e.__class__.__name__}: No such file {e.filename}")
        print()

    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print()

    print("Testing multiple errors together...")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()