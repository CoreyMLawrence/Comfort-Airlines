from __future__ import annotations
from typing import TYPE_CHECKING

from models.airport import Airport
from models.aircraft import Aircraft

class Route:
    def __init__(self, aircraft: Aircraft, source_airport: Airport, destination_airport: Airport, distance: float, demand: int, fuel_requirement: float):
        if not type(aircraft) is Aircraft:
            raise TypeError("Parameter 'aircraft' must be an Aircraft object")
        
        if not type(source_airport) is Airport:
            raise TypeError("Parameter 'source_airport' must be an Airport object")
        
        if not type(destination_airport) is Airport:
            raise TypeError("Parameter 'source_airport' must be an Airport object")

        if source_airport == destination_airport:
            raise ValueError("Parameters 'source_airport' and 'destination_airport' cannot be the same Airport object (do you have a logic error?)")
        
        if not type(distance) is float or distance <= 0.0:
            raise ValueError("Parameter 'distance' must be a float in the range (0.0,inf]")

        if not type(demand) is int or demand <= 0:
            raise ValueError("Parameter 'demand' must be an integer in the range (0,inf]")

        if not type(fuel_requirement) is float or fuel_requirement <= 0:
            raise ValueError("Paramter 'fuel_requirement' must be a float in the range (0.0,inf]")

        self.aircraft = aircraft
        self.source_airport = source_airport
        self.destination_airport = destination_airport
        self.distance = distance
        self.demand = demand
        self.fuel_requirement = fuel_requirement
        
    def __repr__(self) -> str:
        return f"{{ {self.aircraft=}, {self.source_airport=}, {self.destination_airport=}, {self.distance=}, {self.demand=}, {self.fuel_requirement=}}}"