import math


def ask_coordinates() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates as floats in format 'x,y,z': ")

        parts = user_input.split(',')

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0])
            y = float(parts[1])
            z = float(parts[2])
            return (x, y, z)

        except ValueError:
            # Trouver quel paramètre est faux
            for cord in parts:
                try:
                    float(cord)
                except ValueError as e:
                    print(f"Error on parameter '{cord}': {e}")
                    break

def main() -> None:
    print("=== Game Coordinate System ===\n")

    # First set
    print("Get a first set of coordinates")
    first_coords = ask_coordinates()
    print(f"Got a first tuple: {first_coords}")

    x1, y1, z1 = first_coords
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    distance_to_center = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(distance_to_center, 4)}\n")

    # Second set
    print("Get a second set of coordinates")
    second_coords = ask_coordinates()

    x2, y2, z2 = second_coords
    distance_between = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    print(f"Distance between the 2 sets of coordinates: {round(distance_between, 4)}")


if __name__ == "__main__":
    main()
