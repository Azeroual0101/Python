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
    content: list = []
    try:
        file = open(filename, "r")
        print("---\n")
        line = file.readline()
        while line:
            content.append(line)
            print(line, end="")
            line = file.readline()
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
    new_content: list = []
    for line in content:
        new_line = line[:-1] + "#\n"
        new_content += new_line
        print(new_line, end="")
    print("\n---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file = sys.stdin.readline()[:-1]

    if new_file == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")

    f: typing.IO = None
    try:
        f = open(new_file, "w")
        for line in new_content:
            f.write(line)
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
