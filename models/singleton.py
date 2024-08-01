
class Singleton(type):
    """
    Singleton provide a global point of access to one instance and it's responsible to create that instance.
    This has to be use as a metaclass, ie: class Logger(metaclass=Singleton)
    It will not allow to create multiple instances of the same class, instead it will return the existent one.
    Use with caution, the Singleton pattern is for specific use cases, ie: web/db connections, buffer, device access, logs
    """
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
