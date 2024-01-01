class Singleton(type):
    """
    A meta class that creates a Singleton base class when called.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Overrides the default __call__ method to control the instantiation of the class.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    """
    A logger class for logging messages. This class is a singleton, ensuring that only one logger instance is used
    throughout the application.
    """

    def __init__(self):
        print("Initializing Logger...")
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"Log: {message}")

    def show_logs(self):
        return self.logs
