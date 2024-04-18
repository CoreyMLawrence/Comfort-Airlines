from __future__ import annotations
from typing import TYPE_CHECKING
from decimal import Decimal
from enum import Enum
import csv
import os

import structlog

from constants import DEBUG, SIMULATION_OUTPUT_DIRECTORY
from helpers.default import default

if TYPE_CHECKING:
    from models.airport import Airport

class LedgerEntryType(Enum):
    FUEL = 0
    TAKEOFF_FEE = 1
    LANDING_FEE = 2
    PLANE_RENTAL = 3
    TICKET_SALES = 4

class LedgerEntry:
    def __init__(self, type: LedgerEntryType, net_profit: Decimal, time: int, location: Airport | None):
        self.type = type
        self.net_profit = net_profit
        self.time = time
        self.location = location

class Ledger:
    def __init__(self):
        self.logger = structlog.get_logger()
        self.outfile = open(os.path.join(SIMULATION_OUTPUT_DIRECTORY, "ledger.csv"), "w", newline="")
        self.writer = csv.writer(self.outfile, delimiter=",")
        
        self.writer.writerow(["item", "net profit", "time", "location"])

    def __del__(self):
        self.outfile.close()

    def record(self, entry: LedgerEntry) -> None:
        if DEBUG:
            self.logger.info("recorded ledger entry", type=entry.type.name, net_profit=str(entry.net_profit), location=entry.location.name if not entry.location is None else "null")
        
        self.writer.writerow([entry.type.name, entry.net_profit, entry.time, entry.location if not entry.location is None else "null"])