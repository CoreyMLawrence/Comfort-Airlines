from __future__ import annotations
from typing import TYPE_CHECKING
from time import struct_time


from models.aircraft import Aircraft
from models.route import Route
from models.passenger import Passenger

class Flight:
    def __init__(self, flight_number: int, aircraft: Aircraft, route: Route, passengers: list[Passenger]):
        if not type(flight_number) is int or flight_number < 0:
            raise ValueError("Flight parameter 'flight_number' must be an integer greater than or equal to 0")
        
        if not type(aircraft) is Aircraft:
            raise TypeError("Flight parameter 'aircraft' must be an Aircraft object")
        
        if not type(route) is Route:
            raise TypeError("Flight parameter 'route' must be a Route object")
        
        if any(not type(passenger) is Passenger for passenger in passengers):
            raise TypeError("Flight parameter 'passengers' must be a list of Passenger objects")
        
        self.flight_number = flight_number
        self.aircraft = aircraft
        self.route = route
        self.passengers = passengers
        
        # TODO: calculate expected departure and arrival time in Flight constructor
        self.expected_departure_time = None
        self.expected_arrival_time = None
        self.actual_departure_time = None
        self.actual_arrival_time = None