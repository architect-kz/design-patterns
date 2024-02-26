import pytest
from creational.abstract_factory.fastfood import (
    CheesePizza,
    VeggieBurger,
    VeggiePizza,
    AmericanFastFoodFactory,
    VegetarianFastFoodFactory,
    IPizza,
    IBurger,
    order_food
)


# Test factory creation of pizza
def test_american_factory_create_pizza():
    factory = AmericanFastFoodFactory()
    pizza = factory.create_pizza()
    assert isinstance(pizza, IPizza)
    assert isinstance(pizza, CheesePizza)


def test_vegetarian_factory_create_pizza():
    factory = VegetarianFastFoodFactory()
    pizza = factory.create_pizza()
    assert isinstance(pizza, IPizza)
    assert isinstance(pizza, VeggiePizza)


# Test factory creation of burger
def test_american_factory_create_burger():
    factory = AmericanFastFoodFactory()
    burger = factory.create_burger()
    assert isinstance(burger, IBurger)
    assert isinstance(burger, VeggieBurger)


def test_vegetarian_factory_create_burger():
    factory = VegetarianFastFoodFactory()
    burger = factory.create_burger()
    assert isinstance(burger, IBurger)
    assert isinstance(burger, VeggieBurger)


if __name__ == "__main__":
    pytest.main()
