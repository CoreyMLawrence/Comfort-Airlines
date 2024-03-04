from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from models.airport import Airport

class Passenger:
    uuid = 0
    
    def __init__(self, destination: Airport, location: Union[Airport, None]):
        self.destination = destination
        self.location = location
        
        self.uuid = Passenger.uuid
        Passenger.uuid += 1
        
    def __repr__(self) -> str:
        return str(self.uuid)