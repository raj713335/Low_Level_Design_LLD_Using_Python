# Using class Variable

class singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(singleton, cls).__new__(cls)
        return cls._instance


s1 = singleton()
s2 = singleton()

print(s1 is s2)


# Using a decorator

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Logger:
    pass


logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)


# Using a Meta class

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=SingletonMeta):
    pass


c1 = Config()
c2 = Config()

print(c1 is c2)
