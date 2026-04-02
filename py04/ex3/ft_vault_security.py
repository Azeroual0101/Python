def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")

    try:
        with open("classified_data.txt", "r") as f:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            for line in f:
                print(line, end="")
            print("\n")

        with open("security_protocols.txt", "w") as f:
            print("SECURE PRESERVATION:")
            f.write("[CLASSIFIED] New security protocols archived\n")

        with open("security_protocols.txt", "r") as f:
            for line in f:
                print(line, end="")

        print("Vault automatically sealed upon completion\n")

    except FileNotFoundError:
        print("[ERROR] Vault file not found")

    except Exception as e:
        print(f"[ERROR] Unexpected issue: {e}")

    finally:
        print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()