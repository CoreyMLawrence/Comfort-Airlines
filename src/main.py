import structlog
import logger
import time

from reference_wrapper import ReferenceWrapper

def main() -> None:
    """The entry point for the application"""
    simulation_time = ReferenceWrapper(0)
    
    structlog.configure(
        processors=[
            logger.processor_code_location,
            logger.ProcessorID(0),
            logger.ProcessorSimulationTime(simulation_time),
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="%H:%M:%S", utc=True, key="real_time"),
            structlog.processors.JSONRenderer()
        ]
    )
    
    log = structlog.get_logger()

    while True:
        log.info("Hello, comfort airlines!")
        simulation_time.value += 1
        time.sleep(5)

if __name__ == "__main__":
    main()