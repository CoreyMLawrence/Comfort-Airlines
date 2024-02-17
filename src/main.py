import structlog
import logger
import time

def main() -> None:
    """The entry point for the application"""
    structlog.configure(
        processors=[
            logger.processor_code_location,
            logger.ProcessorID(0),
            structlog.contextvars.merge_contextvars,
            structlog.processors.TimeStamper(fmt="%H:%M:%S", utc=True, key="real_time"),
            structlog.processors.JSONRenderer()
        ]
    )
    
    log = structlog.get_logger()

    while True:
        log.info("Hello, comfort airlines!")
        time.sleep(5)

if __name__ == "__main__":
    main()