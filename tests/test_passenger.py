from decimal import Decimal

import pytest

from models.passenger import Passenger
from models.airport import Airport

@pytest.fixture()
def hub() -> Airport:
    return Airport(
        "Some hub", "SH", "Howdey", "Doodey", 25.0, -71.0, 
        [], None, "Metro", 0, Decimal("0.0"), Decimal("0.0"),
        Decimal("0.0")
    )
    
@pytest.fixture
def airport(hub) -> Airport:
    return Airport(
        "Some Airport", "SAP", "Howdey", "Doodey", 25.0, -71.0, 
        [], hub, "Metro", 0, Decimal("0.0"), Decimal("0.0"),
        Decimal("0.0")
    )

def test_passenger_init(airport, hub) -> None:
    """Test Passenger.__init__(). MUST be first or else passenger.uuid will not be 0"""
    passenger = Passenger(airport, hub)
    
    assert passenger.location == airport
    assert passenger.destination == hub

def test_passenger_init_location_legal_type_airport(airport, hub) -> None:
    passenger = Passenger(airport, hub)
    
def test_passenger_init_location_illegal_type(hub) -> None:
    with pytest.raises(TypeError):
        _ = Passenger("not an Airport object", hub)
        
def test_passenger_uuid_generation(airport, hub) -> None:
    a = Passenger(airport, hub)
    b = Passenger(airport, hub)
    c = Passenger(airport, hub)
    
    assert b.uuid == a.uuid + 1
    assert c.uuid == b.uuid + 1