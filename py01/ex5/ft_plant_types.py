class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def __str__(self):
        return f"{self.name} : {self.height}cm , {self.age} days"


class Flower(Plant):

    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} blooming beautifully!")

    def __str__(self):
        return f"{self.name} (Flower) : {self.height}cm , {self.age} days, {self.color} color"


class Tree(Plant):

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides shade")

    def __str__(self):
        return f"{self.name} (Tree) : {self.height}cm , {self.age} days, {self.trunk_diameter}cm trunk diameter"


class Vegetable(Plant):

    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value_value = nutritional_value

    def nutritional_info(self):
        print(f"{self.name} is rich in nutrients ({self.nutritional_value_value})")

    def __str__(self):
        return f"{self.name} (Vegetable) : {self.height}cm , {self.age} days, Harvest: {self.harvest_season}"


def main():
    print("=== Garden Plant Types ===")

    flower1 = Flower("Rose", 20, 2, "Red")
    flower2 = Flower("Tulip", 15, 1, "Yellow")

    tree1 = Tree("Oak", 300, 10, 50)
    tree2 = Tree("Pine", 250, 8, 40)

    veg1 = Vegetable("Carrot", 10, 3, "Spring", "High")
    veg2 = Vegetable("Tomato", 12, 2, "Summer", "Medium")

    plants = [flower1, flower2, tree1, tree2, veg1, veg2]

    for plant in plants:
        print(plant)

        if isinstance(plant, Flower):
            plant.bloom()

        elif isinstance(plant, Tree):
            plant.produce_shade()

        elif isinstance(plant, Vegetable):
            plant.nutritional_info()
        print()

if __name__ == "__main__":
    main()