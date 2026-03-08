def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
        print()

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
        print()

    print("Testing FileNotFoundError...")
    try:
        f = open("missing.txt", "r")
        f.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
        print()

    print("Testing KeyError...")
    try:
        d = {}
        d["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
        print()

    print("Testing multiple errors together...")
    try:
        int("abc")
        1 / 0
        f = open("missing.txt", "r")
        f.close()
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!")
        print()


def test_error_types() -> None:
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    print()
    test_error_types()