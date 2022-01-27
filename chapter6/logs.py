import logging
from selenium import *

from setting import *


def creat_logger(log_name: str = LOG_NAME,
                 log_file: str = LOG_FILE,
                 log_level: int = LOG_LEVEL,
                 log_formatter: tuple = LOG_FORMATTER):
    """
    日志配置和生成器
    :param log_name: 日志名称
    :param log_file: 日志文件的路径
    :param log_level: 日志等级
    :param log_formatter: 日志的格式
    :return:
    """
    formatter = logging.Formatter(*log_formatter)

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(log_name)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    return logger


log = creat_logger()
