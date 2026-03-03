class Plant:
    def __init__(self,name: str,height: int,lifetime: int):
        self.name = name.capitalize()
        self.height = height
        self.lifetime =lifetime
        self.inial_height = height
        self.inial_age =lifetime

    def age(self, augment: int):
        self.lifetime += augment

    def grow(self):
        self.height = self.inial_height + self.lifetime - self.inial_age

    
    def get_info(self):
        return f"Growth this week: +{self.lifetime - self.inial_age}cm"

    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.lifetime} days old"
    
def main():
    plant1 = Plant("rose",25,30)
    print("=== Day 1 ===")
    print(plant1)
    print("=== Day 7 ===")
    plant1.age(6)
    plant1.grow()
    print(plant1)
    print(plant1.get_info())
    print("=== Day 14 ===")
    plant1.age(6)
    plant1.grow()
    print(plant1)
    print(plant1.get_info())

if __name__ == "__main__":
    main()