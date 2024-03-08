from decimal import Decimal

import pytest

from models.flight import Flight
from models.aircraft import Aircraft, AircraftFactory, AircraftType, AircraftStatus
from models.airport import Airport
from models.route import Route
from models.passenger import Passenger

@pytest.fixture
def aircraft() -> Aircraft:
    return Aircraft(
        "Boeing 737-600", AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None,
        0, 119, 1101, 0, 6875, 
        0.55, 5648
    )
    
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
    
@pytest.fixture
def route(aircraft, airport, hub) -> Route:
    return Route(aircraft, airport, hub, 0.0, 0, 0.0)

@pytest.fixture
def passengers(airport, hub) -> list[Passenger]:
    return [
        Passenger(
            airport,
            hub
        ),
        Passenger(
            airport,
            hub
        ),
        Passenger(
            airport,
            hub
        )
    ]

def test_flight_init(aircraft, route, passengers) -> None:
    flight = Flight(0, 10, aircraft, route, passengers)
    
    assert flight.flight_number == 0
    assert flight.time == 10
    assert flight.aircraft == aircraft
    assert flight.route == route
    assert flight.passengers == passengers

@pytest.mark.parametrize("flight_number", [0, 1, 621913])
def test_flight_init_flight_number_legal_value(flight_number, aircraft, route, passengers) -> None:
    _ = Flight(flight_number, 0, aircraft, route, passengers)

@pytest.mark.parametrize("flight_number", [-613, -1])
def test_flight_init_flight_number_illegal_value(flight_number, aircraft, route, passengers) -> None:
    with pytest.raises(ValueError):
        _ = Flight(flight_number, 0, aircraft, route, passengers)
        
@pytest.mark.parametrize("time", [0, 1, 11235])
def test_flight_init_time_legal_value(time, aircraft, route, passengers) -> None:
    _ = Flight(0, time, aircraft, route, passengers)

@pytest.mark.parametrize("time", [-1398, -2, -1])
def test_flight_init_time_illegal_value(time, aircraft, route, passengers) -> None:
    with pytest.raises(ValueError):
        _ = Flight(0, time, aircraft, route, passengers)
        
def test_flight_init_flight_number_illegal_type(aircraft, route, passengers) -> None:
    with pytest.raises(ValueError):
        _ = Flight("not an integer", 0, aircraft, route, passengers)
        
def test_flight_init_aircraft_illegal_type(route, passengers) -> None:
    with pytest.raises(TypeError):
        _ = Flight(0, 0, "not an Aircraft object", route, passengers)
        
def test_flight_init_aircraft_illegal_type(aircraft, passengers) -> None:
    with pytest.raises(TypeError):
        _ = Flight(0, 0, aircraft, "not a Route object", passengers)

@pytest.mark.parametrize("passengers",
    [
        ["not a Passenger object"],
        [-1]
    ]
)
def test_flight_init_passengers_illegal_type(aircraft, route, passengers) -> None:
    with pytest.raises(TypeError):
        _ = Flight(0, 0, aircraft, route, passengers)