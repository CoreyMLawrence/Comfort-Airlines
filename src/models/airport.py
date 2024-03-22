# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Corey Lawrence, Dylan Hudson
# Date: 3/9/2024
#
# Description:
#   This module defines and implements the model class `Airport` as well as the factories and enumerated types for constructing them.

from decimal import Decimal
from enum import Enum
from queue import Queue

class AirportType(Enum):
    """Enumerated type. Defines the 2 types of airports."""
    LOCAL = 0
    HUB = 1

class Airport:
    """Model class. A generic representation of an airport."""
    def __init__(
            self, name: str, iata_code: str, city: str, state: str, metro_population: int,
            is_hub: bool, available_gates: int, latitude: float, longitude: float,
            gas_price: float, takeoff_fee: Decimal, landing_fee: Decimal, tarmac: Queue
        ):
        
        # Check name type
        if not type(name) is str:
            raise TypeError(f"parameter 'name' is not of type 'str'. Got type: {type(name)}")
        
        # Check iata_code type
        if not type(iata_code) is str:
            raise TypeError(f"parameter 'iata_code' is not of type 'str'. Got type: {type(iata_code)}")
        
        # Check city type
        if not type(city) is str:
            raise TypeError(f"parameter 'city' is not of type 'str'. Got type: {type(city)}")
        
        # Check state type
        if not type(state) is str:
            raise TypeError(f"parameter 'state' is not of type 'str'. Got type: {type(state)}")
        
        # Check metro_population type
        if not type(metro_population) is int:
            raise TypeError(f"parameter 'metro_population' is not of type 'int'. Got type: {type(metro_population)}")
        
        # Check if negative metro_population
        if metro_population < 0:
            raise ValueError("metro_population cannot be negative")
        
        # Check is_hub type
        if not type(is_hub) is bool:
            raise TypeError(f"parameter 'is_hub' is not of type 'bool'. Got type: {type(is_hub)}")
        
        # Check available_gates type
        if not type(available_gates) is int:
            raise TypeError(f"parameter 'available_gates' is not of type 'int'. Got type: {type(available_gates)}")
        
        # Check if negative available_gates
        if available_gates < 0:
            raise ValueError("available_gates cannot be negative")
        
        # Check latitude type
        if not type(latitude) is float:
            raise TypeError(f"parameter 'latitude' is not of type 'float'. Got type: {type(latitude)}")
        
        # Check if latitude is in proper range (-90 to 90)
        if latitude < -90 or latitude > 90:
            raise ValueError("latitude value must be between -90 and 90")
        
        # Check longitude type
        if not type(longitude) is float:
            raise TypeError(f"parameter 'longitude' is not of type 'float'. Got type: {type(longitude)}")
        
        # Check if longitude is in proper range (-180 to 180)
        if longitude < -180 or longitude > 180:
            raise ValueError("longitude value must be between -180 and 180")
        
        # Check gas_price type
        if not type(gas_price) is float:
            raise TypeError(f"parameter 'gas_price' is not of type 'float'. Got type: {type(gas_price)}")
        
        # Check if negative gas_price
        if gas_price < 0:
            raise ValueError("gas_price cannot be negative")
        
        # Check takeoff_fee type
        if not type(takeoff_fee) is Decimal:
            raise TypeError(f"parameter 'takeoff_fee' is not of type 'Decimal'. Got type: {type(takeoff_fee)}")
        
        # Check if negative takeoff_fee
        if takeoff_fee < 0:
            raise ValueError("takeoff_fee cannot be negative")
        
        # Check landing_fee type
        if not type(landing_fee) is Decimal:
            raise TypeError(f"parameter 'landing_fee' is not of type 'Decimal'. Got type: {type(landing_fee)}")
        
        # Check if negative landing_fee
        if landing_fee < 0:
            raise ValueError("landing_fee cannot be negative")
        
        # Check tarmac type
        if not type(tarmac) is Queue:
            raise TypeError(f"parameter 'tarmac' is not of type 'Queue'. Got type: {type(tarmac)}")
        
        self.name = name
        self.iata_code = iata_code
        self.city = city
        self.state = state
        self.metro_population = metro_population
        self.is_hub = is_hub
        self.available_gates = available_gates
        self.latitude = latitude
        self.longitude = longitude
        self.gas_price = gas_price
        self.takeoff_fee = takeoff_fee
        self.landing_fee = landing_fee
        self.tarmac = tarmac
