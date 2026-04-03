def secure_archive(
    filename: str,
    mode: str = "r",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if mode == "r":
            with open(filename, "r") as f:
                data = f.read()
            return True, data
        elif mode == "w":
            with open(filename, "w") as f:
                f.write(content)
            return True, "Content successfully written to file"
        else:
            return False, "Invalid mode"
    except Exception as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    success, data = secure_archive("ancient_fragment.txt")
    print((success, data))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w", data))


if __name__ == "__main__":
    main()
