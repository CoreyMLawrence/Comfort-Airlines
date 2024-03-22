# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Dylan Hudson
# Date: 3/21/2024
#
# Description:
#   This module tests the model class `Flight`.

# Import necessary libraries and modules
import pytest
from decimal import Decimal
from queue import Queue
from models.airport import Airport
from models.aircraft import Aircraft, AircraftType, AircraftStatus, AircraftFactory
from models.flight import Flight
from models.route import Route
from models.passenger import Passenger

# Setup test Aircraft
@pytest.fixture()
def aircraft_test() -> Aircraft:
    aircraft1: Aircraft = AircraftFactory.create_aircraft(AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None, 6300)
    return aircraft1

# Setup test Airports
@pytest.fixture()
def airport1() -> Airport:
    airport = Airport(
        "John F. Kennedy International Airport", "JFK", "New York City", "New York", 18713220, False, 5, 40.6413, 
        -73.7781, 2.50, Decimal('1000.00'), Decimal('500.00'), Queue()
    )
    return airport
@pytest.fixture()
def airport2() -> Airport:
    airport = Airport(
        "Dallas/Fort Worth International Airport", "DFW", "Dallas/Fort Worth", "Texas", 7233323, True, 11, 32.8998, 
        -97.0403, 2.65, Decimal('1100.00'), Decimal('550.00'), Queue()
    )
    return airport
    
# Setup test Route
@pytest.fixture()
def route_test(airport1, airport2) -> Route:
    route = Route(AircraftType.BOEING_737_600, airport1, airport2, 2215.6694092085722, 35, 220, 2503.7227066032797)
    return route
    
# Setup test Passengers
@pytest.fixture()
def passengers_test(airport1, airport2) -> list[Passenger]:
    passengers = [Passenger(airport1, airport2), Passenger(airport1, airport2), Passenger(airport1, airport2), 
                  Passenger(airport1, airport2), Passenger(airport1, airport2), Passenger(airport1, airport2)]
    return passengers

# Define the test function with parameterized inputs to test the constructor of Flight class
@pytest.mark.parametrize("flight_number, scheduled_time, expected_departure_time, expected_arrival_time", 
    [
        (1, 123, 163, 383)
    ]
)
def test_flight_constructor(
        flight_number, scheduled_time, aircraft_test, route_test, passengers_test, expected_departure_time, expected_arrival_time
    ) -> None:
    """Flight class constructor test. Asserts that the attributes are initialized correctly."""
    flight = Flight(flight_number, scheduled_time, aircraft_test, route_test, passengers_test, expected_departure_time, expected_arrival_time)

    assert flight.flight_number == flight_number
    assert flight.scheduled_time == scheduled_time
    assert flight.aircraft == aircraft_test
    assert flight.route == route_test
    assert flight.passengers == passengers_test
    assert flight.expected_departure_time == expected_departure_time
    assert flight.expected_arrival_time == expected_arrival_time
    
# Add more tests down here.
