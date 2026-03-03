class Plant:

    def __init__(self,name: str ,height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age
    def __str__(self):
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"

def main():

    Plants = []
    i = 0
    data = {
        "James": [18, 65],
        "Emma": [20, 70],
        "Michael": [22, 75],
        "Olivia": [25, 80],
        "Jordan": [30, 85]
    }
    for name, infos in data.items():
        Plants.append(Plant(name,infos[0],infos[1]))
        i += 1
    for j in range(i):
        print(Plants[j])
        j += 1
    print()
    print(f"Total plants created: {i}")
if __name__ == "__main__":
    main()
        

