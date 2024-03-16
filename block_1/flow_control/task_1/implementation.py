def get_numbers():
    """Возвращает все числа от 1000 до 2000, которые делятся на 7, но не кратны 5

    Returns: итерируемый объект с нужными числами
    """
    list_name = []
    for item in range(1000, 2001):
        if (item % 7) == 0 and (item % 5) != 0:
            list_name.append(item)

    return list_name
