# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Anthony Cox
# Date: 3/21/2024
#
# Description:
#   This program creates the constant variables that we will use in our simulation.

from decimal import Decimal
from models.airport import Airport

# Debugging
DEBUG = False
VERBOSE = DEBUG and False

# Simulation constants
MINUTES_PER_DAY = 1440
SIMULATION_DURATION_DAYS = 14
SIMULATION_DURATION = MINUTES_PER_DAY * SIMULATION_DURATION_DAYS

# Airport constants
DEFAULT_TAKEOFF_FEE = Decimal("2000")
DEFAULT_LANDING_FEE = Decimal("2000")
DEFAULT_GAS_PRICE = Decimal("6.19")