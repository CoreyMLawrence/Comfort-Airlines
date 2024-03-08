from __future__ import annotations
from typing import TYPE_CHECKING

from models.airport import Airport

if TYPE_CHECKING:
    from models.flight import Flight

class Passenger:
    uuid = 0
    
    def __init__(self, source_airport, destination: Airport):
        if not type(source_airport) is Airport:
            raise TypeError("Passenger parameter 'source_airport' must be an Airport object")
        
        if not type(destination) is Airport:
            raise TypeError("Passenger parameter 'destination' must be an Airport object")
        
        self.source_airport = source_airport
        self.location = source_airport
        self.destination = destination
        self.flights_taken: list[Flight] = []
        
        self.uuid = Passenger.uuid
        Passenger.uuid += 1