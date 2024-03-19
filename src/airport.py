# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Corey Lawrence, Dylan Hudson
# Date: 3/9/2024
#
# Description:
#   This module defines and implements the model class `Airport` as well as the factories and enumerated types for constructing them.
from __future__ import annotations
from typing import TYPE_CHECKING
from enum import Enum
from models.aircraft import Aircraft, AircraftStatus

if TYPE_CHECKING:
    from decimal import Decimal
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
            gas_price: float, takeoff_fee: Decimal, landing_fee: Decimal, tarmac: Queue
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

    def assign_gate(self, aircraft: Aircraft) -> None:
        if self.gates > 0:
            self.gates -= 1
            aircraft.set_status(AircraftStatus.AVAILABLE)
        else:
            self.tarmac.put(aircraft)
            aircraft.set_status(AircraftStatus.ON_TARMAC)