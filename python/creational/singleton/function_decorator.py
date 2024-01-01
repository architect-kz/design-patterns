def singleton(cls):
    """
    A decorator that converts a class into a singleton by ensuring that only one instance of the class exists.

    When the decorated class is instantiated, this decorator checks if an instance already exists.
    If it does, the existing instance is returned. If not, a new instance is created and returned.

    Args:
        cls (class): The class to be made into a singleton.

    Returns:
        function: A wrapper function that manages the instantiation of the singleton class.
    """
    instances: dict = {}

    def get_instance(*args, **kwargs):
        """
        Wrapper function that manages the instantiation of the singleton class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            object: An instance of the singleton class.
        """
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Logger:
    """
    A logger class for logging messages. This class is a singleton, ensuring that only one logger instance is used
    throughout the application.
    """
    def __init__(self):
        print("Initializing Logger...")
        self.logs = []

