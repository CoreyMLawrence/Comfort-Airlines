from decimal import Decimal

# Debugging
DEBUG = True
VERBOSE = DEBUG and False

# Data
SIMULATION_OUTPUT_DIRECTORY = "simulation-output"

# Simulation constants
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = MINUTES_PER_HOUR * 24
SIMULATION_DURATION_DAYS = 14
SIMULATION_DURATION = MINUTES_PER_DAY * SIMULATION_DURATION_DAYS

# Airport constants
DEFAULT_TAKEOFF_FEE = Decimal("2000")
DEFAULT_LANDING_FEE = Decimal("2000")
DEFAULT_GAS_PRICE = Decimal("6.19")

HUB_NAMES = {
    "Hartsfield-Jackson Atlanta International Airport",
    "Dallas/Fort Worth International Airport",
    "Denver International Airport",
    "O'Hare International Airport"
}