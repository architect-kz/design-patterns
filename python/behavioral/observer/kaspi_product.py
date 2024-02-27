from __future__ import annotations
from abc import ABC, abstractmethod


class IObserver(ABC):
    """
    Интерфейс для наблюдателей.
    Все наблюдатели должны реализовывать интерфейс IObserver.
    """

    @abstractmethod
    def update(self, product: IObservable) -> None:
        pass


class IObservable(ABC):
    """ Интефейс для субъекта/издателя - то, за чем наблюдают"""

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None:
        """ Также можно назвать attach / detach"""
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def _notify_observers(self) -> None:
        pass


class KaspiProduct(IObservable):
    """
    За этим продуктом будут наблюдать наблюдатели.
    Подпишем на изменение цены продукта.

    Ваши наблюдатели могут в любой моменент постучаться вам в API
    и подписать / удалить себя из наблюдателей. Вы не паритесь. Это их дело.
    """

    def __init__(self, price: int):
        self.price = price
        self.observers: list[IObserver] = []

    def add_observer(self, observer: IObserver) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        self.observers.remove(observer)

    def _notify_observers(self) -> None:
        for observer in self.observers:
            observer.update(self)

    def change_price(self, new_price: int) -> None:
        if self.price != new_price:
            self.price = new_price
            self._notify_observers()


class Sulpak(IObserver):
    name: str = 'Sulpak'

    def update(self, product: KaspiProduct) -> None:
        if product.price > 10000:
            print(f'{self.name}: Цена продукта повышена на {product.price}, предложить рассрочку')
        else:
            print(f'{self.name}: Цена продукта уменьшена на {product.price}, пока все ок')


class TechnoDom(IObserver):
    name: str = 'Технодом'

    def update(self, product: KaspiProduct) -> None:
        if product.price > 10000:
            print(f'{self.name}: Цена продукта повышена на {product.price}, подсмотри что предложит Сулпак')
        else:
            print(f'{self.name}: Цена продукта уменьшена на {product.price}, не паримся')


if __name__ == '__main__':
    # Субъект для наблюдения. Издатель, на которого подписываются наблюдатели
    product = KaspiProduct(10000)

    # Любое количество наблюдателей тут:
    sulpak: IObserver = Sulpak()
    techno_dom: IObserver = TechnoDom()

    product.add_observer(sulpak)
    product.add_observer(techno_dom)

    # Уменьшим цену, наблюдатели получать уведомления.
    product.change_price(5000)
    print('\n')

    # Увеличем цену
    product.change_price(10001)
    print('\n')

    # Технодом не хочет больше наблюдать и стучиться вам в API
    product.remove_observer(techno_dom)
    product.change_price(10002)
