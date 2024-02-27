import pytest
from behavioral.strategy.shipping import ShippingCostCalculator, StandardShipping, ExpressShipping, FreeShipping


@pytest.mark.parametrize("order, expected_cost, strategy", [
    ({"weight": 1}, 5.5, StandardShipping),  # Ожидаемая стоимость для стандартной доставки с весом 1 кг
    ({"weight": 1}, 11.5, ExpressShipping),  # Ожидаемая стоимость для экспресс доставки с весом 1 кг
    ({"weight": 1}, 0, FreeShipping),  # Ожидаемая стоимость для бесплатной доставки
])
def test_shipping_cost_calculator(order, expected_cost, strategy):
    shipping_calculator = ShippingCostCalculator()
    shipping_calculator.set_shipping_strategy(strategy())

    assert shipping_calculator.calculate_shipping_cost(order) == expected_cost


if __name__ == "__main__":
    pytest.main()
