# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Date: 2/19/2024
#
# Description:
#   This module is the entry point to the program. All pre-program initialization is performed
#   here before the simulation is started.
from typing import TYPE_CHECKING

import structlog

from constants import SIMULATION_DURATION
import log.processors as processors
from helpers.reference_wrapper import ReferenceWrapper
from singletons.simulation import Simulation

if TYPE_CHECKING:
    from models.aircraft import Aircraft
    from models.aircraft import Airport
    from models.route import Route

def main() -> None:
    """The entry point for the application"""

    aircrafts: list[Aircraft] = []
    airports: list[Airport] = []
    routes: list[Route] = []
    
    simulation = Simulation(SIMULATION_DURATION, aircrafts, airports, routes)
    
    structlog.configure(
        processors=[
            processors.CodeLocation(),
            processors.ProcessorID(),
            processors.ProcessorSimulationTime(simulation.time),
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="%H:%M:%S", utc=True, key="real_time"),
            structlog.processors.JSONRenderer()
        ]
    )
    
    simulation.run()

if __name__ == "__main__":
    main()