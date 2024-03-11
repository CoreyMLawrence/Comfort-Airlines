from decimal import Decimal

import pytest

from models.aircraft import Aircraft, AircraftType, AircraftStatus
from models.airport import Airport
from models.route import Route

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

def test_route_init(aircraft, airport, hub) -> None:
    route = Route(aircraft, airport, hub, 1.0, 1, 1.0)

def test_route_init_aircraft_illegal_type(airport, hub) -> None:
    with pytest.raises(TypeError):
        _ = Route("not an Aircraft object", airport, hub, 1.0, 1, 1.0)

def test_route_init_source_airport_illegal_type(aircraft, hub) -> None:
    with pytest.raises(TypeError):
        _ = Route(aircraft, "not an Airport object", hub, 1.0, 1, 1.0)

def test_route_init_destination_airport_illegal_type(aircraft, airport) -> None:
    with pytest.raises(TypeError):
        _ = Route(aircraft, airport, "not an Airport object", 1.0, 1, 1.0)

def test_route_init_same_airports(aircraft, airport) -> None:
    with pytest.raises(ValueError):
        _ = Route(aircraft, airport, airport, 1.0, 1, 1.0)

@pytest.mark.parametrize("distance", [0.01, 103.13, 351013.0])
def test_route_init_distance_legal_value(distance, aircraft, airport, hub) -> None:
    _ = Route(aircraft, airport, hub, distance, 1, 1.0)

@pytest.mark.parametrize("distance", ["not a float", 10, -0.01, -31.73414])
def test_route_init_distance_illegal_value(distance, aircraft, airport, hub) -> None:
    with pytest.raises(ValueError):
        _ = Route(aircraft, airport, hub, distance, 1, 1.0)

@pytest.mark.parametrize("demand", [1, 131, 51390513])
def test_route_init_demand_legal_value(demand, aircraft, airport, hub) -> None:
    _ = Route(aircraft, airport, hub, 1.0, demand, 1.0)

@pytest.mark.parametrize("demand", ["not an integer", 10.5, -1, -1531, 0])
def test_route_init_demand_illegal_value(demand, aircraft, airport, hub) -> None:
    with pytest.raises(ValueError):
        _ = Route(aircraft, airport, hub, 1.0, demand, 1.0)

@pytest.mark.parametrize("fuel_requirement", [1.0, 31.51, 3415319.013])
def test_route_init_fuel_requirement_legal_value(fuel_requirement, aircraft, airport, hub) -> None:
    _ = Route(aircraft, airport, hub, 1.0, 1, fuel_requirement)

@pytest.mark.parametrize("fuel_requirement", ["not a float", 10, 0, 0.0, -0.01, -315.13, -31531.718])
def test_route_init_fuel_requirement_illegal_value(fuel_requirement, aircraft, airport, hub) -> None:
    with pytest.raises(ValueError):
        _ = Route(aircraft, airport, hub, 1.0, 1, fuel_requirement)