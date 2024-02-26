from __future__ import annotations
from abc import ABC, abstractmethod


class AccessHandlerBase(ABC):
    _successor = None

    def set_next(self, successor: AccessHandlerBase) -> AccessHandlerBase:
        self._successor = successor

        return successor

    @abstractmethod
    def handle(self, request):
        if self._successor:
            return self._successor.handle(request)

        return None


class BasicAccessHandler(AccessHandlerBase):
    NAME = 'basic'

    def handle(self, request):
        if request == self.NAME:
            print('Basic access granted')
        else:
            return super().handle(request)


class PremiumAccessHandler(AccessHandlerBase):
    NAME = 'premium'

    def handle(self, request):
        if request == self.NAME:
            print('Premium access granted')
        else:
            return super().handle(request)


class AdminAccessHandler(AccessHandlerBase):
    NAME = 'admin'

    def handle(self, request):
        if request == self.NAME:
            print('Admin access granted')
        else:
            return super().handle(request)


if __name__ == "__main__":
    basic_handler = BasicAccessHandler()
    premium_handler = PremiumAccessHandler()
    admin_handler = AdminAccessHandler()

    admin_handler.set_next(premium_handler).set_next(basic_handler)

    requests = ('basic', 'admin')
    for request in requests:
        admin_handler.handle(request)
