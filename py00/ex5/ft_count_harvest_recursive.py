def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def helper(current_day):
        if current_day == days:
            return
        print(f"Day {current_day}")
        return helper(current_day + 1)
    
    helper(1)
    print("Harvest time!")


def main():
    ft_count_harvest_recursive()


if __name__ == "__main__":
    main()