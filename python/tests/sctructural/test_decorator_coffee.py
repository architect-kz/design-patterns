import pytest
from structural.decorator.coffee import Espresso, MilkDecorator, SugarDecorator


def test_espresso():
    espresso = Espresso()
    assert espresso.get_description() == "Espresso"
    assert espresso.get_cost() == 2.0


def test_milk_decorator():
    espresso = Espresso()
    coffee_with_milk = MilkDecorator(espresso)
    assert coffee_with_milk.get_description() == "Espresso, Milk"
    assert coffee_with_milk.get_cost() == 3.0


def test_sugar_decorator():
    espresso = Espresso()
    coffee_with_milk = MilkDecorator(espresso)
    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
    assert coffee_with_milk_and_sugar.get_description() == "Espresso, Milk, Sugar"
    assert coffee_with_milk_and_sugar.get_cost() == 3.5


if __name__ == "__main__":
    pytest.main()
