# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Corey Lawrence, Zach Christopher
# Date: 3/21/2024
#
# Description:
#   This module defines and implements the model class `route` which provides an object associated with 
#   a specific source, destination, and aircraft type.

from models.aircraft import AircraftType
from models.airport import Airport

class Route:
    def __init__(self, aircraft_type, source_airport, destination_airport, distance, daily_demand, estimated_flight_time, fuel_requirement):
        # Check for aircraft type
        if not isinstance(aircraft_type, AircraftType):
            raise TypeError("Aircraft type must be an instance of AircraftType")
        
        # Check for source airport
        if not isinstance(source_airport, Airport):
            raise TypeError("Source airport must be an instance of Airport")
        
        # Check for destination airport
        if not isinstance(destination_airport, Airport):
            raise TypeError("Destination airport must be an instance of Airport")
        
        # Check for positive distance
        if not isinstance(distance, float) or distance <= 0:
            raise ValueError("Distance must be a float greater than 0")
        
        # Check for positive daily demand
        if not isinstance(daily_demand, int) or daily_demand <= 0:
            raise ValueError("Daily demand must be an integer greater than 0")
        
        # Check for positive estimated flight time
        if not isinstance(estimated_flight_time, int) or estimated_flight_time <= 0:
            raise ValueError("Estimated flight time must be an integer greater than 0")
        
        # Check for positive fuel requirement
        if not isinstance(fuel_requirement, float) or fuel_requirement <= 0:
            raise ValueError("Fuel requirement must be a float greater than 0")
        
        self.aircraft_type = aircraft_type
        self.source_airport = source_airport
        self.destination_airport = destination_airport
        self.distance = distance
        self.daily_demand = daily_demand
        self.estimated_flight_time = estimated_flight_time
        self.fuel_requirement = fuel_requirement
