import pytest
from behavioral.chain_of_responsibility.access import (
    BasicAccessHandler,
    PremiumAccessHandler,
    AdminAccessHandler
)


# Test BasicAccessHandler
def test_basic_access_handler(capfd):
    handler = BasicAccessHandler()
    handler.handle('basic')
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Basic access granted'

    handler.handle('premium')
    captured = capfd.readouterr()
    assert captured.out.strip() == ''


# Test PremiumAccessHandler
def test_premium_access_handler(capfd):
    handler = PremiumAccessHandler()
    handler.handle('premium')
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Premium access granted'

    handler.handle('admin')
    captured = capfd.readouterr()
    assert captured.out.strip() == ''


# Test AdminAccessHandler
def test_admin_access_handler(capfd):
    handler = AdminAccessHandler()
    handler.handle('admin')
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Admin access granted'

    handler.handle('basic')
    captured = capfd.readouterr()
    assert captured.out.strip() == ''


# Test chain of responsibility
def test_chain_of_responsibility(capfd):
    basic_handler = BasicAccessHandler()
    premium_handler = PremiumAccessHandler()
    admin_handler = AdminAccessHandler()

    admin_handler.set_next(premium_handler).set_next(basic_handler)

    admin_handler.handle('basic')
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Basic access granted'

    admin_handler.handle('premium')
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Premium access granted'

    admin_handler.handle('admin')
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Admin access granted'

    admin_handler.handle('guest')
    captured = capfd.readouterr()
    assert captured.out.strip() == ''


# Additional test cases can be added to cover more scenarios or edge cases as needed.

if __name__ == "__main__":
    pytest.main()
