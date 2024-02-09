def egg_count(display_value):
    total_eggs = 0

    while display_value > 0:
        if display_value % 2 == 1:
            total_eggs += 1
            display_value = int(display_value / 2)

        else:
            display_value = int(display_value / 2)

    return total_eggs
