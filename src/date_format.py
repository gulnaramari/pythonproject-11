import datetime


def date_formatting(date_str: str) -> str:
    """Функция приводящая дату к нужному формату"""
    if len(date_str) == 26:
        dt_obj = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
        formatted_date_string = dt_obj.strftime('%d.%m.%Y')
    else:
        dt_obj = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
        formatted_date_string = dt_obj.strftime('%d.%m.%Y')
    return formatted_date_string
