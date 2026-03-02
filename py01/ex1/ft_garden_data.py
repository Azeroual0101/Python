class Plant:
    def __init__(self,name: str,height: int,age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age
    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

def main():

    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(plant1)
    print(plant2)
    print(plant3)


if __name__ == "__main__":
    main()