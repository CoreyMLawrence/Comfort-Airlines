from __future__ import annotations
from typing import TYPE_CHECKING
import time as t

import structlog

from helpers.reference_wrapper import ReferenceWrapper

if TYPE_CHECKING:
    from models.aircraft import Aircraft
    from models.airport import Airport
    from models.route import Route

class Simulation:
    def __init__(self, duration: int, aircraft: list[Aircraft], airports: list[Airport], routes: list[Route]):
        self.duration = duration
        self.aircraft = aircraft
        self.airports = airports
        self.routes = routes
        
        self.time = ReferenceWrapper(0)
        self.logger = structlog.get_logger()
        
    def run(self) -> None:
        while self.time.value < self.duration:
            for airport in self.airports:
                pass # respawn population
            
            self.logger.info(f"time: {self.time.value}")
            t.sleep(3)
            
            self.time.value += 1