# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Date: 2/19/2024
#
# Description:
#   This module is the entry point to the program. All pre-programm initialization is performed
#   here before the simulation is started.
import structlog
import processors
import time

from reference_wrapper import ReferenceWrapper

def main() -> None:
    """The entry point for the application"""
    simulation_time = ReferenceWrapper(0)
    
    structlog.configure(
        processors=[
            processors.processor_code_location,
            processors.ProcessorID(0),
            processors.ProcessorSimulationTime(simulation_time),
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="%H:%M:%S", utc=True, key="real_time"),
            structlog.processors.JSONRenderer()
        ]
    )
    

    # EXAMPLE - FEEL FREE TO CHANGE
    log = structlog.get_logger()

    while True:
        log.info("Hello, comfort airlines!")
        simulation_time.value += 1
        time.sleep(5)

if __name__ == "__main__":
    main()