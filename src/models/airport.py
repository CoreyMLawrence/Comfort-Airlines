from __future__ import annotations
from typing import Union, TYPE_CHECKING
from decimal import Decimal
from queue import Queue

if TYPE_CHECKING:
    from models.passenger import Passenger
    from models.route import Route

class Airport:
    def __init__(self, name: str, iata_code: str, city: str, state: str, latitude: float, longitude: float, routes: list[Route], passengers: list[Passenger], regional_airport: Union[Airport, None], metro_area: str, metro_population: int, gas_price: Decimal, takeoff_fee: Decimal, landing_fee: Decimal):
        self.name = name
        self.iata_code = iata_code
        self.city = city
        self.state = state
        self.latitude = latitude
        self.longitude = longitude
        self.routes = routes
        self.passengers = passengers
        self.regional_airport = regional_airport
        self.metro_area = metro_area
        self.metro_population = metro_population
        self.gates = 11 if regional_airport is None else (min(metro_population // 1_000_000, 5))
        self.gas_price = gas_price
        self.takeoff_fee = takeoff_fee
        self.landing_fee = landing_fee
        self.tarmac = Queue()
        
    @property
    def is_hub(self) -> bool:
        return self.regional_airport is None