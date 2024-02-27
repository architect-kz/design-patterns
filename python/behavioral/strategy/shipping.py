import pytest


# Абстрактный класс стратегии расчета стоимости доставки
class ShippingCostStrategy:
    def calculate(self, order):
        pass


# Конкретные реализации стратегий расчета стоимости доставки
class StandardShipping(ShippingCostStrategy):
    def calculate(self, order):
        # Пример расчета стоимости стандартной доставки
        weight = order['weight']
        return 5 + weight * 0.5  # Базовая стоимость + стоимость за кг


class ExpressShipping(ShippingCostStrategy):
    def calculate(self, order):
        # Пример расчета стоимости экспресс доставки
        weight = order['weight']
        return 10 + weight * 1.5  # Базовая стоимость + стоимость за кг (больше, чем для стандартной)


class FreeShipping(ShippingCostStrategy):
    def calculate(self, order):
        # Бесплатная доставка
        return 0


# Класс контекста
class ShippingCostCalculator:
    def __init__(self, shipping_strategy):
        self.shipping_strategy = shipping_strategy

    def calculate_shipping_cost(self, order):
        return self.shipping_strategy.calculate(order)


# Тесты
@pytest.mark.parametrize("order, expected_cost", [
    ({"weight": 1}, 5.5),  # Ожидаемая стоимость для стандартной доставки с весом 1 кг
    ({"weight": 1}, 11.5),  # Ожидаемая стоимость для экспресс доставки с весом 1 кг
    ({"weight": 1}, 0),  # Ожидаемая стоимость для бесплатной доставки
])
def test_shipping_cost_calculator(order, expected_cost):
    standard_shipping_calculator = ShippingCostCalculator(StandardShipping())
    express_shipping_calculator = ShippingCostCalculator(ExpressShipping())
    free_shipping_calculator = ShippingCostCalculator(FreeShipping())

    assert standard_shipping_calculator.calculate_shipping_cost(order) == expected_cost
    assert express_shipping_calculator.calculate_shipping_cost(order) == expected_cost
    assert free_shipping_calculator.calculate_shipping_cost(order) == expected_cost


if __name__ == "__main__":
    pytest.main()
