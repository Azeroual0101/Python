class GardenError(Exception):
    """Base exception class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for problems with plants."""
    def __init__(self, name: str) -> None:
        """Initialize PlantError with the plant name."""
        super().__init__(f"The {name} plant is wilting!")


class WaterError(GardenError):
    """Exception raised for problems with watering."""
    pass


def test_water(volume: int) -> None:
    """Test WaterError with a given water volume."""
    print("Testing WaterError...")
    try:
        if volume <= 0:
            raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")


def test_garden(name: str, volume: int) -> None:
    """Test catching all garden errors using the base GardenError class."""
    print("Testing catching all garden errors...")
    try:
        raise PlantError(name)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        if volume <= 0:
            raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")
    print("All custom error types work correctly!")


def test_plant(name: str) -> None:
    """Test PlantError with a given plant name."""
    print("Testing PlantError...")
    try:
        raise PlantError(name)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")


if __name__ == "__main__":
    try:
        print("=== Custom Garden Errors Demo ===\n")
        name: str = "tomato"
        volume: int = -5
        test_plant(name)
        test_water(volume)
        test_garden(name, volume)
    except Exception as e:
        print(f"Caught an error: {e}")
