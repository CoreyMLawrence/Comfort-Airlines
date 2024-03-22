# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Anthony Cox, Will Wadsworth
# Date: 3/9/2024
#
# Description:
#   This module tests the model class `Aircraft`.

# Import necessary libraries and modules
import pytest
from decimal import Decimal
from queue import Queue
from models.aircraft import Airport, Aircraft, AircraftType, AircraftStatus, AircraftFactory

@pytest.mark.parametrize("name, type, status, location, tail_number, passenger_capacity, cruise_speed, fuel_level, fuel_capacity, fuel_efficiency, wait_timer, max_range", 
    [
        ("Boeing 737-600", AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None, "N00000", 119, 1101, 6300, 6875, 0.55, 0, 5648),
        ("Boeing 767-800", AircraftType.BOEING_737_800, AircraftStatus.AVAILABLE, None, "N00001", 189, 1101, 500, 6875, 0.44, 0, 5665),
        ("Airbus A200-100", AircraftType.AIRBUS_A200_100, AircraftStatus.AVAILABLE, None, "N00002", 135, 1012, 5020, 5790, 0.57, 0, 5460),
        ("Airbus A220-300", AircraftType.AIRBUS_A220_300, AircraftStatus.AVAILABLE, None, "N00003", 160, 1012, 0, 5790, 0.66, 0, 5920),
    ]
)
def test_aircraft_factory_create_aircraft(name, type, status, location, tail_number, passenger_capacity, cruise_speed, fuel_level, fuel_capacity, fuel_efficiency, wait_timer, max_range) -> None:
    """AircraftFactory.createAircraft() method test. Asserts that passing in the aircraft type correctly yields an aircraft with the correct information"""
    aircraft: Aircraft = AircraftFactory.create_aircraft(type, status, location, fuel_level)

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
    """Aircraft.__init__() method test. Tests that the aircraft class constructor protects against negative fuel levels"""
    _: Aircraft = AircraftFactory.create_aircraft(AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None, 0)
    
    with pytest.raises(ValueError):
        _: Aircraft = AircraftFactory.create_aircraft(AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None, -1)
        
@pytest.mark.parametrize("type, status, location, fuel_capacity", 
    [
        (AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None, 6875),
        (AircraftType.BOEING_737_800, AircraftStatus.AVAILABLE, None, 6875),
        (AircraftType.AIRBUS_A200_100, AircraftStatus.AVAILABLE, None, 5790),
        (AircraftType.AIRBUS_A220_300, AircraftStatus.AVAILABLE, None, 5790),
    ]
)
def test_aircraft_overfull_fuel_level(type, status, location,  fuel_capacity) -> None:
    """Aircraft.__init__() method test. Tests that the aircraft class constructor protects against fuel levels greater than the capacity of the aircraft"""
    _: Aircraft = AircraftFactory.create_aircraft(type, status, location, fuel_capacity)
    
    with pytest.raises(ValueError):
        _: Aircraft = AircraftFactory.create_aircraft(type, status, location, fuel_capacity + 1)

def test_aircraft_factory_create_aircraft_type_error() -> None:
    """AircraftFactory.createAircraft() method test. Asserts that the status and location"""
    _: Aircraft = AircraftFactory.create_aircraft(AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, 
                                                  Airport("John F. Kennedy International Airport", "JFK", "New York City", "New York", 18713220, 
                                                          False, 5, 40.6413, -73.7781, 2.50, Decimal('1000.00'), Decimal('500.00'), Queue()), 0)
    _: Aircraft = AircraftFactory.create_aircraft(AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None, 0)
    
    with pytest.raises(TypeError):
        _: Aircraft = AircraftFactory.create_aircraft("not an AircraftType error", AircraftStatus.AVAILABLE, None, 0)

def test_aircraft_factory_create_aircraft_range_error() -> None:
    """AircraftFactory.createAircraft() method test. Asserts that an enumerated type passed is checked if in the range of the enum"""
    with pytest.raises(ValueError):
        _ = AircraftFactory.create_aircraft(AircraftType(100))
