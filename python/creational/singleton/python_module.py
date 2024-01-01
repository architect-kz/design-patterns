"""
Gang of Four:

Modules are “singletons” in Python because import only creates a single copy of each module;
subsequent imports of the same name keep returning the same module object.
https://python-patterns.guide/gang-of-four/singleton/
"""


class Logger:
    def __init__(self):
        print("Initializing Logger...")
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"Log: {message}")

    def show_logs(self):
        return self.logs


# this variable is used to test the singleton pattern
logger = Logger()
