import sys

if __name__ == "__main__":

    try:
        print("=== Command Quest ===")
        print(f"Program name: {sys.argv[0]}")
        count = len(sys.argv)
        if len == 1:
            print("No arguments provided!")
        else:
            i = 1
            while i < count:
                print(f"Argument {i}: {sys.argv[i]}")
                i += 1

    except Exception as e:
        print(f"Error : {e}")
    finally:
        print(f"Total arguments: {count}")
