# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Corey Lawrence, Dylan Hudson
# Date: 3/9/2024
#
# Description:
#   This module defines and implements the model class `Airport` as well as the factories and enumerated types for constructing them.


from enum import Enum
from queue import Queue

class AirportType(Enum):
    """Enumerated type. Defines the 2 types of airports."""
    LOCAL = 0
    HUB = 1

class Airport:
    """Model class. A generic representation of an airport."""
    def __init__(
            self, name: str, iata_code: str, city: str, state: str, metro_population: int,
            is_hub: bool, available_gates: int, latitude: float, longitude: float,
            gas_price: float, takeoff_fee: float, landing_fee: float, tarmac: Queue,
            constructor: str
        ):
        self.name = name
        self.iata_code = iata_code
        self.city = city
        self.state = state
        self.metro_population = metro_population
        self.is_hub = is_hub
        self.available_gates = available_gates
        self.latitude = latitude
        self.longitude = longitude
        self.gas_price = gas_price
        self.takeoff_fee = takeoff_fee
        self.landing_fee = landing_fee
        self.tarmac = tarmac
        self.constructor = constructor

class AirportFactory:
    """Factory class to create Airport objects."""
    @staticmethod
    def create_airport(
            name: str, iata_code: str, city: str, state: str, metro_population: int,
            is_hub: bool, available_gates: int, latitude: float, longitude: float,
            gas_price: float, takeoff_fee: float, landing_fee: float, constructor: str
        ) -> Airport:
        """Factory method to create Airport objects."""
        return Airport(
            name, iata_code, city, state, metro_population, is_hub, available_gates,
            latitude, longitude, gas_price, takeoff_fee, landing_fee, Queue(), constructor
        )
