class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm , {self.age} days"


class Flower(Plant):

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def __str__(self) -> str:
        return (f"{self.name} (Flower): {self.height}cm,"
                f" {self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int,
                 shade_area: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_area = shade_area

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.shade_area} square meters of shade")

    def __str__(self) -> str:
        return (f"{self.name} (Tree): {self.height}cm, {self.age} days, "
                f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):

    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional_info(self) -> None:
        print(
            f"{self.name} is rich in vitamin "
            f"{self.nutritional_value}")

    def __str__(self) -> None:
        return (f"{self.name} (Vegetable): {self.height}cm,"
                f" {self.age} days, {self.harvest_season} harvest")


def main() -> None:
    print("=== Garden Plant Types ===")

    flower1 = Flower("rose", 25, 30, "red")
    flower2 = Flower("lily", 15, 20, "white")

    tree1 = Tree("oak", 500, 1825, 50, 78)
    tree2 = Tree("pine", 600, 2000, 70, 60)

    veg1 = Vegetable("tomato", 80, 90, "summer", "C")
    veg2 = Vegetable("carrot", 40, 60, "spring", "B")

    plants = [flower1, flower2, tree1, tree2, veg1, veg2]
    for plant in plants:
        print()
        print(plant)

        if plant.__class__.__name__ == "Flower":
            plant.bloom()

        elif plant.__class__.__name__ == "Tree":
            plant.produce_shade()

        elif plant.__class__.__name__ == "Vegetable":
            plant.nutritional_info()


if __name__ == "__main__":
    main()
