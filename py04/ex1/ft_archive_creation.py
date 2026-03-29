if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    name = "new_discovery.txt"
    entries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]

    try:
        print(f"Initializing new storage unit: {name}")
        with open(name, "w") as f:
            for entry in entries:
                f.write(entry + "\n")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        for entry in entries:
            print(entry)
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{name}' ready for long-term preservation.")
    except Exception as e:
        print("Error:", e)
