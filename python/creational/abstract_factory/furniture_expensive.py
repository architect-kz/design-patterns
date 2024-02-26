from abc import ABC, abstractmethod


class IChair(ABC):
    @abstractmethod
    def sit_on(self) -> None:
        pass


class ISofa(ABC):
    @abstractmethod
    def lie_on(self) -> None:
        pass


class ICoffeeTable(ABC):
    @abstractmethod
    def place_on(self) -> None:
        pass


class IFurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> IChair:
        pass

    @abstractmethod
    def create_sofa(self) -> ISofa:
        pass

    @abstractmethod
    def create_coffee_table(self) -> ICoffeeTable:
        pass


# Concrete products
class VictorianChair(IChair):
    def sit_on(self) -> None:
        print("Sitting on a Victorian Chair")


class VictorianSofa(ISofa):
    def lie_on(self) -> None:
        print("Lying on a Victorian Sofa")


class VictorianCoffeeTable(ICoffeeTable):
    def place_on(self) -> None:
        print("Placing items on a Victorian Coffee Table")


class ModernChair(IChair):
    def sit_on(self) -> None:
        print("Sitting on a Modern Chair")


class ModernSofa(ISofa):
    def lie_on(self) -> None:
        print("Lying on a Modern Sofa")


class ModernCoffeeTable(ICoffeeTable):
    def place_on(self) -> None:
        print("Placing items on a Modern Coffee Table")


class VictorianFurnitureFactory(IFurnitureFactory):
    def create_chair(self) -> VictorianChair:
        return VictorianChair()

    def create_sofa(self) -> VictorianSofa:
        return VictorianSofa()

    def create_coffee_table(self) -> VictorianCoffeeTable:
        return VictorianCoffeeTable()


class ModernFurnitureFactory(IFurnitureFactory):
    def create_chair(self) -> ModernChair:
        return ModernChair()

    def create_sofa(self) -> ModernSofa:
        return ModernSofa()

    def create_coffee_table(self) -> ModernCoffeeTable:
        return ModernCoffeeTable()


def order_furniture(factory: IFurnitureFactory) -> None:
    print(f'** Using {factory.__class__.__name__} **\n')
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    coffee_table = factory.create_coffee_table()

    chair.sit_on()
    sofa.lie_on()
    coffee_table.place_on()
    print('\n')


# Usage
if __name__ == "__main__":
    victorian_factory = VictorianFurnitureFactory()
    order_furniture(victorian_factory)

    modern_factory = ModernFurnitureFactory()
    order_furniture(modern_factory)
