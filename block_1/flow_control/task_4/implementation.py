def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    dates = some_date.split(",")

    year = dates[0] 
    month = dates[1]
    day = dates[2]

    value = []

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day == 31:
            if month == 12:
                value.append(year + 1) 
                value.append(1) 
                value.append(1)
            else:
            value.append(year) 
            value.append(month + 1) 
            value.append(1)
        else:
            value.append(year) 
            value.append(month) 
            value.append(day + 1)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day == 30:
        value.append(year) 
        value.append(month + 1) 
        value.append(1)
        else:
            value.append(year) 
            value.append(month) 
            value.append(day + 1)
    elif month == 2:
        if (day == 28) and (year % 4 != 0):
        value.append(year) 
        value.append(month + 1) 
        value.append(1)
        else:
            value.append(year) 
            value.append(month) 
            value.append(day + 1)
    else:
        value.append(0)
    
    print(value)    
    # return value


    raise NotImplementedError
