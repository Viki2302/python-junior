def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    value = []

    if month == 'январь' or month == 'март' or month == 'май' or month == 'июль' or month == 'август' or month == 'октябрь'or month == 'декабрь':
        value.append(31)
    elif month == 'апрель' or month == 'июнь' or month == 'сентябрь' or month == 'ноябрь':
        value.append(30)
    elif month == 'февраль':
        value.append(28)
        value.append(29)
    else:
        value.append(0)
        
    return value
