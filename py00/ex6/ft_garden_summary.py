def ft_garden_summary() -> None:
    name = input("Enter garden name: ")
    nbrs = input("Enter number of plants: ")
    print(f"Garden: {name}")
    print(f"Plants: {nbrs}")
    print("Status: Growing well!")

def main():
    ft_garden_summary()

if __name__ == "__main__":
    ft_garden_summary()