# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Dylan Hudson
# Date: 3/18/2024
#
# Description:
#   This module defines and implements the model class `Flight`.

from models.aircraft import Aircraft
from models.route import Route
from models.passenger import Passenger

class Flight:
    """Model class. A generic representation of a flight."""
    def __init__(
            self, flight_number: int, scheduled_time: int, aircraft: Aircraft, route: Route, passengers: list[Passenger], 
            expected_departure_time: int, expected_arrival_time: int
        ):
        
        # Check flight_number type
        if not type(flight_number) is int:
            raise TypeError(f"parameter 'flight_number' is not of type 'int'. Got type: {type(flight_number)}")

        # Check if negative flight_number
        if flight_number < 0:
            raise ValueError("flight_number cannot be negative")
        
        # Check scheduled_time type
        if not type(scheduled_time) is int:
            raise TypeError(f"parameter 'scheduled_time' is not of type 'int'. Got type: {type(scheduled_time)}")
        
        # Check if negative scheduled_time
        if scheduled_time < 0:
            raise ValueError("scheduled_time cannot be negative")
        
        # Check aircraft type
        if not type(aircraft) is Aircraft:
            raise TypeError(f"parameter 'aircraft' is not of type 'Aircraft'. Got type: {type(aircraft)}")
        
        # Check route type
        if not type(route) is Route:
            raise TypeError(f"parameter 'route' is not of type 'Route'. Got type: {type(route)}")
        
        # Check type for all passengers
        if any(not type(passenger) is Passenger for passenger in passengers):
            raise TypeError("Flight parameter 'passengers' must be a list of Passenger objects")
        
        # Check expected_departure_time type
        if not type(expected_departure_time) is int:
            raise TypeError(f"parameter 'expected_departure_time' is not of type 'int'. Got type: {type(expected_departure_time)}")
        
        # Check if negative expected_departure_time
        if expected_departure_time < 0:
            raise ValueError("expected_departure_time cannot be negative")
        
        # Check expected_arrival_time type
        if not type(expected_arrival_time) is int:
            raise TypeError(f"parameter 'expected_arrival_time' is not of type 'int'. Got type: {type(expected_arrival_time)}")
        
        # Check if negative expected_arrival_time
        if expected_arrival_time < 0:
            raise ValueError("expected_arrival_time cannot be negative")
        
        self.flight_number = flight_number
        self.scheduled_time = scheduled_time
        self.aircraft = aircraft
        self.route = route
        self.passengers = passengers
        self.expected_departure_time = expected_departure_time
        self.expected_arrival_time = expected_arrival_time
        self.actual_departure_time = None
        self.actual_arrival_time = None
        

    def set_actual_departure_time(self, actual_departure_time: int) -> None:
        # Check actual_departure_time type
        if not type(actual_departure_time) is int:
            raise TypeError(f"parameter 'actual_departure_time' is not of type 'int'. Got type: {type(actual_departure_time)}")
        
        # Check if negative actual_departure_time
        if actual_departure_time < 0:
            raise ValueError("actual_departure_time cannot be negative")
        
        self.actual_departure_time = actual_departure_time
        

    def set_actual_arrival_time(self, actual_arrival_time: int) -> None:
        # Check actual_arrival_time type
        if not type(actual_arrival_time) is int:
            raise TypeError(f"parameter 'actual_arrival_time' is not of type 'int'. Got type: {type(actual_arrival_time)}")
        
        # Check if negative actual_arrival_time
        if actual_arrival_time < 0:
            raise ValueError("actual_arrival_time cannot be negative")
        
        self.actual_arrival_time = actual_arrival_time
