def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    name = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {name}")

    file = None
    try:
        file = open(name, "r")
        print("Connection established...\n")

        print("RECOVERED DATA:")
        print(file.read())

        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")

    finally:
        if file is not None:
            file.close()


if __name__ == "__main__":
    main()
