# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Dylan Hudson
# Date: 3/18/2024
#
# Description:
#   This module defines and implements the model class `Flight` as well as the  and enumerated types for constructing them.

from models.aircraft import Aircraft
from models.route import Route
from models.passenger import Passenger

class Flight:
    """Model class. A generic representation of a flight."""
    def __init__(
            self, flight_number: int, scheduled_time: int, aircraft: Aircraft, route: Route, passenger: Passenger
            #, passengers: list[Passenger]
        ):
        self.flight_number = flight_number
        self.scheduled_time = scheduled_time
        self.aircraft = aircraft
        self.route = route
        self.passenger = passenger
        # self.passengers: passengers
        # pass
    
class FlightFactory:
    @staticmethod
    def create_flight(
            flight_number: int, scheduled_time: int, aircraft: Aircraft, 
            route: Route, passenger: Passenger
        ) -> Flight:
        """Factory class to create Flight objects. Uses ???????? as the API."""
        if not type(flight_number) is int:
            raise TypeError(f"parameter 'flight_number' is not of type 'int'. Got type: {type(flight_number).__name__}")

        if flight_number < 0:
            raise ValueError("flight_number cannot be negative")
        
        # Does there have to be a unique flight number check right here?
        
        if not type(scheduled_time) is int:
            raise TypeError(f"parameter 'scheduled_time' is not of type 'int'. Got type: {type(scheduled_time).__name__}")
        
        if scheduled_time < 0:
            raise ValueError("scheduled_time cannot be negative")
        
        if not type(aircraft) is Aircraft:
            raise TypeError(f"parameter 'aircraft' is not of type 'Aircraft'. Got type: {type(aircraft).__name__}")
        
        if not type(route) is Route:
            raise TypeError(f"parameter 'route' is not of type 'Route'. Got type: {type(route).__name__}")
        
        if not type(passenger) is Passenger:
            raise TypeError(f"parameter 'passenger' is not of type 'Passenger'. Got type: {type(passenger).__name__}")
        
        return Flight(flight_number, scheduled_time, aircraft, route, passenger)
        
