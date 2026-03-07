class Plant:
    def __init__(self, name: str, height: int, lifetime: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.lifetime = lifetime
        self.inial_height = height
        self.inial_age = lifetime

    def age(self) -> None:
        self.lifetime += 1
        self.grow()

    def grow(self) -> None:
        self.height += 1

    def get_info(self) -> None:
        print(f"Growth this week: +{self.lifetime - self.inial_age}cm")

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.lifetime} days old"


def main() -> None:
    plants = [
        Plant("rose", 25, 30),
        Plant("tulip", 15, 10),
        Plant("lily", 20, 12)
    ]

    day = 1
    print(f"=== Day {day} ===")
    for plant in plants:
        print(plant)

    for _ in range(6):
        for plant in plants:
            plant.age()
        day += 1

    print(f"=== Day {day} ===")
    for plant in plants:
        print(plant)
        plant.get_info()


if __name__ == "__main__":
    main()
