import pytest
from behavioral.observer.kaspi_product import KaspiProduct, Sulpak, TechnoDom


class MockSulpak(Sulpak):
    def __init__(self):
        super().__init__()
        self.update_called = False

    def update(self, product):
        super().update(product)
        self.update_called = True


def test_product_initial_price():
    product = KaspiProduct(10000)
    assert product.price == 10000


def test_add_remove_observer():
    product = KaspiProduct(10000)
    sulpak = MockSulpak()
    techno_dom = TechnoDom()

    product.add_observer(sulpak)
    product.add_observer(techno_dom)

    assert len(product.observers) == 2

    product.remove_observer(sulpak)
    assert len(product.observers) == 1


def test_change_price_notifies_observers():
    product = KaspiProduct(10000)
    sulpak = MockSulpak()
    techno_dom = TechnoDom()

    product.add_observer(sulpak)
    product.add_observer(techno_dom)

    with pytest.raises(TypeError):
        product.change_price('not an int')

    product.change_price(9000)
    assert sulpak.update_called


def test_observer_updates():
    product = KaspiProduct(10000)
    sulpak = MockSulpak()

    product.add_observer(sulpak)
    product.change_price(11000)
    assert sulpak.update_called


if __name__ == '__main__':
    pytest.main()
