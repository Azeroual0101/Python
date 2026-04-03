import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO = None
    try:
        file = open(filename, "r")
        content = file.read()
        print("---\n")
        print(content, end="")
        print("\n---")

    except Exception as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{filename}': {e}\n"
        )
        return

    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.\n")

    print("Transform data:")
    print("---\n")
    new_content = ""
    for line in content.split("\n"):
        if line:
            new_content += line + "#\n"
    print(new_content, end="")
    print("\n---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file = sys.stdin.readline().strip()

    if new_file == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")

    f: typing.IO = None
    try:
        f = open(new_file, "w")
        f.write(new_content)
        print(f"Data saved in file '{new_file}'.")
    except Exception as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{new_file}': {e}\n"
        )
        print("Data not saved.")
    finally:
        if f is not None:
            f.close()


if __name__ == "__main__":
    main()
