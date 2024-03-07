# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Anthony Cox, Will Wadsworth
# Date: 2/18/2024
#
# Description:
#   This module defines and implements the model class `Aircraft` as well as the factories and enumerated types for constructing them.
from __future__ import annotations
from enum import IntEnum
from typing import Union
from models.airport import Airport
from singletons.ledger import Ledger, LedgerEntry, LedgerEntryType

class AircraftType(IntEnum):
    """Enumerated type. Defines the 4 types of aircraft"""
    BOEING_737_600 = 0
    BOEING_737_800 = 1
    AIRBUS_A200_100 = 2
    AIRBUS_A220_300 = 3
    
class AircraftStatus(IntEnum):
    """Enumerated type. Defines the 7 unique possible states of an aircraft"""
    AVAILABLE = 0
    IN_MAINTENANCE = 1
    ON_TARMAC = 2
    BOARDING_WITHOUT_REFUELING = 3
    BOARDING_WITH_REFUELING = 4
    DEBOARDING = 5
    IN_FLIGHT = 6

class Aircraft:
    """Model class. A generic representation of an aircraft. Type is indicated by AirCraft.Type"""
    def __init__(
            self, name: str, type: AircraftType, status: AircraftStatus, location: Union[Airport | None], 
            tail_number: str, passenger_capacity: int, cruise_speed: int, fuel_level: int, fuel_capacity: int, 
            fuel_efficiency: float, max_range: int
        ):
        self.name = name
        self.type = type
        self.status = status
        self.location = location
        self.tail_number = tail_number
        self.passenger_capacity = passenger_capacity
        self.cruise_speed = cruise_speed                # km / h
        self.fuel_level = fuel_level
        self.fuel_capacity = fuel_capacity              # gallons
        self.fuel_efficiency = fuel_efficiency
        self.flight_hours = 0
        self.wait_timer = WAIT_TIMERS.get(status, 0)
        self.max_range = max_range                      # km
        
    @property
    def needs_maintenance(self) -> bool:
        return self.flight_hours >= 200
        
    def set_status(self, status: AircraftStatus) -> None:
        """Sets the status of the aircraft AND sets the wait timer if applicable"""
        if (self.status == status):
            raise ValueError(f"Error: duplicate assignment of status {status.name} to aircraft {self.tail_number} (do you have a logic error?)")
        
        self.status = status
        self.wait_timer = WAIT_TIMERS.get(status, 0)
        
    def depart(self) -> None:
        Ledger.entries.append(LedgerEntryType.TAKEOFF_FEE, self.location.takeoff_fee)
        
        # TODO: - Record actual flight departure time in scheduler flight entry
        # TODO: - If the aircraft needs to refuel:
        # TODO:     - Refuel the aircraft with the required fuel for the trip
        # TODO:     - `[Subroutine::Ledger::Append]` Add fuel costs to ledger
        # TODO:     - Start timer for boarding wait time with extra refuel time (35m)
        # TODO: - Else
        # TODO:     - Start timer for boarding wait time without refueling (25m)
        # TODO: - Set plane location to null
        # TODO: - Start timer for flight time (flight-dependent)
        # TODO: set passenger location to null
        
        if len(self.location.tarmac) > 0:
            aircraft = self.location.tarmac.get()
            aircraft.set_status(AircraftStatus.DEBOARDING)
        else:
            self.location.gates += 1
        
        self.location = None
        
        
    def arrive(self, airport: Airport) -> None:
        """Simulates an aircraft landing at an airport"""
        self.location = airport
        Ledger.entries.append(LedgerEntryType.LANDING_FEE, airport.landing_fee)
        # TODO: increase actual flight arrival time in scheduler flight entry
        # TODO: increase aircraft flight hours by flight duration
        # TODO: decrease the aircraft fuel amount by fuel used
        if airport.gates > 0:
            airport.gates -= 1
            self.set_status(AircraftStatus.DEBOARDING)
        else:
            airport.tarmac.put(self)
            self.set_status(AircraftStatus.ON_TARMAC)
        
    def __repr__(self) -> str:
        return self.tail_number

class AircraftFactory:
    # Static class variables
    uuid = 0
        
    @staticmethod
    def __next_tail_number() -> str:
        """Internal AircraftFactory static method. Generates a next unique aircraft tail number"""
        tail_number = f"N{str(AircraftFactory.uuid).zfill(5)}"
        AircraftFactory.uuid += 1        
        return tail_number
    
    @staticmethod
    def create_aircraft(
            aircraft_type: AircraftType, status: AircraftStatus,
            location: Union[Airport | None], fuel_level: int
        ) -> Aircraft:
        """Factory class to create Aircraft objects. Uses AircraftType as the API."""
        if not type(aircraft_type) is AircraftType:
            raise TypeError(f"parameter 'aircraft_type' is not of enum type 'AircraftType'. Got type: {type(aircraft_type).__name__}")
        
        if not type(location) is Airport and not location is None:
            raise TypeError(f"parameter 'location' must be an airport or None")

        if fuel_level < 0:
            raise ValueError("fuel_level cannot be negative")

        match aircraft_type:
            case AircraftType.BOEING_737_600:
                if fuel_level > 6875:
                    raise ValueError(f"Fuel level is greater than Boeing 737-600 fuel capacity: {6875}")
                
                return Aircraft(
                    "Boeing 737-600", AircraftType.BOEING_737_600, status, location,
                    AircraftFactory.__next_tail_number(), 119, 1101, fuel_level, 6875, 
                    0.55, 5648
                )
    
            case AircraftType.BOEING_737_800:
                if fuel_level > 6875:
                    raise ValueError(f"Fuel level is greater than Boeing 767-800 fuel capacity: {6875}")
                
                return Aircraft(
                    "Boeing 767-800", AircraftType.BOEING_737_800, status, location,
                    AircraftFactory.__next_tail_number(), 189, 1101, fuel_level, 6875, 
                    0.44, 5665
                )
                
            case AircraftType.AIRBUS_A200_100:
                if fuel_level > 5790:
                    raise ValueError(f"Fuel level is greater than Boeing 767-800 fuel capacity: {5790}")
                
                return Aircraft(
                    "Airbus A200-100", AircraftType.AIRBUS_A200_100, status, location,
                    AircraftFactory.__next_tail_number(), 135, 1012, fuel_level, 5790, 
                    0.57, 5460
                )
            
            case AircraftType.AIRBUS_A220_300:
                if fuel_level > 5790:
                    raise ValueError(f"Fuel level is greater than Boeing 767-800 fuel capacity: {5790}")
                
                return Aircraft(
                    "Airbus A220-300", AircraftType.AIRBUS_A220_300, status, location,
                    AircraftFactory.__next_tail_number(), 160, 1012, fuel_level, 5790, 
                    0.66, 5920
                )
            
            case _:
                raise ValueError(f"parameter 'aircraft_type' not in range of AircraftType enum: [{min(AircraftType)},{max(AircraftType)}].")

WAIT_TIMERS: dict[AircraftStatus,int] = {
    AircraftStatus.IN_MAINTENANCE : 2160,
    AircraftStatus.BOARDING_WITHOUT_REFUELING : 25,
    AircraftStatus.BOARDING_WITH_REFUELING : 35,
    AircraftStatus.DEBOARDING : 15
}
