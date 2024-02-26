import pytest
from creational.abstract_factory.payment import (
    CardHandler,
    WalletHandler,
    BankTransferHandler,
    PaymentType,
    PaymentFactory,
    IHandler
)


# Test CardHandler
def test_card_handler(capfd):
    handler = CardHandler()
    handler.process_payment(1000)
    captured = capfd.readouterr()
    assert captured.out == "Processing via card: 1000\n"


# Test WalletHandler
def test_wallet_handler(capfd):
    handler = WalletHandler()
    handler.process_payment(1000)
    captured = capfd.readouterr()
    assert captured.out == "Processing via wallet: 1000\n"


# Test BankTransferHandler
def test_bank_transfer_handler(capfd):
    handler = BankTransferHandler()
    handler.process_payment(1000)
    captured = capfd.readouterr()
    assert captured.out == "Processing via bank transfer: 1000\n"


# Test PaymentFactory
def test_payment_factory():
    factory = PaymentFactory()
    assert isinstance(factory.create_payment_handler(PaymentType.CARD), IHandler)
    assert isinstance(factory.create_payment_handler(PaymentType.WALLET), IHandler)
    assert isinstance(factory.create_payment_handler(PaymentType.BANK_TRANSFER), IHandler)
    with pytest.raises(ValueError):
        factory.create_payment_handler(PaymentType('unknown'))


# Additional test cases can be added to cover more scenarios or edge cases as needed.

if __name__ == "__main__":
    pytest.main()
