# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Corey Lawrence, Dylan Hudson
# Date: 3/9/2024
#
# Description:
#   This module tests the model class `Airport` as well as the factories and enumerated types for constructing them.

# Import necessary libraries and modules
import pytest
from decimal import Decimal
from queue import Queue
from models.airport import Airport, AirportType  # Assuming Airport class and AirportType enumeration are defined in models.airport

# Define the test function with parameterized inputs to test the constructor of Airport class
@pytest.mark.parametrize("name, iata_code, city, state, metro_population, is_hub, available_gates, latitude, longitude, gas_price, takeoff_fee, landing_fee, tarmac", 
    [
        # Test cases with different airport attributes
        ("John F. Kennedy International Airport", "JFK", "New York City", "New York", 18713220, False, 5, 40.6413, -73.7781, 2.50, Decimal('1000.00'), Decimal('500.00'), Queue()),
        ("Los Angeles International Airport", "LAX", "Los Angeles", "California", 13310447, False, 5, 33.9416, -118.4085, 2.75, Decimal('1200.00'), Decimal('600.00'), Queue()),
        ("Dallas/Fort Worth International Airport", "DFW", "Dallas/Fort Worth", "Texas", 7233323, True, 11, 32.8998, -97.0403, 2.65, Decimal('1100.00'), Decimal('550.00'), Queue()),
        ("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue()),
    ]
)
def test_airport_constructor(
        name, iata_code, city, state, metro_population, is_hub, available_gates, latitude, longitude, 
        gas_price, takeoff_fee, landing_fee, tarmac
    ):
    """Airport class constructor test. Asserts that the attributes are initialized correctly."""
    # Create an instance of Airport class with provided attributes
    airport = Airport(name, iata_code, city, state, metro_population, is_hub, available_gates, latitude, longitude, gas_price, takeoff_fee, landing_fee, tarmac)

    # Assert that the attributes are correctly initialized
    assert airport.name == name
    assert airport.iata_code == iata_code
    assert airport.city == city
    assert airport.state == state
    assert airport.metro_population == metro_population
    assert airport.is_hub == is_hub
    assert airport.available_gates == available_gates
    assert airport.latitude == latitude
    assert airport.longitude == longitude
    assert airport.gas_price == gas_price
    assert airport.takeoff_fee == takeoff_fee
    assert airport.landing_fee == landing_fee
    assert airport.tarmac == tarmac
