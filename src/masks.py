import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    filename='logs/masks.log',
                    filemode='w')
mask_logger = logging.getLogger('masks')


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирующая номер карты"""
    mask_logger.info('Запуск программы')
    step = 4
    card_number_str = str(card_number)
    if len(card_number_str) == 16:
        mask_logger.info('Данные карты успешно зашифрованы')
        removed_string = card_number_str[6:-4]
        hidden_number_string = card_number_str.replace(removed_string, '******')
        hidden_number = (
            " ".join([hidden_number_string[j:j + step] for j in range(0, len(hidden_number_string), step)]))
        return hidden_number
    else:
        mask_logger.error('Введены неверные данные карты')


def get_mask_account(account_number: str) -> str:
    """Функция маскирующая номер счета"""
    mask_logger.info('Запуск программы')
    account_number_str = str(account_number)
    if len(account_number_str) == 20:
        removed_string = account_number_str[0:-4]
        hidden_number = account_number_str.replace(removed_string, '**')
        mask_logger.info('Данные счёта успешно зашифрованы')
        return hidden_number
    else:
        mask_logger.error('Введены неверные данные счёта')
