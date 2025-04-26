import threading

# ----- Classic GoF Singleton -----
class ClassicSingleton:
    # class-level variable to store single class instance
    _instance = None

    # override the __init__ method to control initialization
    def __init__(self):
        # raise an error to prevent constructor utilization
        raise RuntimeError('Call instance() instead.')

    @classmethod
    def  get_instance(cls):
        if not cls._instance:  # NOTE: lazy instantiation
            # create new instance of the class
            cls._instance = cls.__new__(cls)
        # return the single instance of the class, either newly created one or existing one
        return cls._instance

# NOTE: s1 = ClassicSingleton.get_instance()  --> lazy instantiation


# ----- Simple Singleton implementation in Python -----
class SimplePythonSingleton:
    # class-level variable to store single instance of the class
    _instance = None

    # override __new__ method to control how new objects are created
    def __new__(cls, *args, **kwargs):
        # check if instance of class has been created before. NOTE: lazy instantiation
        if not cls._instance:
            # create new instance of class and store it in _instance
            cls._instance = super().__new__(cls)
        # return single instance of class, either newly created or existing one
        return cls._instance

# NOTE: s1 = SimplePythonSingleton()  --> lazy instantiation


# ----- Best Singleton implementation in Python -----
class SingletonMeta(type):
    # Dictionary stores single instance of the class for each subclass of the SingletonMeta metaclass
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # Single instance of the class already been created?
        if cls not in cls._instances:
            # Create instance by calling the __call__ method of the parent's (super().__call__())
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]

# our actual Singleton class:
class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        print('do some business here...')

# NOTE: s1 = Singleton()  --> lazy instantiation


# ----- Best Singleton implementation in Python with Eager Loading -----
class EagerSingletonMeta(type):
    # Dictionary stores single instance of the class for each subclass of the EagerSingletonMeta metaclass
    _instances = {}

    # override: called during creation of sub-types
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        # Eager loading of the class instance
        cls._instances[cls] = super().__call__()

    # returns the singleton instance
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

# our actual EagerSingleton class:
class EagerSingleton(metaclass=EagerSingletonMeta):
    def __init__(self):
        print('do some initialization here...')

# NOTE: s1 = EagerSingleton()  --> here is Eager loading inside.


# ----- Thread-Safe Singleton implementation in Python -----
class ThreadSafeSingleton:
    # class-level variable to store single instance of the class
    _instance = None
    # class-level lock to ensure thread safety
    _lock = threading.Lock()

    # override __new__ method to control how new objects are created
    def __new__(cls, *args, **kwargs):
        # acquire the lock to ensure thread safety
        with cls._lock:
            # check if instance of class has been created before. NOTE: lazy instantiation
            if not cls._instance:
                # create new instance of class and store it in _instance
                cls._instance = super().__new__(cls)
        # return single instance of class, either newly created or existing one
        return cls._instance

# NOTE: s1 = ThreadSafeSingleton()  --> thread-safe instantiation