import pytest
from creational.abstract_factory.shipment import (
    LandShipment,
    AirShipment,
    SeaShipment,
    ShipmentType,
    ShipmentFactory,
    IShipment
)


# Test LandShipment
def test_land_shipment(capfd):
    handler = LandShipment()
    handler.process_shipment("details")
    captured = capfd.readouterr()
    assert captured.out == "Processing land shipment: details\n"


# Test AirShipment
def test_air_shipment(capfd):
    handler = AirShipment()
    handler.process_shipment("details")
    captured = capfd.readouterr()
    assert captured.out == "Processing air shipment: details\n"


# Test SeaShipment
def test_sea_shipment(capfd):
    handler = SeaShipment()
    handler.process_shipment("details")
    captured = capfd.readouterr()
    assert captured.out == "Processing sea shipment: details\n"


# Test ShipmentFactory
def test_shipment_factory():
    factory = ShipmentFactory()
    assert isinstance(factory.create_shipment(ShipmentType.LAND), IShipment)
    assert isinstance(factory.create_shipment(ShipmentType.AIR), IShipment)
    assert isinstance(factory.create_shipment(ShipmentType.SEA), IShipment)
    with pytest.raises(ValueError):
        factory.create_shipment(ShipmentType('unknown'))


# Additional test cases can be added to cover more scenarios or edge cases as needed.

if __name__ == "__main__":
    pytest.main()
