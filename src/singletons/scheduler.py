from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.aircraft import Aircraft
    from models.route import Route
    from models.passenger import Passenger
    from models.flight import Flight

class Scheduler:
    flight_uuid = 0
    flights: list[Flight] = []
    
    @staticmethod
    def __next_flight_uuid() -> int:
        id = Scheduler.flight_uuid
        Scheduler.flight_uuid += 1

        return id
        
    def schedule_flight(aircraft: Aircraft, routes: list[Route], passengers: list[Passenger]) -> Flight:
        raise NotImplementedError()
            
        flight = Flight(
            Scheduler.__next_flight_uuid(),
            aircraft,
            routes[0],
            passengers
        )   
        
        Scheduler.flights.append(flight)
        return flight
    
    def schedule_maintenance_flight(aircraft: Aircraft, routes: list[Route], passengers: list[Passenger]) -> Flight:
        raise NotImplementedError()
        
        flight = Flight(
            Scheduler.__next_flight_uuid(),
            aircraft,
            routes[0],
            passengers     
        )
        
        Scheduler.flights.append(flight)
        return flight