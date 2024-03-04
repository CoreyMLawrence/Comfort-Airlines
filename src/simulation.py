from __future__ import annotations
from typing import TYPE_CHECKING
import itertools
import time as t
from pprint import pprint

import structlog

from constants import MINUTES_PER_DAY
from helpers.reference_wrapper import ReferenceWrapper
from models.passenger import Passenger
from models.aircraft import Aircraft, AircraftStatus

if TYPE_CHECKING:
    from models.airport import Airport
    from models.route import Route

class Simulation:
    def __init__(self, duration: int, aircrafts: list[Aircraft], airports: list[Airport], routes: list[Route]):
        self.duration = duration
        self.aircrafts = aircrafts
        self.airports = airports
        self.routes = routes
        
        self.time = ReferenceWrapper(0)
        self.logger = structlog.get_logger()
        
    def spawn_passengers(self) -> None:
        for airport in self.airports:
            for route in airport.routes:
                airport.passengers.extend([Passenger(route.source_airport, route.destination_airport) for _ in range(route.demand)])
            
    def run(self) -> None:
        while self.time.value < self.duration:
            if self.time.value % MINUTES_PER_DAY == 0:
                self.spawn_passengers()
                
            for aircraft in self.aircrafts:
                if aircraft.status == AircraftStatus.AVAILABLE:
                    if aircraft.needs_maintenance:
                        pass
                    
            self.logger.info(f"time: {self.time.value}")
            t.sleep(3)
            
            self.time.value += 1
            
        