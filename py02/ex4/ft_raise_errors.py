def check_plant_health(
    plant_name: str, water_level: int, sunlight_hours: int
) -> None | str:
    """Validate plant health parameters and return status or raise errors."""
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Error: Water level {water_level} "
                         "is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level} "
                         "is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too high (max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Test plant health validation with valid and invalid inputs."""
    try:
        print("Testing good values...")
        succ: str = check_plant_health("tomato", 9, 10)
        if succ:
            print(succ)
        print("\nTesting empty plant name...")
        check_plant_health("", 8, 12)
    except ValueError as e:
        print(e)
    try:
        print("\nTesting bad water level...")
        check_plant_health("tomato", 15, 9)
    except ValueError as e:
        print(e)
    try:
        print("\nTesting bad sunlight hours...")
        check_plant_health("tomato", 8, 0)
    except ValueError as e:
        print(e)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    try:
        print("=== Garden Plant Health Checker ===\n")
        test_plant_checks()
    except Exception as e:
        print(f"Caught an error: {e}")
