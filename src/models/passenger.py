from __future__ import annotations
from typing import Union

from models.airport import Airport

class Passenger:
    uuid = 0
    
    def __init__(self, location: Union[Airport, None], destination: Airport):
        if not type(location) is Airport and not location is None:
            raise TypeError("Passenger location must be an Airport object or None")
        
        if not type(destination) is Airport:
            raise TypeError("Passenger destination must be an Airport object")
        
        self.location = location
        self.destination = destination
        
        self.uuid = Passenger.uuid
        Passenger.uuid += 1