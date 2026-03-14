def check_temperature(temp_str: str) -> int | None:
    """Check if temperature string is valid for plants (0-40°C)."""
    try:
        temp = int(temp_str)
        if temp < 0:
            raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp
    except ValueError as e:
        print(f"Error: {e}")
        return None


def test_temperature_input():
    """Test temperature validation with various inputs."""
    print("=== Garden Temperature Checker ===")

    test_values = ["25", "abc", "100", "-50"]

    for val in test_values:
        print()
        print(f"Testing temperature: {val}")
        check_temperature(val)

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    try:
        test_temperature_input()
    except Exception as e:
        print(f"Caught an error: {e}")
