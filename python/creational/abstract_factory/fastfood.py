from abc import ABC, abstractmethod


class IPizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass


class IBurger:
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def wrap(self):
        pass


# Абстрактная фабрика
class IFastFoodFactory(ABC):
    @abstractmethod
    def create_pizza(self) -> IPizza:
        pass

    @abstractmethod
    def create_burger(self) -> IBurger:
        pass


class CheesePizza(IPizza):
    def prepare(self):
        print("Preparing Cheese Pizza")

    def bake(self):
        print("Baking Cheese Pizza")

    def cut(self):
        print("Cutting Cheese Pizza")

    def box(self):
        print("Boxing Cheese Pizza")


class VeggieBurger(IBurger):
    def prepare(self):
        print("Preparing Veggie Burger")

    def cook(self):
        print("Cooking Veggie Burger")

    def wrap(self):
        print("Wrapping Veggie Burger")


class VeggiePizza(IPizza):
    def prepare(self):
        print("Preparing Veggie Pizza")

    def bake(self):
        print("Baking Veggie Pizza")

    def cut(self):
        print("Cutting Veggie Pizza")

    def box(self):
        print("Boxing Veggie Pizza")


class AmericanFastFoodFactory(IFastFoodFactory):
    def create_pizza(self) -> IPizza:
        return CheesePizza()

    def create_burger(self) -> IBurger:
        return VeggieBurger()


class VegetarianFastFoodFactory(IFastFoodFactory):
    def create_pizza(self) -> IPizza:
        return VeggiePizza()

    def create_burger(self) -> IBurger:
        return VeggieBurger()


def order_food(factory):
    print("*** Fast food order ***")
    pizza = factory.create_pizza()
    burger = factory.create_burger()

    print("Pizza:")
    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()

    print("\nBurger:")
    burger.prepare()
    burger.cook()
    burger.wrap()

    print("\n")


if __name__ == "__main__":
    # Order for American Fast Food
    american_fastfood = AmericanFastFoodFactory()
    order_food(american_fastfood)

    # Order for Vegetarian Fast Food
    veggie_fastfood = VegetarianFastFoodFactory()
    order_food(veggie_fastfood)

    # You can make or combine any other products in any other factory.
    # ...
