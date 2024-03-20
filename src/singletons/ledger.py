from __future__ import annotations
from typing import TYPE_CHECKING
from decimal import Decimal
from enum import Enum

if TYPE_CHECKING:
    from models.airport import Airport

class LedgerEntryType(Enum):
    FUEL = 0
    TAKEOFF_FEE = 1
    LANDING_FEE = 2
    PLANE_RENTAL = 3
    TICKET_SALES = 4

class LedgerEntry:
    def __init__(self, type: LedgerEntryType, net_profit: Decimal, time: int, location: Airport):
        self.type = type
        self.net_profit = net_profit
        self.time = time
        self.location = location
        
    def __repr__(self) -> str:
        return f"[{self.type.name}] {self.net_profit} (location: {self.location}, time: {self.time})"

class Ledger:
    entries: list[LedgerEntry] = []