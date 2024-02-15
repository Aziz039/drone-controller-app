'''
This is a singleton design pattern.
Acts as a blueprint to ensure there's only one instance of the DroneManager at any given time.
'''
class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]