from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.airport import Airport
    from models.aircraft import Aircraft

class Route:
    def __init__(self, aircraft: Aircraft, source_airport: Airport, destination_airport: Airport, distance: float, demand: int, fuel_requirement: float):
        self.aircraft = aircraft
        self.source_airport = source_airport
        self.destination_airport = destination_airport
        self.distance = distance
        self.demand = demand
        self.fuel_requirement = fuel_requirement
        
    def __repr__(self) -> str:
        return f"{{ {self.aircraft=}, {self.source_airport=}, {self.destination_airport=}, {self.distance=}, {self.demand=}, {self.fuel_requirement=}}}"