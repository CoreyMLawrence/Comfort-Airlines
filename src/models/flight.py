from __future__ import annotations
from typing import TYPE_CHECKING


from models.aircraft import Aircraft
from models.route import Route
from models.passenger import Passenger

class Flight:
    def __init__(self, flight_number: int, time: int, aircraft: Aircraft, route: Route, passengers: list[Passenger], expected_departure_time: int, expected_arrival_time: int):
        if not type(flight_number) is int or flight_number < 0:
            raise ValueError("Flight parameter 'flight_number' must be an integer greater than or equal to 0")
        
        if not type(time) is int or time < 0:
            raise ValueError("Flight parameter 'time' must be an integer greater than or equal to 0")
        
        if not type(aircraft) is Aircraft:
            raise TypeError("Flight parameter 'aircraft' must be an Aircraft object")
        
        if not type(route) is Route:
            raise TypeError("Flight parameter 'route' must be a Route object")
        
        if any(not type(passenger) is Passenger for passenger in passengers):
            raise TypeError("Flight parameter 'passengers' must be a list of Passenger objects")
        
        if not type(expected_departure_time) is int:
            raise TypeError("Flight parameter 'expected_departure_time' must be an int")
        
        if not type(expected_arrival_time) is int:
            raise TypeError("Flight parameter 'expected_arrival_time' must be an int")
        
        if expected_arrival_time < expected_departure_time:
            raise ValueError("Flight parameter 'expected_arrival_time' must be greater than or equal to parameter 'expected_departure_time'")
        
        self.flight_number = flight_number
        self.time = time
        self.aircraft = aircraft
        self.route = route
        self.passengers = passengers
        
        self.expected_departure_time = expected_departure_time
        self.expected_arrival_time = expected_arrival_time
        self.actual_departure_time = None
        self.actual_arrival_time = None