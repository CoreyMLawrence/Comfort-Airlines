from __future__ import annotations
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from models.airport import Airport

class Passenger:
    uuid = 0
    
    def __init__(self, location: Union[Airport, None], destination: Airport):
        self.location = location
        self.destination = destination
        
        self.uuid = Passenger.uuid
        Passenger.uuid += 1