import pytest
from creational.abstract_factory.furniture import (
    WoodenFurnitureFactory,
    MetalFurnitureFactory,
    order_furniture
)


# Test creating Wooden furniture
def test_wooden_factory_creation(capfd):
    wooden_factory = WoodenFurnitureFactory()
    order_furniture(wooden_factory)
    captured = capfd.readouterr()
    assert captured.out == "** Creating Wooden furniture **\n\nOrdered Wooden chair\nOrdered Wooden table\n\n\n"


# Test creating Metal furniture
def test_metal_factory_creation(capfd):
    metal_factory = MetalFurnitureFactory()
    order_furniture(metal_factory)
    captured = capfd.readouterr()
    assert captured.out == "** Creating Metal furniture **\n\nOrdered Metal chair\nOrdered Metal table\n\n\n"


if __name__ == "__main__":
    pytest.main()
