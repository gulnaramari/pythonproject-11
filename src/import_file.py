import logging

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/import_file.log",
    filemode="w",
)
read_csvExcel_logger = logging.getLogger("import_file")


def transactions_from_csvExcel(path_to_file: str) -> list[dict]:
    """Функция чтения данных из csv и Excel файлов"""
    read_csvExcel_logger.info("Reading is started")
    try:
        if ".csv" in path_to_file[-4:]:
            df = pd.read_csv(path_to_file, delimiter=";")
            read_csvExcel_logger.info(
                "Creating a DataFrame from a csv file is successful"
            )
            result_csv = df.to_dict(orient="records")
            read_csvExcel_logger.info("Reading was completed")
            return result_csv
        else:
            df = pd.read_excel(path_to_file)
            read_csvExcel_logger.info(
                "Creating a DataFrame from a Excel file is successful"
            )
            result_Excel = df.to_dict(orient="records")
            read_csvExcel_logger.info("Reading was completed")
            return result_Excel
    except FileNotFoundError:
        read_csvExcel_logger.warning("File not found. Incorrect path to file")
        read_csvExcel_logger.info("The work is completed")
        print("Файл не найден")
        return []


if __name__ == "__main__":
    result = transactions_from_csvExcel("..\\data\\transactions_excel.xlsx")
    print(result)


if __name__ == "__main__":
    result = transactions_from_csvExcel("..\\data\\transactions.csv")
    print(result)
