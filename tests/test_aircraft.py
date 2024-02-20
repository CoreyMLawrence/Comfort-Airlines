import pytest
from src.aircraft import Aircraft, AircraftType, AircraftStatus, AircraftFactory

@pytest.mark.parametrize("name, type, status, location, tail_number, passenger_capacity, cruise_speed, fuel_level, fuel_capacity, fuel_efficiency, wait_timer, max_range", 
    [
        ("Boeing 737-600", AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None, "CA0000", 119, 1101, 6300, 6875, 0.55, 0, 5648),
        ("Boeing 767-800", AircraftType.BOEING_737_800, AircraftStatus.AVAILABLE, None, "CA0000", 189, 1101, 500, 6875, 0.44, 0, 5665),
        ("Airbus A200-100", AircraftType.AIRBUS_A200_100, AircraftStatus.AVAILABLE, None, "CA0000", 135, 1012, 5020, 5790, 0.57, 0, 5460),
        ("Airbus A220-300", AircraftType.AIRBUS_A220_300, AircraftStatus.AVAILABLE, None, "CA0000", 160, 1012, 0, 5790, 0.66, 0, 5920),
    ]
)
def test_aircraft_init(name, type, status, location, tail_number, passenger_capacity, cruise_speed, fuel_level, fuel_capacity, fuel_efficiency, wait_timer, max_range) -> None:
    aircraft_factory = AircraftFactory()
    aircraft: Aircraft = aircraft_factory(type, status, location, fuel_level)

    assert aircraft.name == name
    assert aircraft.type == type
    assert aircraft.status == status
    assert aircraft.location == location
    assert aircraft.tail_number == tail_number
    assert aircraft.passenger_capacity == passenger_capacity
    assert aircraft.cruise_speed == cruise_speed
    assert aircraft.fuel_level == fuel_level
    assert aircraft.fuel_capacity == fuel_capacity
    assert aircraft.fuel_efficiency == fuel_efficiency
    assert aircraft.wait_timer == wait_timer
    assert aircraft.max_range == max_range
        
def test_aircraft_negative_fuel_level() -> None:
    aircraft_factory = AircraftFactory()
    
    _: Aircraft = aircraft_factory(AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None, 0)
    
    with pytest.raises(ValueError):
        _: Aircraft = aircraft_factory(AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None, -1)
        
@pytest.mark.parametrize("type, status, location, fuel_capacity", 
    [
        (AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None, 6875),
        (AircraftType.BOEING_737_800, AircraftStatus.AVAILABLE, None, 6875),
        (AircraftType.AIRBUS_A200_100, AircraftStatus.AVAILABLE, None, 5790),
        (AircraftType.AIRBUS_A220_300, AircraftStatus.AVAILABLE, None, 5790),
    ]
)
def test_aircraft_overfull_fuel_level(type, status, location,  fuel_capacity) -> None:
    aircraft_factory = AircraftFactory()
    
    _: Aircraft = aircraft_factory(type, status, location, fuel_capacity)
    
    with pytest.raises(ValueError):
        _: Aircraft = aircraft_factory(type, status, location, fuel_capacity + 1)

def test_aircraft_type_error() -> None:
    aircraft_factory = AircraftFactory()
    
    with pytest.raises(TypeError):
        _: Aircraft = aircraft_factory("not an AircraftType error")

def test_aircraft_range_error() -> None:
    aircraft_factory = AircraftFactory()
    
    with pytest.raises(ValueError):
        _ = aircraft_factory(AircraftType(100))
