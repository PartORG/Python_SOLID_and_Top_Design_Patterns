import os
import datetime
import logging
import threading

from abc import ABC, ABCMeta,abstractmethod


class SingletonMeta(metaclass=ABCMeta):
    # class-level dictionary to store single instance of the class
    _instances = {}
    # class-level lock to ensure thread safety
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            print('<SingletonMeta> in the __call__...')
            if cls not in cls._instances:
                cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
            return cls._instances[cls]


class BaseLogger(SingletonMeta):
    @abstractmethod
    def debug(cls, message: str):
        pass

    @abstractmethod
    def info(cls, message: str):
        pass

    @abstractmethod
    def warning(cls, message: str):
        pass

    @abstractmethod
    def error(cls, message: str):
        pass

    @abstractmethod
    def critical(cls, message: str):
        pass


class MyLogger(BaseLogger):

    def __init__(self):
        print('<MyLogger init> initializing logger...')
        self._logger = logging.getLogger('my_logger')
        self._logger.setLevel(logging.DEBUG)

        # create a file handler and set its level to DEBUG
        file_handler = logging.FileHandler('my_log_file.log')
        file_handler.setLevel(logging.DEBUG)

        # create a console handler and set its level to INFO
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # create a formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # add the handlers to the logger
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def debug(self, message: str):
        self._logger.debug(message)

    def info(self, message: str):
        self._logger.info(message)

    def warning(self, message: str):
        self._logger.warning(message)

    def error(self, message: str):
        self._logger.error(message)

    def critical(self, message: str):
        self._logger.critical(message)

# Usage
logger = MyLogger()
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')