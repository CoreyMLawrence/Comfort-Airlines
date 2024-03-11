from __future__ import annotations
from typing import TYPE_CHECKING

from models.airport import Airport

if TYPE_CHECKING:
    from models.flight import Flight

class Passenger:
    uuid = 0
    
    def __init__(self, source_airport: Airport, destination: Airport):
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

    @property
    def expected_departure_time(self) -> int:
        if not self.flights_taken:
            raise Exception(f"Passenger {self.uuid} has no scheduled flights. You have a logic error.")
        
        if self.flights_taken[0].expected_departure_time is None:
            raise Exception(f"The expected departure time for passenger {self.uuid} has not been calculated. You have a logic error.")

        return self.flights_taken[0].expected_departure_time

    @property
    def actual_departure_time(self) -> int:
        if not self.flights_taken:
            raise Exception(f"Passenger {self.uuid} has no scheduled flights. You have a logic error.")
        
        if self.flights_taken[0].actual_departure_time is None:
            raise Exception(f"The actual departure time for passenger {self.uuid} has not been calculated. You have a logic error.")

        return self.flights_taken[0].actual_departure_time

    @property
    def expected_arrival_time(self) -> int:
        index_last_flight = len(self.flights_taken) - 1

        if not self.flights_taken:
            raise Exception(f"Passenger {self.uuid} has no scheduled flights. You have a logic error.")

        if self.flights_taken[index_last_flight].expected_arrival_time is None:
            raise Exception(f"The expected arrival time for passenger {self.uuid} has not been calculated. You have a logic error.")

        return self.flights_taken[index_last_flight].expected_arrival_time
    
    @property
    def actual_arrival_time(self) -> int:
        index_last_flight = len(self.flights_taken) - 1

        if not self.flights_taken:
            raise Exception(f"Passenger {self.uuid} has no scheduled flights. You have a logic error.")

        if self.flights_taken[index_last_flight].actual_arrival_time is None:
            raise Exception(f"The actual arrival time for passenger {self.uuid} has not been calculated. You have a logic error.")

        return self.flights_taken[index_last_flight].actual_arrival_time