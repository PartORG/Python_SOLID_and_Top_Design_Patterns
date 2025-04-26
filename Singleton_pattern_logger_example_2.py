import logging
import threading

# define a SingletonLogger class
class SingletonLogger:
    # class-level variable to store single instance of the class
    _instance = None
    # class-level lock to ensure thread safety
    _lock = threading.Lock()

    # Class method to get the SingletonLogger instance
    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
                cls._instance._initialize_logger()
            return cls._instance

    # Helper method to initialize logger
    def _initialize_logger(self):
        # create a logger object with specified name
        self.logger = logging.getLogger('my_logger')
        self.logger.setLevel(logging.DEBUG)

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
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

# Usage
logger = SingletonLogger.get_instance().logger
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')