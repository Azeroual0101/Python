def open_archive(file_path: str) -> str:
    """Lit le contenu d'un fichier et le retourne."""
    with open(file_path, "r") as archive:
        content = archive.read()
        return content


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    try:
        archive_file = "../lost_archive.txt"
        print(f"CRISIS ALERT: Attempting access to '{archive_file}'...")
        archive_content = open_archive(archive_file)
        print(archive_content)
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except Exception as e:
        print("ERROR:", e)
    finally:
        print("STATUS: Crisis handled, system stable\n")

    try:
        archive_file = "../classified_vault.txt"
        print(f"CRISIS ALERT: Attempting access to '{archive_file}'...")
        open_archive(archive_file)
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception as e:
        print("ERROR:", e)
    finally:
        print("STATUS: Crisis handled, security maintained\n")


    try:
        archive_file = "../standard_archive.txt"
        print(f"ROUTINE ACCESS: Attempting access to '{archive_file}'...")
        archive_content = open_archive(archive_file)
        print(f"SUCCESS: Archive recovered - ``{archive_content}''")
    except Exception as e:
        print("ERROR:", e)
    finally:
        print("STATUS: Normal operations resumed\n")

    print("All crisis scenarios handled successfully. Archives secure.")