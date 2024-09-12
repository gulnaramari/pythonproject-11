import datetime


def date_formatting(input_data: str) -> str:
    """Функция приводящая дату к нужному формату"""
    if len(input_data) == 26:
        dt_obj = datetime.datetime.strptime(input_data, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date_string = dt_obj.strftime("%d.%m.%Y")
    else:
        dt_obj = datetime.datetime.strptime(input_data, "%Y-%m-%dT%H:%M:%SZ")
        formatted_date_string = dt_obj.strftime("%d.%m.%Y")
    return formatted_date_string
