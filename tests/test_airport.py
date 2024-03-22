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
    

####################################### For Temporary Reference ####################################################
# Test flight_number type
def test_airport_name_type_error() -> None:
    with pytest.raises(TypeError):
        _: Airport = Airport(name, iata_code, city, state, metro_population, is_hub, available_gates, latitude, longitude, gas_price, takeoff_fee, landing_fee, tarmac)
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

# Test for negative flight_number
def test_airport_negative_metro_population() -> None:
    _: Airport = Airport(name, iata_code, city, state, metro_population, is_hub, available_gates, latitude, longitude, gas_price, takeoff_fee, landing_fee, tarmac)
    _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

    with pytest.raises(ValueError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())
####################################### For Temporary Reference ####################################################

        
# Test name type
def test_airport_name_type_error() -> None:
    with pytest.raises(TypeError):
        _: Airport = Airport(11111, "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

# Test iata_code type
def test_airport_iata_code_type_error() -> None:
    with pytest.raises(TypeError):
        _: Airport = Airport("Denver International Airport", 11111, "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

# Test city type
def test_airport_city_type_error() -> None:
    with pytest.raises(TypeError):
        _: Airport = Airport("Denver International Airport", "DEN", 11111, "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

# Test state type
def test_airport_state_type_error() -> None:
    with pytest.raises(TypeError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", 11111, 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

# Test metro_population type
def test_airport_metro_population_type_error() -> None:
    with pytest.raises(TypeError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", "this is not an int", True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

# Test if negative metro_population
def test_airport_negative_metro_population() -> None:
    _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 0, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

    with pytest.raises(ValueError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", -1, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

# Test is_hub type
def test_airport_is_hub_type_error() -> None:
    with pytest.raises(TypeError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, "this is not a bool", 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

# Test available_gates type
def test_airport_available_gates_type_error() -> None:
    with pytest.raises(TypeError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, "this is not an int", 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

# Test if negative available_gates
def test_airport_negative_available_gates() -> None:
    _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 0, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

    with pytest.raises(ValueError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, -1, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

# Test latitude type
def test_airport_latitude_type_error() -> None:
    with pytest.raises(TypeError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, "this is not a float", -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

# Test if latitude is in proper range (-90 to 90)
def test_airport_latitude_range() -> None:
    _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, -90.0, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())
    _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 90.0, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

    with pytest.raises(ValueError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, -90.1, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())
    with pytest.raises(ValueError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 90.1, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

# Test longitude type
def test_airport_longitude_type_error() -> None:
    with pytest.raises(TypeError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, "this is not a float", 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

# Test if longitude is in proper range (-180 to 180)
def test_airport_longitude_range() -> None:
    _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -180.0, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())
    _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, 180.0, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

    with pytest.raises(ValueError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -180.1, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())
    with pytest.raises(ValueError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, 180.1, 2.45, Decimal('900.00'), Decimal('450.00'), Queue())

# Test gas_price type
def test_airport_gas_price_type_error() -> None:
    with pytest.raises(TypeError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, "this is not a float", Decimal('900.00'), Decimal('450.00'), Queue())

# Test if negative gas_price
def test_airport_negative_gas_price() -> None:
    _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 0.0, Decimal('900.00'), Decimal('450.00'), Queue())

    with pytest.raises(ValueError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, -0.01, Decimal('900.00'), Decimal('450.00'), Queue())

# Test takeoff_fee type
def test_airport_takeoff_fee_type_error() -> None:
    with pytest.raises(TypeError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, 900.00, Decimal('450.00'), Queue())

# Test if negative takeoff_fee
def test_airport_negative_takeoff_fee() -> None:
    _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('0.00'), Decimal('450.00'), Queue())

    with pytest.raises(ValueError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('-900.00'), Decimal('450.00'), Queue())

# Test landing_fee type
def test_airport_landing_fee_type_error() -> None:
    with pytest.raises(TypeError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), 450.00, Queue())

# Test if negative landing_fee
def test_airport_negative_landing_fee() -> None:
    _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('0.00'), Queue())

    with pytest.raises(ValueError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('-450.00'), Queue())

# Test tarmac type
def test_airport_tarmac_type_error() -> None:
    with pytest.raises(TypeError):
        _: Airport = Airport("Denver International Airport", "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), "this is not a Queue")


##############################################################################################################################################################################
# Tried testing this way, but it is not easy to tell what the error is.
# @pytest.mark.parametrize("name, iata_code, city, state, metro_population, is_hub, available_gates, latitude, longitude, gas_price, takeoff_fee, landing_fee, tarmac", 
#     [
#         # Test name type
#         (11111, "DEN", "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue()),
#         # Test iata_code type
#         ("Denver International Airport", 11111, "Denver", "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue()),
#         # Test city type
#         ("Denver International Airport", "DEN", 11111, "Colorado", 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue()),
#         # Test state type
#         ("Denver International Airport", "DEN", "Denver", 11111, 2949387, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue()),
#         # Test metro_population type
#         ("Denver International Airport", "DEN", "Denver", "Colorado", "this is not an int", True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue()),
#         ### No TypeError throw -> Harder to figure out what the problem is.
#         ("Denver International Airport", "DEN", "Denver", "Colorado", 1, True, 11, 39.8561, -104.6737, 2.45, Decimal('900.00'), Decimal('450.00'), Queue()),
#     ]
# )
# def test_airport_name_type_error(name, iata_code, city, state, metro_population, is_hub, available_gates, latitude, longitude, gas_price, takeoff_fee, landing_fee, tarmac) -> None:
#     with pytest.raises(TypeError):
#         _: Airport = Airport(name, iata_code, city, state, metro_population, is_hub, available_gates, latitude, longitude, gas_price, takeoff_fee, landing_fee, tarmac)