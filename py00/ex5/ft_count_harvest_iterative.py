def ft_count_harvest_iterative() -> None:
    days = 0
    days = int(input("Days until harvest: "))
    i = 1
    while i <= days:
        print(f"Day {i}")
        i += 1
    print("Harvest time!")

def main():
    ft_count_harvest_iterative()

if __name__ == "__main__":
    main()