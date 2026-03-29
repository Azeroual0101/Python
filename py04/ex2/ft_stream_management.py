import sys

# 1. En-tête
print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

# 2. Collecte des données (stdin via input())
archivist_id = input("Input Stream active. Enter archivist ID: ")
status_report = input("Input Stream active. Enter status report: ")

# 3. Affichage sur la sortie STANDARD (stdout)
print(f"[STANDARD] Archive status from {archivist_id}: {status_report}", file=sys.stdout)

# 4. Affichage sur la sortie ALERTE (stderr)
print("[ALERT] System diagnostic: Communication channels verified", file=sys.stderr)

# 5. Suite sur la sortie STANDARD (stdout)
print("[STANDARD] Data transmission complete", file=sys.stdout)

# 6. Confirmation finale
print("Three-channel communication test successful.")
