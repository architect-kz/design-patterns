# Handlers
from abc import ABC, abstractmethod
from enum import Enum


class IHandler(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass


class CardHandler(IHandler):
    def process_payment(self, amount: float):
        print(f'Processing via card: {amount}')


class WalletHandler(IHandler):
    def process_payment(self, amount: float):
        print(f'Processing via wallet: {amount}')


class BankTransferHandler(IHandler):
    def process_payment(self, amount: float):
        print(f'Processing via bank transfer: {amount}')


# Payment types
class PaymentType(str, Enum):
    CARD = 'card'
    WALLET = 'wallet'
    BANK_TRANSFER = 'bank_transfer'


# Factories
class IPaymentFactory(ABC):
    @abstractmethod
    def create_payment_handler(self, payment_type: PaymentType):
        pass


class PaymentFactory(IPaymentFactory):
    HANDLERS = {
        PaymentType.CARD: CardHandler,
        PaymentType.WALLET: WalletHandler,
        PaymentType.BANK_TRANSFER: BankTransferHandler
    }

    def create_payment_handler(self, payment_type: PaymentType) -> IHandler:
        handler_class = self.HANDLERS.get(payment_type)

        if handler_class:
            return handler_class()

        raise ValueError(f'Unknown payment type: {payment_type}')


if __name__ == "__main__":
    amount = 1000
    handlers = ('card', 'wallet', 'bank_transfer', 'unknown')
    factory = PaymentFactory()

    for handler_name in handlers:
        try:
            handler = factory.create_payment_handler(PaymentType(handler_name))
            handler.process_payment(amount)
        except Exception as e:
            print(f'Failed to process {handler_name}: {e}')
