def get_date(input_data: str) -> str:
    """Функция преобразования даты"""
    for arg in input_data:
        if not isinstance(arg, str):
            raise TypeError("Ошибка типа данных")
    if len(input_data) == 26 and input_data[10] == "T":
        date = input_data.split("T")[0]
        slice_date = f"{date[-2:]}.{date[5:7]}.{date[:4]}"
    else:
        raise ValueError("Некорректно введены данные")
    return slice_date


print(get_date("2024-03-11T02:26:18.671407"))
