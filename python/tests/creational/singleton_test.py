from creational.singleton.function_decorator import Logger as FunctionDecoratorLogger
from creational.singleton.metaclass import Logger as MetaLogger
from creational.singleton.python_module import logger as python_module_logger1
from creational.singleton.python_module import logger as python_module_logger2


class TestSingleton:
    def test_singleton_as_function_decorator(self):
        logger_1 = FunctionDecoratorLogger()
        logger_2 = FunctionDecoratorLogger()

        assert logger_1 is logger_2
        assert id(logger_1) == id(logger_2)

    def test_singleton_as_metaclass(self):
        logger_1 = MetaLogger()
        logger_2 = MetaLogger()

        assert logger_1 is logger_2
        assert id(logger_1) == id(logger_2)

    def test_singleton_as_python_module(self):
        assert python_module_logger1 is python_module_logger2
        assert id(python_module_logger1) == id(python_module_logger2)
