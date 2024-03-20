from __future__ import annotations
from typing import TYPE_CHECKING
from decimal import Decimal

from models.airport import Airport
from models.aircraft import AircraftType

class Route:
    def __init__(self, aircraft_type: AircraftType, source_airport: Airport, destination_airport: Airport, distance: float, demand: int, fuel_requirement: float, expected_time: int, ticket_cost: Decimal, net_profit: Decimal):
        if not type(aircraft_type) is AircraftType:
            raise TypeError("Parameter 'aircraft' must be an AircraftType object")
        
        if not type(source_airport) is Airport:
            raise TypeError("Parameter 'source_airport' must be an Airport object")
        
        if not type(destination_airport) is Airport:
            raise TypeError("Parameter 'source_airport' must be an Airport object")

        if source_airport == destination_airport:
            raise ValueError("Parameters 'source_airport' and 'destination_airport' cannot be the same Airport object (do you have a logic error?)")
        
        if not type(distance) is float:
            raise TypeError("Parameter 'distance' must be a float")
        
        if distance <= 0.0:
            raise ValueError("Parameter 'distance' must be in the range (0.0,inf]")

        if not type(demand) is int:
            raise TypeError("Parameter 'demand' must be an integer")
        
        if demand <= 0:
            raise ValueError("Parameter 'demand' must be in the range (0,inf]")

        if not type(fuel_requirement) is float:
            raise TypeError("Parameter 'fuel_requirement' must be a float")
        
        if fuel_requirement <= 0.0:
            raise ValueError("Parameter 'fuel_requirement' must be in the range (0.0,inf]")

        self.aircraft_type = aircraft_type
        self.source_airport = source_airport
        self.destination_airport = destination_airport
        self.distance = distance
        self.demand = demand
        self.fuel_requirement = fuel_requirement
        self.expected_time = expected_time
        self.ticket_cost = ticket_cost
        self.net_profit = net_profit
        
    def __repr__(self) -> str:
        return f"{self.source_airport} => {self.destination_airport}"