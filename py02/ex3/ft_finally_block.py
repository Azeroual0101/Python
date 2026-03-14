def water_plants(plant_list: list[str | None]) -> None:
    """Water each plant in the list, always closing the system in finally."""
    if plant_list.__class__.__name__ != "list":
        raise TypeError("error: wrong type (must be a list)")
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Test the watering system with valid and invalid plant lists."""
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])


if __name__ == "__main__":
    try:
        test_watering_system()
    except Exception as e:
        print(e)
    finally:
        print("\nCleanup always happens, even with errors!")
