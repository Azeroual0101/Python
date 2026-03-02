def ft_harvest_total() -> None:
    i = 1
    totale = 0
    while i < 4:
        day = int(input(f"Day {i} harvest: "))
        totale += day
        i += 1
    print("Total harvest: ",totale) 
