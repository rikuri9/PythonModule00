def ft_count_harvest_iterative():
    harvest_day = int(input("Days until harvest: "))
    days = range(harvest_day)

    for day in days:
        print(f"Day {day + 1}")

    print("Harvest time!")
