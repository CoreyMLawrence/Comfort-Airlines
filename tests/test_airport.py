import pytest
from models.airport import Airport

def test_airport_init() -> None:
    _ = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, -71.0, [], [], None, "Metro", 0, 0, 0, 0)

@pytest.mark.parametrize("name", ["", None])
def test_airport_init_empty_or_null_name(name) -> None:
    with pytest.raises(ValueError):
        _ = Airport(name, "SAP", "Howdey", "Doodey", 25.0, -71.0, [], [], None, "Metro", 0, 0, 0, 0)


@pytest.mark.parametrize("iata_code", ["", None])
def test_airport_init_empty_or_null_iata_code(iata_code) -> None:
    with pytest.raises(ValueError):
        _ = Airport("Some Airport", iata_code, "Howdey", "Doodey", 25.0, -71.0, [], [], None, "Metro", 0, 0, 0, 0)

@pytest.mark.parametrize("city", ["", None])
def test_airport_init_empty_or_null_city(city) -> None:
    with pytest.raises(ValueError):
        _ = Airport("Some Airport", "SAP", city, "Doodey", 25.0, -71.0, [], [], None, "Metro", 0, 0, 0, 0)


@pytest.mark.parametrize("state", ["", None])
def test_airport_init_empty_or_null_state(state) -> None:
    with pytest.raises(ValueError):
        _ = Airport("Some Airport", "SAP", "Howdey", state, 25.0, -71.0, [], [], None, "Metro", 0, 0, 0, 0)

@pytest.mark.parametrize("latitude", [-90.0, 0.0, 90.0])
def test_airport_init_legal_latitude(latitude) -> None:
    _ = Airport("Some Airport", "SAP", "Howdey", "Doodey", latitude, -71.0, [], [], None, "Metro", 0, 0, 0, 0)

@pytest.mark.parametrize("latitude", [-90.1, 90.1])
def test_airport_init_illegal_latitude(latitude) -> None:
    with pytest.raises(ValueError):
         _ = Airport("Some Airport", "SAP", "Howdey", "Doodey", latitude, -71.0, [], [], None, "Metro", 0, 0, 0, 0)

@pytest.mark.parametrize("longitude", [-180.0, 0.0, 180.0])
def test_airport_init_legal_longitude(longitude) -> None:
    _ = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, longitude, [], [], None, "Metro", 0, 0, 0, 0)

@pytest.mark.parametrize("longitude", [-180.1, 180.1])
def test_airport_init_illegal_longitude(longitude) -> None:
    with pytest.raises(ValueError):
         _ = Airport("Some Airport", "SAP", "Howdey", "Doodey", 25.0, longitude, [], [], None, "Metro", 0, 0, 0, 0)

@pytest.mark.parametrize("gates",
    [

    ]
)
def test_airport_gates(gates: int) -> None:
    pass

