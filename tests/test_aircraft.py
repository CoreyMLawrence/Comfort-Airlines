import pytest
from src.aircraft import Aircraft, AircraftType, aircraft_factory

@pytest.mark.parametrize("name, type, passenger_capacity, cruise_speed, fuel_capacity, max_range, max_altitude", 
    [
        ("Boeing 737-600", AircraftType.BOEING_737_600, 119, 969, 6875, 5648, 41000),
        ("Boeing 767-800", AircraftType.BOEING_737_800, 189, 969, 6875, 5665, 41000),
        ("Airbus A200-100", AircraftType.AIRBUS_A200_100, 135, 910, 5790, 5460, 41000),
        ("Airbus A220-300", AircraftType.AIRBUS_A220_300, 160, 910, 5790, 5920, 41000),
    ]
)
def test_aircraft(name, type, passenger_capacity, cruise_speed, fuel_capacity, max_range, max_altitude) -> None:
    aircraft = aircraft_factory(type)

    assert aircraft.name == name
    assert aircraft.type == type
    assert aircraft.passenger_capacity == passenger_capacity
    assert aircraft.cruise_speed == cruise_speed
    assert aircraft.fuel_capacity == fuel_capacity
    assert aircraft.max_range == max_range
    assert aircraft.max_altitude == aircraft.max_altitude

def test_aircraft_type_error() -> None:
    with pytest.raises(TypeError):
        aircraft_factory("not an AircraftType error")

def test_aircraft_range_error() -> None:
    with pytest.raises(ValueError):
        aircraft_factory(AircraftType(100))
