# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Parker Blue, Anthony Cox
# Date: 3/21/2024
#
# Description:
#   This module tests the model class `Passenger`.

# Import necessary libraries and modules
from decimal import Decimal
from queue import Queue

import pytest

from models.passenger import Passenger
from models.airport import Airport
#setup test airports
@pytest.fixture()
def hub() -> Airport:
    return Airport(
        "Dallas/Fort Worth International Airport", "DFW", "Dallas/Fort Worth", "Texas", 7233323, True, 11, 32.8998, 
        -97.0403, 2.65, Decimal('1100.00'), Decimal('550.00'), Queue()
    )
#add hub to some test airport
@pytest.fixture
def airport(hub) -> Airport:
    return Airport(
        "John F. Kennedy International Airport", "JFK", "New York City", "New York", 18713220, 
        False, 5, 40.6413, -73.7781, 2.50, Decimal('1000.00'), Decimal('500.00'), Queue()
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
#tests auto increment     
def test_passenger_uuid_generation(airport, hub) -> None:
    a = Passenger(airport, hub)
    b = Passenger(airport, hub)
    c = Passenger(airport, hub)
    
    assert b.uuid == a.uuid + 1
    assert c.uuid == b.uuid + 1