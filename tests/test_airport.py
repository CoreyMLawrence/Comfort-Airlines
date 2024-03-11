import pytest
from ..src.airport import Airport, AirportFactory, AirportType

@pytest.mark.parametrize("name, iata_code, city, state, metro_population, is_hub, available_gates, latitude, longitude, gas_price, takeoff_fee, landing_fee, constructor", 
    [
        ("Hartsfield-Jackson Atlanta International Airport", "ATL", "Atlanta", "Georgia", 5210000, True, 207, 33.6407, -84.4277, 2.75, 5000.00, 5000.00, "Foobar"),
        ("O'Hare International Airport", "ORD", "Chicago", "Illinois", 2695000, True, 185, 41.9742, -87.9073, 2.95, 5500.00, 5500.00, "Foobar"),
    ]
)
def test_airport_factory_create_airport(name, iata_code, city, state, metro_population, is_hub, available_gates, latitude, longitude, gas_price, takeoff_fee, landing_fee, constructor) -> None:
    """AirportFactory.create_airport() method test. Asserts that passing in the airport type correctly yields an airport with the correct information"""
    airport = AirportFactory.create_airport(name, iata_code, city, state, metro_population, is_hub, available_gates, latitude, longitude, gas_price, takeoff_fee, landing_fee, constructor)

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
    assert airport.constructor == constructor

def test_airport_factory_create_airport_type_error() -> None:
    """AirportFactory.create_airport() method test. Asserts that the airport factory handles type errors"""
    with pytest.raises(TypeError):
        AirportFactory.create_airport("Some Airport", "SPT", "Some City", "Some State", 1000000, True, 50, 42.0, -80.0, 3.0, 2000.0, 1500.0, 123)
