class SecurePlant():

    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print(f"Security: Negative height rejected")
        else:
            self.height = height
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print(f"Security: Negative age rejected")
        else:
            self.age = age
        print(f"Palnt created :{self.name}")

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print(f"Security: Negative height rejected")
        else:
            self.height = height
            print(f"Height updated: {height}cm [OK]")
    def set_age(self, age: int):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print(f"Security: Negative age rejected")
        else:
            self.age = age
            print(f"Age updated: {age} days [OK]")
    def __str__(self):
        return(f"Current plant: {self.name} ({self.height}cm, {self.age} days)")
    
def main():

    print("=== Garden Security System ===")
    plant = SecurePlant("emy",-99,-30)
    plant.set_height(9)
    plant.set_age(8)
    print()
    plant.set_height(-9)
    print()
    print(plant)

if __name__ == "__main__":
    main()