from __future__ import annotations
from typing import TYPE_CHECKING
from decimal import Decimal
from enum import Enum
import csv

import structlog

from constants import DEBUG

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
    entries: list[LedgerEntry] = []
    logger = structlog.get_logger()
    
    def record(entry: LedgerEntry) -> None:
        if DEBUG:
            Ledger.logger.info("recorded ledger entry", type=entry.type.name, net_profit=str(entry.net_profit), location=entry.location.name)
        
        Ledger.entries.append(entry)

    def serialize(filepath: str) -> None:
        with open(filepath, "w", newline="") as outfile:
            writer = csv.writer(outfile, delimiter=",")
            writer.writerow(["item", "net profit", "time", "location"])
            
            for entry in Ledger.entries:
                writer.writerow([entry.type.name, entry.net_profit, entry.time, entry.location])