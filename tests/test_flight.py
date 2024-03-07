from decimal import Decimal

import pytest

from models.flight import Flight
from models.aircraft import Aircraft, AircraftFactory, AircraftType, AircraftStatus
from models.airport import Airport
from models.route import Route
from models.passenger import Passenger

def test_flight_init() -> None:
    airport = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, -71.0, [], [], None, "Metro", 0, Decimal("0.0"), Decimal("0.0"), Decimal("0.0"))
    
    aircraft = Aircraft(
        "Boeing 737-600", AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None,
        0, 119, 1101, 0, 6875, 
        0.55, 5648
    )
    
    route = Route(
        AircraftFactory.create_aircraft(AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None, 0),
        airport,
        airport,
        0.0,
        0,
        0.0
    )
    
    passengers = [
        Passenger(
            airport,
            airport
        ),
        Passenger(
            airport,
            airport
        ),
    ]
    
    flight = Flight(0, aircraft, route, passengers)
    
    assert flight.flight_number == 0
    assert flight.aircraft == aircraft
    assert flight.route == route
    assert flight.passengers == passengers