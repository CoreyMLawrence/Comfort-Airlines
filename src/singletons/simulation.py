# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Anthony Cox
# Date: 3/21/2024
#
# Description:
#   This is the file that will implement and run the simulation.

from __future__ import annotations
from typing import TYPE_CHECKING
import time

import structlog

from helpers.reference_wrapper import ReferenceWrapper

if TYPE_CHECKING:
    from models.aircraft import Aircraft
    from models.airport import Airport
    from models.route import Route
    from models.passenger import Passenger

class Simulation:
    def __init__(self, duration: int, aircrafts: list[Aircraft], airports: list[Airport], routes: list[Route]):
        self.duration = duration
        self.aircrafts = aircrafts
        self.airports = airports
        self.routes = routes
        self.passengers: list[Passenger] = []
        
        self.time = ReferenceWrapper(0)
        self.logger = structlog.get_logger()

    def run(self) -> None:
        while True:
            self.logger.info("example log statement")
            time.sleep(3)
            
            self.time.value += 1