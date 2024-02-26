from abc import abstractmethod, ABC


class Chair:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Ordered {self.name} chair'


class Table:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Ordered {self.name} table'


class IFurnitureFactory(ABC):
    @abstractmethod
    def create_table(self) -> Table:
        pass

    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class WoodenFurnitureFactory(IFurnitureFactory):
    __name = 'Wooden'

    def create_table(self) -> Table:
        return Table(self.__name)

    def create_chair(self) -> Chair:
        return Chair(self.__name)

    @property
    def name(self) -> str:
        return self.__name


class MetalFurnitureFactory(IFurnitureFactory):
    __name = 'Metal'

    def create_table(self) -> Table:
        return Table(self.__name)

    def create_chair(self) -> Chair:
        return Chair(self.__name)

    @property
    def name(self) -> str:
        return self.__name


def order_furniture(furniture: IFurnitureFactory) -> None:
    print(f'** Creating {furniture.name} furniture **\n')
    chair = furniture.create_chair()
    table = furniture.create_table()

    print(chair)
    print(table)
    print('\n')


if __name__ == '__main__':
    wooden_factory = WoodenFurnitureFactory()
    metal_factory = MetalFurnitureFactory()

    order_furniture(wooden_factory)
    order_furniture(metal_factory)
