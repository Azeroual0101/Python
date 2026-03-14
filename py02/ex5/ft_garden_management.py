class GardenError(Exception):
    """Base exception class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for problems with plants."""
    pass


class WaterError(GardenError):
    """Exception raised for problems with watering."""
    pass


class Plant:
    """Represents a plant with its health parameters."""
    def __init__(self, name: str, water: int, sun: int) -> None:
        """Initialize a plant with name, water level and sunlight hours."""
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    """Manages a collection of plants with error-resilient operations."""
    def __init__(self) -> None:
        """Initialize the garden manager with empty plant list."""
        self.plants: list[Plant] = []
        self.water_tank: int = 15

    def add_plant(self, plants_data: list) -> None:
        """Add plants from data list, handling invalid entries gracefully."""
        for data in plants_data:
            try:
                if not data[0]:
                    raise PlantError("Error adding plant: Plant name cannot "
                                     "be empty!")

                plant = Plant(data[0], data[1], data[2])
                self.plants += [plant]
                print(f"Added {data[0]} successfully")

            except PlantError as error:
                print(error)

    def water_plants(self) -> None:
        """Water all plants with cleanup guaranteed via finally block."""
        try:
            if self.water_tank <= 0:
                raise WaterError("Not enough water in tank")

            print("Opening watering system")

            for plant in self.plants:
                print(f"Watering {plant.name} - success")

        except GardenError as error:
            print(f"Caught GardenError: {error}")
            print("System recovered and continuing...")

        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        """Check health of all plants and report errors for invalid values."""
        for plant in self.plants:
            try:
                if plant.water < 1 or plant.water > 10:
                    raise GardenError(
                        f"Water level {plant.water} is invalid (1-10)"
                    )

                if plant.sun < 2 or plant.sun > 12:
                    raise GardenError(
                        f"Sunlight hours {plant.sun} is invalid (2-12)"
                    )

            except GardenError as error:
                print(f"Error checking {plant.name}: {error}")

            else:
                print(
                    f"{plant.name}: healthy "
                    f"(water: {plant.water}, sun: {plant.sun})"
                )


def test_garden_management() -> None:
    """Test all garden management features including error recovery."""
    manager = GardenManager()

    print("Adding plants to garden...")

    plants = [
        ["tomato", 5, 8],
        ["lettuce", 15, 12],
        ["", 10, 12]
    ]

    manager.add_plant(plants)

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_plant_health()

    manager.water_tank = 0

    print("\nTesting error recovery...")
    manager.water_plants()

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()
