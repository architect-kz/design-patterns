def singleton(cls):
    def get_instance(*args, **kwargs):
        return cls(*args, **kwargs)

    return get_instance


@singleton
class Logger:
    pass
