class Plant():
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.initial_height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize_points: int):
        super().__init__(name, height, color)
        self.prize_points = prize_points

class Garden:
    def __init__(self, proprietaire: str) -> None:
        self.proprietaire = proprietaire
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        self.plants += [plant]
        print(f"Added {plant.name} to {self.proprietaire}'s garden")

    def grow_all(self) -> None:
        for plant in self.plants:
            plant.grow()

    def cal_len(self) -> int:
        count = 0
        for plant in self.plants:
            count += 1
        return count

    def validate_heights(self) -> bool:
        for plant in self.plants:
            if plant.height <= 0:
                return False
        return True

    def generate_report(self):
        print(f"=== {self.proprietaire}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if hasattr(plant, 'prize_points'):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming), Prize points: {plant.prize_points}")
            elif hasattr(plant, 'color'):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming)")
            else:
                print(f"- {plant.name}: {plant.height}cm")

        total_plants = self.cal_len()

        regular_count = 0
        flowering_count = 0
        prize_count = 0
        total_growth = 0

        for plant in self.plants:
            class_name = plant.__class__.__name__

            if class_name == "PrizeFlower":
                prize_count += 1
            elif class_name == "FloweringPlant":
                flowering_count += 1
            elif class_name == "Plant":
                regular_count += 1

            if hasattr(plant, 'initial_height'):
                total_growth += plant.height - plant.initial_height

        print()
        print(f"Plants added: {total_plants}, Total growth: {total_growth}cm")
        print(f"Plant types: {regular_count} regular, {flowering_count} flowering, {prize_count} prize flowers")

        validation_result = self.validate_heights()
        print()
        print(f"Height validation test: {validation_result}")

class GardenManager:
    def __init__(self) -> None:
        self.gardens = {}

    def add_garden(self, name: str, garden: Garden) -> None:
        self.gardens[name] = garden

    class GardenStats:
        @staticmethod
        def calculate_score(garden: Garden) -> int:
            total = 0

            # Base score: 40 points per plant
            total += len(garden.plants) * 40

            for plant in garden.plants:
                # Bonus for flowering plants (have a color)
                if hasattr(plant, 'color'):
                    total += 12

                # Bonus for prize points
                if hasattr(plant, 'prize_points'):
                    total += plant.prize_points * 5

                # Blooming bonus: plant has grown since initial
                if plant.height > plant.initial_height:
                    total += 8

            return total

        @classmethod
        def compare_gardens(cls, garden1: Garden, garden2: Garden) -> str:
            score1 = cls.calculate_score(garden1)
            score2 = cls.calculate_score(garden2)
            return f"{garden1.proprietaire}: {score1}, {garden2.proprietaire}: {score2}"

    @classmethod
    def create_garden_network(cls, gardens_dict: dict) -> str:
        count = 0
        for key in gardens_dict:
            count += 1
        return f"Total gardens managed: {count}"

    @staticmethod
    def utility_function() -> str:
        return "This is a utility function"

def main():
    print("=== Garden Management System Demo ===")
    print()

    # Créer des plantes
    chene = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    tournesol = PrizeFlower("Sunflower", 50, "yellow", 10)

    # Jardin d'Alice
    jardin_alice = Garden("Alice")
    jardin_alice.add_plant(chene)
    jardin_alice.add_plant(rose)
    jardin_alice.add_plant(tournesol)

    # Jardin de Bob (sans afficher les messages)
    jardin_bob = Garden("Bob")
    chene2 = Plant("Oak Tree", 90)
    rose2 = FloweringPlant("Rose", 20, "pink")
    jardin_bob.plants += [chene2, rose2]  # Pas de print

    print()
    print("Alice is helping all plants grow...")
    jardin_alice.grow_all()

    print()
    jardin_alice.generate_report()

    # GardenManager
    manager = GardenManager()
    manager.add_garden("Alice", jardin_alice)
    manager.add_garden("Bob", jardin_bob)

    stats = GardenManager.GardenStats()
    print(f"Garden scores - {stats.compare_gardens(jardin_alice, jardin_bob)}")

    print(GardenManager.create_garden_network(manager.gardens))

if __name__ == "__main__":
    main()