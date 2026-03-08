def check_temperature(temp_str):
    try:
        err: bool = True
        temp = int(temp_str)
        if temp < 0:
            err = False
            raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            err = False
            raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp

    except ValueError as e:
        if err:
            print(f"Error: '{temp_str}' is not a valid number\n")
        else:
            print(f"Error: {e}")
        return None


def test_temperature_input():
    print("=== Garden Temperature Checker ===")

    test_values = ["25", "abc", "100", "-50"]

    for val in test_values:
        print()
        print(f"Testing temperature: {val}")
        check_temperature(val)

    print()
    print("All tests completed - program didn't crash!")


test_temperature_input()