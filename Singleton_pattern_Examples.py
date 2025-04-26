import threading

# ----- Classic GoF Singleton -----
class ClassicSingleton:
    # class-level variable to store single class instance
    _instance = None

    # override the __init__ method to control initialization
    def __init__(self):
        print('<init> called...')
        # raise an error to prevent constructor utilization
        raise RuntimeError('Call get_instance() instead.')

    @classmethod
    def  get_instance(cls):
        print('<get_instance> called...')
        if not cls._instance:  # NOTE: lazy instantiation
            # create new instance of the class
            cls._instance = cls.__new__(cls)
        # return the single instance of the class, either newly created one or existing one
        return cls._instance

# s0 = ClassicSingleton.get_instance()
# s1 = ClassicSingleton.get_instance()
#
# print(s0 is s1)
# print(s0)
# print(s1)


# ----- Simple Singleton implementation in Python -----
class SimplePythonSingleton:
    # class-level variable to store single instance of the class
    _instance = None

    # override __new__ method to control how new objects are created
    def __new__(cls, *args, **kwargs):
        print('<new> creating...')
        # check if instance of class has been created before. NOTE: lazy instantiation
        if not cls._instance:
            # create new instance of class and store it in _instance
            cls._instance = super().__new__(cls)
        # return single instance of class, either newly created or existing one
        return cls._instance

    def __init__(self):
        print('<init> called...')

# s1 = SimplePythonSingleton()
# s2 = SimplePythonSingleton()
# print(s1 is s2)
# print(s1)
# print(s2)


# ----- Best Singleton implementation in Python (META) -----
class SingletonMeta(type):
    # Dictionary stores single instance of the class for each subclass of the SingletonMeta metaclass
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print('<call meta> calling...')
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

# s1 = Singleton()
# s2 = Singleton()
# print(s1 is s2)
# print(s1)
# print(s2)



# ----- Best Singleton implementation in Python with Eager Loading  (INIT override)-----
class EagerSingletonMetaInit(type):
    # Dictionary stores single instance of the class for each subclass of the EagerSingletonMeta metaclass
    _instances = {}

    # override: called during creation of sub-types
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        # Eager loading of the class instance
        cls._instances[cls] = super().__call__()
        print('initializing <super meta with init>...')

    # returns the singleton instance
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

# our actual EagerSingleton class:
class EagerSingletonInit(metaclass=EagerSingletonMetaInit):
    def __init__(self):
        print('initializing <child with init>...')
        self.attribute = "I'm a Singleton"

# s1 = EagerSingletonInit()
# s2 = EagerSingletonInit()
#
# print(s1.attribute)
# print(s2.attribute)
#
# print(s1 is s2)



# ----- Best Singleton implementation in Python with Eager Loading (NEW override)-----
class EagerSingletonMetaNew(type):
    # Dictionary stores single instance of the class for each subclass of the EagerSingletonMeta metaclass
    _instances = {}

    # override: called during creation of sub-types
    def __new__(cls, *args, **kwargs):
        print('initializing <super meta with new>...')
        new_class = super().__new__(cls, *args, **kwargs)
        # Eager loading of the class instance
        cls._instances[new_class] = super(EagerSingletonMetaNew, new_class).__call__()
        return new_class

    # returns the singleton instance
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

# our actual EagerSingleton class:
class EagerSingletonNew(metaclass=EagerSingletonMetaNew):
    def __init__(self):
        print('initializing <child with new>...')
        self.attribute = "I'm a Singleton"

# s1 = EagerSingletonNew()
# s2 = EagerSingletonNew()
#
# print(s1.attribute)
# print(s2.attribute)
#
# print(s1 is s2)


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

# s1 = ThreadSafeSingleton()
# s2 = ThreadSafeSingleton()
#
# print(s1 is s2)
# print(s1)
# print(s2)


# ----- Thread-Safe Singleton implementation in Python (META)-----
class ThreadSafeSingletonMeta(type):
    # class-level variable to store single instance of the class
    _instance = None
    # class-level lock to ensure thread safety
    _lock = threading.Lock()

    # override __new__ method to control how new objects are created
    def __call__(cls, *args, **kwargs):
        # acquire the lock to ensure thread safety
        with cls._lock:
            # check if instance of class has been created before. NOTE: lazy instantiation
            if not cls._instance:
                # create new instance of class and store it in _instance
                cls._instance = super().__call__(*args, **kwargs)
        # return single instance of class, either newly created or existing one
        return cls._instance

# Define a Singleton class with SingletonMeta as its metaclass
class ThreadSingleton(metaclass=ThreadSafeSingletonMeta):
    pass

def get_singleton_instance():
    s = ThreadSingleton()
    print(s)

# Create a list to store threads
threads = []
# Create 10 thread objects, appending each to the thread list
for i in range(10):
    t = threading.Thread(target=get_singleton_instance)
    threads.append(t)

# Start each thread in the threads list
for t in threads:
    t.start()

# Wait for each thread to finish
for t in threads:
    t.join()