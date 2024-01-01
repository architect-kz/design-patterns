from creational.singleton.function_decorator import Logger


class TestSingleton:
    def test_singleton_as_function_decorator(self):
        logger_1 = Logger()
        logger_2 = Logger()

        assert logger_1 is logger_2
        assert id(logger_1) == id(logger_2)
