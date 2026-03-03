class Plant:
    def __init__(self,name: str,height: int,age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age
    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

def main():

    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        Plant("Tulip", 20, 25)
    ]
    print("=== Garden Plant Registry ===")
    for i in range(4):
        print(plants[i]) 


if __name__ == "__main__":
    main()