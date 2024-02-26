# Handlers
from abc import ABC, abstractmethod
from enum import Enum


class IShipment(ABC):
    @abstractmethod
    def process_shipment(self, details: str):
        pass


class LandShipment(IShipment):
    def process_shipment(self, details: str):
        print(f'Processing land shipment: {details}')


class AirShipment(IShipment):
    def process_shipment(self, details: str):
        print(f'Processing air shipment: {details}')


class SeaShipment(IShipment):
    def process_shipment(self, details: str):
        print(f'Processing sea shipment: {details}')


# Factories
class ShipmentType(str, Enum):
    LAND = 'land'
    AIR = 'air'
    SEA = 'sea'


class IShipmentFactory(ABC):
    @abstractmethod
    def create_shipment(self, shipment_type: ShipmentType):
        pass


class ShipmentFactory(IShipmentFactory):
    HANDLERS = {
        ShipmentType.LAND: LandShipment,
        ShipmentType.AIR: AirShipment,
        ShipmentType.SEA: SeaShipment
    }

    def create_shipment(self, shipment_type: ShipmentType) -> IShipment:
        handler_class = self.HANDLERS.get(shipment_type)

        if handler_class:
            return handler_class()

        raise ValueError(f'Unknown shipment type: {shipment_type}')


if __name__ == "__main__":
    handlers = ('land', 'air', 'sea', 'unknown')
    factory = ShipmentFactory()

    for handler_name in handlers:
        try:
            handler = factory.create_shipment(ShipmentType(handler_name))
            handler.process_shipment(handler_name)
        except Exception as e:
            print(f'Failed to process {handler_name}: {e}')
