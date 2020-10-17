import logging


def get_logger():
    formatter = logging.Formatter(
        fmt='{levelname} - {asctime} - {lineno} - {name} -  In {funcName}: {message}', style='{')

    file_handler = logging.FileHandler('telegram_bot.log', mode='a')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)


    logger = logging.getLogger('app_logger')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

