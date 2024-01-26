from enum import Enum
from copy import deepcopy

class AircraftType(Enum):
    """Enumerated type. Defines the 4 types of aircraft"""
    BOEING_737_600 = 0
    BOEING_737_800 = 1
    AIRBUS_A200_100 = 2
    AIRBUS_A220_300 = 3

class Aircraft:
    """Model class. A generic representation of an aircraft. Type is indicated by AirCraft.Type"""
    def __init__(self, name: str, type: AircraftType, passenger_capacity: int, cruise_speed: int, fuel_capacity: int, max_range: int, max_altitude: int) -> None:
        self.name = name
        self.type = type
        self.passenger_capacity = passenger_capacity
        self.cruise_speed = cruise_speed                # km / h
        self.fuel_capacity = fuel_capacity              # gallons
        self.max_range = max_range                      # km
        self.max_altitude = max_altitude                # feet

BOEING_737_600_TEMPLATE = Aircraft("Boeing 737-600", AircraftType.BOEING_737_600,  119, 969, 6875, 5648, 41000)
BOEING_737_800_TEMPLATE = Aircraft("Boeing 767-800", AircraftType.BOEING_737_800,  189, 969, 6875, 5665, 41000)
AIRBUS_A200_100_TEMPLATE = Aircraft("Airbus A200-100", AircraftType.AIRBUS_A200_100, 135, 910, 5790, 5460, 41000)
AIRBUS_A220_300_TEMPLATE = Aircraft("Airbus A220-300", AircraftType.AIRBUS_A220_300, 160, 910, 5790, 5920, 41000)

def aircraft_factory(aircraft_type: AircraftType) -> Aircraft:
    """Factory class to create Aircraft objects. Uses AircraftType as the API."""
    if not type(aircraft_type) is AircraftType:
        raise TypeError(f"parameter 'aircraft_type' is not of enum type 'AircraftType'. Found type: {type(aircraft_type)}")

    match aircraft_type:
        case AircraftType.BOEING_737_600:
            return deepcopy(BOEING_737_600_TEMPLATE)
        case AircraftType.BOEING_737_800:
            return deepcopy(BOEING_737_800_TEMPLATE)
        case AircraftType.AIRBUS_A200_100:
            return deepcopy(AIRBUS_A200_100_TEMPLATE)
        case AircraftType.AIRBUS_A220_300:
            return deepcopy(AIRBUS_A220_300_TEMPLATE)
        case _:
            raise ValueError(f"parameter 'aircraft_type' not in range of AircraftType enum.")
