from __future__ import annotations
from typing import TYPE_CHECKING
from time import struct_time

if TYPE_CHECKING:
    from models.aircraft import Aircraft
    from models.route import Route
    from models.passenger import Passenger

class Flight:
    def __init__(self, flight_number: int, aircraft: Aircraft, route: Route, passengers: list[Passenger]):
        self.flight_number = flight_number
        self.aircraft = aircraft
        self.route = route
        self.passengers = passengers
        
        # TODO: calculate expected departure and arrival time in Flight constructor
        self.expected_departure_time = None
        self.expected_arrival_time = None
        self.actual_departure_time = None
        self.actual_arrival_time = None