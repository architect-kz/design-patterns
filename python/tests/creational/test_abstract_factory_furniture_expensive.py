import pytest
from creational.abstract_factory.furniture_expensive import (
    VictorianFurnitureFactory,
    ModernFurnitureFactory,
    order_furniture,
    VictorianChair,
    VictorianSofa,
    VictorianCoffeeTable,
    ModernChair,
    ModernSofa,
    ModernCoffeeTable,
    IFurnitureFactory,
    IChair,
    ISofa,
    ICoffeeTable,
)


# Test Victorian Furniture Factory
def test_victorian_factory_creation(capfd):
    victorian_factory = VictorianFurnitureFactory()
    order_furniture(victorian_factory)
    captured = capfd.readouterr()
    expected_output = (
        "** Using VictorianFurnitureFactory **\n\n"
        "Sitting on a Victorian Chair\n"
        "Lying on a Victorian Sofa\n"
        "Placing items on a Victorian Coffee Table\n\n\n"
    )
    assert captured.out == expected_output


# Test Modern Furniture Factory
def test_modern_factory_creation(capfd):
    modern_factory = ModernFurnitureFactory()
    order_furniture(modern_factory)
    captured = capfd.readouterr()
    expected_output = (
        "** Using ModernFurnitureFactory **\n\n"
        "Sitting on a Modern Chair\n"
        "Lying on a Modern Sofa\n"
        "Placing items on a Modern Coffee Table\n\n\n"
    )
    assert captured.out == expected_output


# Test interfaces
def test_interfaces():
    # Check if classes implement interfaces correctly
    assert issubclass(VictorianChair, IChair)
    assert issubclass(VictorianSofa, ISofa)
    assert issubclass(VictorianCoffeeTable, ICoffeeTable)
    assert issubclass(ModernChair, IChair)
    assert issubclass(ModernSofa, ISofa)
    assert issubclass(ModernCoffeeTable, ICoffeeTable)


# Additional test cases can be added to cover more scenarios or edge cases as needed.

if __name__ == "__main__":
    pytest.main()
