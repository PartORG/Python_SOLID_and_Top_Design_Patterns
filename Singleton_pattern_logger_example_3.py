import logging
import threading



# define a SingletonLogger class
class SingletonMeta(type):
    # class-level dictionary to store single instance of the class
    _instances = {}
    # class-level lock to ensure thread safety
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
            return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    _logger = None

    def __init__(self):
        self._initialize_logger()

    # Helper method to initialize logger
    def _initialize_logger(self):
        # create a logger object with specified name
        print('<Logger init> initializing logger... ')
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

    # getter method
    def get_logger(self):
        return self._logger

# Usage
logger = Logger().get_logger()
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')