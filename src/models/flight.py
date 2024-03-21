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
            self, flight_number: int, scheduled_time: int, aircraft: Aircraft, route: Route, passengers: list[Passenger]
        ):
        
        # Check flight_number type
        if not type(flight_number) is int:
            raise TypeError(f"parameter 'flight_number' is not of type 'int'. Got type: {type(flight_number)}")

        # Check for positive flight_number
        if flight_number < 0:
            raise ValueError("flight_number cannot be negative")
        
        # Check scheduled_time type
        if not type(scheduled_time) is int:
            raise TypeError(f"parameter 'scheduled_time' is not of type 'int'. Got type: {type(scheduled_time)}")
        
        # Check for positive scheduled_time
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
        
        self.flight_number = flight_number
        self.scheduled_time = scheduled_time
        self.aircraft = aircraft
        self.route = route
        self.passengers = passengers

