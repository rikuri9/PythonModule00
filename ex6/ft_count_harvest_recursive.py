def ft_count_harvest_recursive(harvest_day=None, days=None):
    if days is None:

        days = int(input("Days until harvest: "))
        harvest_day = days
        ft_count_harvest_recursive(harvest_day, days)

    else:
        if days > 1:
            ft_count_harvest_recursive(harvest_day, days - 1)
        print(f"Day {days}")
        if days == harvest_day:
            print("Harvest time!")
