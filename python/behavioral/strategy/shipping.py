from abc import ABC, abstractmethod


# Абстрактный класс стратегии расчета стоимости доставки
class IShippingCostStrategy(ABC):
    @abstractmethod
    def calculate(self, order) -> float:
        pass


# Конкретные реализации стратегий расчета стоимости доставки
class StandardShipping(IShippingCostStrategy):
    def calculate(self, order) -> float:
        # Пример расчета стоимости стандартной доставки
        weight = order['weight']
        return 5 + weight * 0.5  # Базовая стоимость + стоимость за кг


class ExpressShipping(IShippingCostStrategy):
    def calculate(self, order) -> float:
        # Пример расчета стоимости экспресс доставки
        weight = order['weight']
        return 10 + weight * 1.5  # Базовая стоимость + стоимость за кг (больше, чем для стандартной)


class FreeShipping(IShippingCostStrategy):
    def calculate(self, order) -> float:
        # Бесплатная доставка
        return 0


# Класс контекста
class ShippingCostCalculator:
    def __init__(self, shipping_strategy: IShippingCostStrategy | None = None):
        self.shipping_strategy: IShippingCostStrategy = shipping_strategy

    def calculate_shipping_cost(self, order):
        return self.shipping_strategy.calculate(order)

    def set_shipping_strategy(self, shipping_strategy: IShippingCostStrategy):
        self.shipping_strategy: IShippingCostStrategy = shipping_strategy
