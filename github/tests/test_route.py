from decimal import Decimal

import pytest

from models.aircraft import Aircraft, AircraftType, AircraftStatus
from models.airport import Airport
from models.route import Route
    
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

def test_route_init(airport, hub) -> None:
    route = Route(AircraftType.AIRBUS_A200_100, airport, hub, 1.0, 1, 1.0, 315, Decimal("315"), Decimal("51390"))

def test_route_init_aircraft_illegal_type(airport, hub) -> None:
    with pytest.raises(TypeError):
        _ = Route("not an AircraftType object", airport, hub, 1.0, 1, 1.0, 315, Decimal("315"), Decimal("51390"))

def test_route_init_source_airport_illegal_type(hub) -> None:
    with pytest.raises(TypeError):
        _ = Route(AircraftType.AIRBUS_A200_100, "not an Airport object", hub, 1.0, 1, 1.0, 315, Decimal("315"), Decimal("51390"))

def test_route_init_destination_airport_illegal_type(airport) -> None:
    with pytest.raises(TypeError):
        _ = Route(AircraftType.AIRBUS_A200_100, airport, "not an Airport object", 1.0, 1, 1.0, 315, Decimal("315"), Decimal("51390"))

def test_route_init_same_airports(airport) -> None:
    with pytest.raises(ValueError):
        _ = Route(AircraftType.AIRBUS_A200_100, airport, airport, 1.0, 1, 1.0, 315, Decimal("315"), Decimal("51390"))

@pytest.mark.parametrize("distance", [0.01, 103.13, 351013.0])
def test_route_init_distance_legal_value(distance, airport, hub) -> None:
    _ = Route(AircraftType.AIRBUS_A200_100, airport, hub, distance, 1, 1.0, 315, Decimal("315"), Decimal("51390"))

@pytest.mark.parametrize("distance", ["not a float", 10])
def test_route_init_distance_illegal_type(distance, airport, hub) -> None:
    with pytest.raises(TypeError):
        _ = Route(AircraftType.AIRBUS_A200_100, airport, hub, distance, 1, 1.0, 315, Decimal("315"), Decimal("51390"))

@pytest.mark.parametrize("distance", [-0.01, -31.73414])
def test_route_init_distance_illegal_value(distance, airport, hub) -> None:
    with pytest.raises(ValueError):
        _ = Route(AircraftType.AIRBUS_A200_100, airport, hub, distance, 1, 1.0, 315, Decimal("315"), Decimal("51390"))

@pytest.mark.parametrize("demand", [1, 131, 51390513])
def test_route_init_demand_legal_value(demand, airport, hub) -> None:
    _ = Route(AircraftType.AIRBUS_A200_100, airport, hub, 1.0, demand, 1.0, 315, Decimal("315"), Decimal("51390"))

@pytest.mark.parametrize("demand", ["not an integer", 10.5])
def test_route_init_demand_illegal_type(demand, airport, hub) -> None:
    with pytest.raises(TypeError):
        _ = Route(AircraftType.AIRBUS_A200_100, airport, hub, 1.0, demand, 1.0, 315, Decimal("315"), Decimal("51390"))

@pytest.mark.parametrize("demand", [-1, -1531, 0])
def test_route_init_demand_illegal_value(demand, airport, hub) -> None:
    with pytest.raises(ValueError):
        _ = Route(AircraftType.AIRBUS_A200_100, airport, hub, 1.0, demand, 1.0, 315, Decimal("315"), Decimal("51390"))

@pytest.mark.parametrize("fuel_requirement", [1.0, 31.51, 3415319.013])
def test_route_init_fuel_requirement_legal_value(fuel_requirement, airport, hub) -> None:
    _ = Route(AircraftType.AIRBUS_A200_100, airport, hub, 1.0, 1, fuel_requirement, 315, Decimal("315"), Decimal("51390"))

@pytest.mark.parametrize("fuel_requirement", ["not a float", 10, 0])
def test_route_init_fuel_requirement_illegal_type(fuel_requirement, airport, hub) -> None:
    with pytest.raises(TypeError):
        _ = Route(AircraftType.AIRBUS_A200_100, airport, hub, 1.0, 1, fuel_requirement, 315, Decimal("315"), Decimal("51390"))

@pytest.mark.parametrize("fuel_requirement", [-0.01, -315.13, -31531.718])
def test_route_init_fuel_requirement_illegal_value(fuel_requirement, airport, hub) -> None:
    with pytest.raises(ValueError):
        _ = Route(AircraftType.AIRBUS_A200_100, airport, hub, 1.0, 1, fuel_requirement, 315, Decimal("315"), Decimal("51390"))