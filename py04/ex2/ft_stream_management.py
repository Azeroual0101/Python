import sys

def main() -> None:
	print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

	try:
		archivist_id = input("Input Stream active. Enter archivist ID: ")
		status_report = input("Input Stream active. Enter status report: ")
		print()

		message = (
			f"[STANDARD] Archive status from {archivist_id}: {status_report}"
		)
		sys.stdout.write(message + "\n")

		sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n" + "\n")

		sys.stdout.write("[STANDARD] Data transmission complete"+ "\n")
		sys.stdout.write("Three-channel communication test successful.\n")
	except Exception as e:
		sys.stderr.write(f"[ERROR] An error occurred: {e}\n")

if __name__ == "__main__":
	main()