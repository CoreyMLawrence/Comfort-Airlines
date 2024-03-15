from __future__ import annotations
from typing import TYPE_CHECKING
import itertools
import time as t
from pprint import pprint

import structlog
from haversine import haversine

from constants import MINUTES_PER_DAY
from singletons.scheduler import Scheduler

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
        self.passengers: list[Passenger] = []
        
        self.time = ReferenceWrapper(0)
        self.logger = structlog.get_logger()
        
    def spawn_passengers(self) -> None:
        self.passengers = list(filter(lambda passenger: passenger.location != passenger.source_airport, self.passengers))
        
        for route in self.routes:
            self.passengers.extend([Passenger(route.source_airport, route.destination_airport) for _ in route.demand])

    def run(self) -> None:
        while self.time.value < self.duration:
            if self.time.value % MINUTES_PER_DAY == 0:
                self.passengers = list(filter(lambda passenger: passenger.location != passenger.source_airport, self.passengers))
                self.spawn_passengers()
                
            for aircraft in self.aircrafts:
                if aircraft.status == AircraftStatus.AVAILABLE:
                    if aircraft.needs_maintenance:
                        if aircraft.location.is_hub and aircraft.location.maintenance_gates > 0:
                            aircraft.location.maintenance_gates -= 1
                            aircraft.set_status(AircraftStatus.IN_MAINTENANCE)
                        else:
                            # TODO: fix this bullshit
                            # Schedule the aircraft for a flight to the hub with the shortest wait time
                            #if len(available_hubs := list(filter(lambda hub: hub.maintenance_gates > 0, HUBS.values()))) > 0:
                            #    closest_available_hub = sorted()[0]
                            #
                            #Scheduler.schedule_flight(aircraft, None, [])
                            #closest_available_hub.maintenance_gates -= 1
                            #aircraft.set_status(AircraftStatus.IN_MAINTENANCE)
                            pass
                    else:
                        # Schedule the aircraft for the most profitable, available flight that can be made within operating hours (if any)
                        pass
                else:
                    if aircraft.status == AircraftStatus.IN_FLIGHT and aircraft.wait_timer <= 0:
                        aircraft.arrive()
                    
                    if aircraft.status == AircraftStatus.IN_MAINTENANCE and aircraft.wait_timer <= 0:
                        aircraft.set_status(AircraftStatus.AVAILABLE)
                        aircraft.flight_hours = 0
                        
                        if aircraft.location.gates > 0:
                            aircraft.location.gates -= 1
                            aircraft.set_status(AircraftStatus.AVAILABLE)
                        else:
                            aircraft.location.tarmac.put(aircraft)
                            aircraft.set_status(AircraftStatus.ON_TARMAC)
                    
                    if aircraft.status in [AircraftStatus.BOARDING_WITHOUT_REFUELING, AircraftStatus.BOARDING_WITH_REFUELING] and aircraft.wait_timer <= 0:
                       aircraft.set_status(AircraftStatus.IN_FLIGHT)
                       aircraft.depart()

                    if aircraft.status == AircraftStatus.DEBOARDING and aircraft.wait_timer <= 0:
                        aircraft.set_status(AircraftStatus.AVAILABLE)
                        # TODO update passenger location
                    
            self.logger.info(f"time: {self.time.value}")
            t.sleep(3)
            
            for aircraft in self.aircrafts:
                if aircraft.wait_timer is not None:
                    aircraft.wait_timer -= 1
            self.time.value += 1