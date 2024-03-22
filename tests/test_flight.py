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
        (1, 123, 163, 383),
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
    assert flight.actual_departure_time == None
    assert flight.actual_arrival_time == None

# Test flight_number type
def test_flight_number_type_error(aircraft_test, route_test, passengers_test) -> None:
    with pytest.raises(TypeError):
        _: Flight = Flight("this is not an int", 123, aircraft_test, route_test, passengers_test, 163, 383)

# Test if negative flight_number
def test_flight_negative_flight_number(aircraft_test, route_test, passengers_test) -> None:
    _: Flight = Flight(0, 123, aircraft_test, route_test, passengers_test, 163, 383)
    
    with pytest.raises(ValueError):
        _: Flight = Flight(-1, 123, aircraft_test, route_test, passengers_test, 163, 383)

# Test scheduled_time type
def test_flight_scheduled_time_type_error(aircraft_test, route_test, passengers_test) -> None:
    with pytest.raises(TypeError):
        _: Flight = Flight(1, "this is not an int", aircraft_test, route_test, passengers_test, 163, 383)

# Test if negative scheduled_time
def test_flight_negative_scheduled_time(aircraft_test, route_test, passengers_test) -> None:
    _: Flight = Flight(1, 0, aircraft_test, route_test, passengers_test, 163, 383)
    
    with pytest.raises(ValueError):
        _: Flight = Flight(1, -1, aircraft_test, route_test, passengers_test, 163, 383)

# Test Aircraft type
def test_flight_aircraft_type_error(route_test, passengers_test) -> None:
    with pytest.raises(TypeError):
        _: Flight = Flight(1, 123, "this is not an Aircraft", route_test, passengers_test, 163, 383)

# Test Route type
def test_flight_route_type_error(aircraft_test, passengers_test) -> None:
    with pytest.raises(TypeError):
        _: Flight = Flight(1, 123, aircraft_test, "this is not a Route", passengers_test, 163, 383)

# Test type for all passengers (method 1)
def test_flight_passengers_type_error1(aircraft_test, route_test, passengers_test) -> None:
    passengers_test.append("not a passenger")
    with pytest.raises(TypeError):
        _: Flight = Flight(1, 123, aircraft_test, route_test, passengers_test, 163, 383)

# Test type for all passengers (method 2)
def test_flight_passengers_type_error2(aircraft_test, route_test, passengers_test) -> None:
    with pytest.raises(TypeError):
        _: Flight = Flight(1, 123, aircraft_test, route_test, "this is not a Passenger list", 163, 383)

# Test expected_departure_time type
def test_flight_expected_departure_time_type_error(aircraft_test, route_test, passengers_test) -> None:
    with pytest.raises(TypeError):
        _: Flight = Flight(1, 123, aircraft_test, route_test, passengers_test, "this is not an int", 383)

# Test if negative expected_departure_time
def test_flight_negative_expected_departure_time(aircraft_test, route_test, passengers_test) -> None:
    _: Flight = Flight(1, 123, aircraft_test, route_test, passengers_test, 0, 383)
    
    with pytest.raises(ValueError):
        _: Flight = Flight(1, 123, aircraft_test, route_test, passengers_test, -1, 383)

# Test expected_arrival_time type
def test_flight_expected_arrival_time_type_error(aircraft_test, route_test, passengers_test) -> None:
    with pytest.raises(TypeError):
        _: Flight = Flight(1, 123, aircraft_test, route_test, passengers_test, 163, "this is not an int")

# Test if negative expected_arrival_time
def test_flight_negative_expected_arrival_time(aircraft_test, route_test, passengers_test) -> None:
    _: Flight = Flight(1, 123, aircraft_test, route_test, passengers_test, 163, 0)
    
    with pytest.raises(ValueError):
        _: Flight = Flight(1, 123, aircraft_test, route_test, passengers_test, 163, -1)


# Test changing actual_departure_time and actual_arrival_time
def test_set_actual_departure_and_arrival_time(aircraft_test, route_test, passengers_test) -> None:
    flight_test = Flight(1, 123, aircraft_test, route_test, passengers_test, 163, 383)
    
    flight_test.set_actual_departure_time(12)
    flight_test.set_actual_arrival_time(120)
    
    assert flight_test.actual_departure_time == 12
    assert flight_test.actual_arrival_time == 120
    
# Test actual_departure_time type
def test_flight_actual_departure_time_type_error(aircraft_test, route_test, passengers_test) -> None:
    flight_test = Flight(1, 123, aircraft_test, route_test, passengers_test, 163, 383)
    with pytest.raises(TypeError):
        flight_test.set_actual_departure_time("this is not an int")
        
# Check for negative actual_departure_time
def test_flight_negative_actual_departure_time(aircraft_test, route_test, passengers_test) -> None:
    """Aircraft.__init__() method test. Tests that the aircraft class constructor protects against negative fuel levels"""
    flight_test = Flight(1, 123, aircraft_test, route_test, passengers_test, 163, 383)
    flight_test.set_actual_departure_time(0)
    
    with pytest.raises(ValueError):
        flight_test.set_actual_departure_time(-1)
    
# Test actual_arrival_time type
def test_flight_actual_arrival_time_type_error(aircraft_test, route_test, passengers_test) -> None:
    flight_test = Flight(1, 123, aircraft_test, route_test, passengers_test, 163, 383)
    with pytest.raises(TypeError):
        flight_test.set_actual_arrival_time("this is not an int")
        
# Check for negative actual_arrival_time
def test_flight_negative_actual_arrival_time(aircraft_test, route_test, passengers_test) -> None:
    """Aircraft.__init__() method test. Tests that the aircraft class constructor protects against negative fuel levels"""
    flight_test = Flight(1, 123, aircraft_test, route_test, passengers_test, 163, 383)
    flight_test.set_actual_arrival_time(0)
    
    with pytest.raises(ValueError):
        flight_test.set_actual_arrival_time(-1)
