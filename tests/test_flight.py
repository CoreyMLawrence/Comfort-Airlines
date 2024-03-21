import pytest
from decimal import Decimal
from queue import Queue
from models.airport import Airport, Aircraft, AircraftType, AircraftStatus, AircraftFactory
from models.flight import Flight


@pytest.mark.parametrize("name, iata_code, city, state, metro_population, is_hub, available_gates, latitude, longitude, gas_price, takeoff_fee, landing_fee, tarmac", 
    [
        ("John F. Kennedy International Airport", "JFK", "New York City", "New York", 18713220, False, 5, 40.6413, -73.7781, 2.50, Decimal('1000.00'), Decimal('500.00'), Queue()),
        ("Los Angeles International Airport", "LAX", "Los Angeles", "California", 13310447, False, 5, 33.9416, -118.4085, 2.75, Decimal('1200.00'), Decimal('600.00'), Queue()),
        ("Dallas/Fort Worth International Airport", "DFW", "Dallas/Fort Worth", "Texas", 7233323, True, 11, 32.8998, -97.0403, 2.65, Decimal('1100.00'), Decimal('550.00'), Queue()),
        ("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue()),
    ]
)
def test_flight_constructor(
        flight_number, scheduled_time, aircraft, route, passengers
    ):
    """Flight class constructor test. Asserts that the attributes are initialized correctly."""
    flight = Flight(flight_number, scheduled_time, aircraft, route, passengers)

    assert flight.flight_number == flight_number
    assert flight.scheduled_time == scheduled_time
    assert flight.aircraft == aircraft
    assert flight.route == route
    assert flight.passengers == passengers
    
    
