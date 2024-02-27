from abc import ABC, abstractmethod


class ICoffee(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class Espresso(ICoffee):
    def get_cost(self) -> float:
        return 2.0

    def get_description(self) -> str:
        return "Espresso"


# Decorators
class MilkDecorator(ICoffee):
    def __init__(self, coffee: ICoffee):
        self._coffee = coffee

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 1.0

    def get_description(self) -> str:
        return self._coffee.get_description() + ", Milk"


class SugarDecorator(ICoffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.5

    def get_description(self) -> str:
        return self._coffee.get_description() + ", Sugar"


if __name__ == "__main__":
    """
        Похоже на матрешку. 
        - Самый дорогой кофе (coffee_with_milk_and_sugar) декорирует кофе с молоком (coffee_with_milk)
        - Кофе с молоком декорирует эспрессо (coffee)
    """
    # Готовится эспрессо
    coffee = Espresso()
    print(f"Order: {coffee.get_description()}")
    print(f"Cost: ${coffee.get_cost()}")

    # На основе экспрессо готовится кофе с молоком (Латте, например)
    coffee_with_milk = MilkDecorator(coffee)
    print(f"Order: {coffee_with_milk.get_description()}")
    print(f"Cost: ${coffee_with_milk.get_cost()}")

    # Добавляется подсластитель в Латте
    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
    print(f"Order: {coffee_with_milk_and_sugar.get_description()}")
    print(f"Cost: ${coffee_with_milk_and_sugar.get_cost()}")
