class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


def main() -> None:

    Plants = []
    i = 0
    data = {
        "rose": [25, 30],
        "oak": [200, 365],
        "cactus": [5, 90],
        "sunflower": [80, 45],
        "fern": [15, 120]
    }
    print("=== Plant Factory Output ===")
    for name in data:
        Plants += [(Plant(name, data[name][0], data[name][1]))]
        i += 1
    for plant in Plants:
        print(plant)

    print()
    print(f"Total plants created: {i}")


if __name__ == "__main__":
    main()
