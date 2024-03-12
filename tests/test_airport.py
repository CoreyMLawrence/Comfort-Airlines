<<<<<<< HEAD
from decimal import Decimal

import pytest

from models.airport import Airport

def test_airport_init() -> None:
    _ = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, -71.0, [], None, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))

@pytest.mark.parametrize("name", ["", None])
def test_airport_init_empty_or_null_name(name) -> None:
    with pytest.raises(ValueError):
        _ = Airport(name, "SAP", "Howdey", "Doodey", 25.0, -71.0, [], None, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))

@pytest.mark.parametrize("iata_code", ["", None])
def test_airport_init_empty_or_null_iata_code(iata_code) -> None:
    with pytest.raises(ValueError):
        _ = Airport("Some Airport", iata_code, "Howdey", "Doodey", 25.0, -71.0, [], None, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))

@pytest.mark.parametrize("city", ["", None])
def test_airport_init_empty_or_null_city(city) -> None:
    with pytest.raises(ValueError):
        _ = Airport("Some Airport", "SAP", city, "Doodey", 25.0, -71.0, [],  None, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))


@pytest.mark.parametrize("state", ["", None])
def test_airport_init_empty_or_null_state(state) -> None:
    with pytest.raises(ValueError):
        _ = Airport("Some Airport", "SAP", "Howdey", state, 25.0, -71.0, [], None, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))

@pytest.mark.parametrize("latitude", [-90.0, 0.0, 90.0])
def test_airport_init_legal_latitude(latitude) -> None:
    _ = Airport("Some Airport", "SAP", "Howdey", "Doodey", latitude, -71.0, [], None, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))

@pytest.mark.parametrize("latitude", [-90.1, 90.1])
def test_airport_init_illegal_latitude(latitude) -> None:
    with pytest.raises(ValueError):
         _ = Airport("Some Airport", "SAP", "Howdey", "Doodey", latitude, -71.0, [], None, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))

@pytest.mark.parametrize("longitude", [-180.0, 0.0, 180.0])
def test_airport_init_legal_longitude(longitude) -> None:
    _ = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, longitude, [], None, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))

@pytest.mark.parametrize("longitude", [-180.1, 180.1])
def test_airport_init_illegal_longitude(longitude) -> None:
    with pytest.raises(ValueError):
         _ = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, longitude, [], None, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))


@pytest.mark.parametrize("metro_population, expected_gates",
    [
        (0, 0),
        (999_999, 0),
        (1_000_000, 1),
        (1_999_999, 1),
        (2_000_000, 2),
    ]
)
def test_airport_init_airport_gates(metro_population: int, expected_gates: int) -> None:
    hub = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, -71.0, [], None, "Metro", metro_population, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))
    airport = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, -71.0, [], hub, "Metro", metro_population, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))
    assert airport.gates == expected_gates
    
@pytest.mark.parametrize("metro_population, expected_gates",
    [
        (0, 11),
        (999_999, 11),
        (1_000_000, 11),
        (1_999_999, 11),
        (2_000_000, 11),
    ]
)
def test_airport_init_hub_gates(metro_population: int, expected_gates: int) -> None:
    airport = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, -71.0, [], None, "Metro", metro_population, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))
    assert airport.gates == expected_gates
    
def test_airport_init_airport_maintenance_gates() -> None:
    hub = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, -71.0, [], None, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))
    airport = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, -71.0, [], hub, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))
    assert airport.maintenance_gates == 0
    
def test_airport_init_hub_maintenance_gates() -> None:
    hub = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, -71.0, [], None, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))
    assert hub.maintenance_gates == 3
    
def test_airport_property_is_hub() -> None:
    hub = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, -71.0, [], None, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))
    airport = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, -71.0, [], hub, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))
    
    assert hub.is_hub
    assert not airport.is_hub
=======
import pytest
from decimal import Decimal
from queue import Queue
from src.airport import Airport, AirportType

@pytest.mark.parametrize("name, iata_code, city, state, metro_population, is_hub, available_gates, latitude, longitude, gas_price, takeoff_fee, landing_fee, tarmac", 
    [
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
    airport = Airport(name, iata_code, city, state, metro_population, is_hub, available_gates, latitude, longitude, gas_price, takeoff_fee, landing_fee, tarmac)

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
>>>>>>> 11e1fa100fad9509ad536753e3bd6d7434795362
