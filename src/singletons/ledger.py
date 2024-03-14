from __future__ import annotations
from typing import TYPE_CHECKING
from decimal import Decimal
from enum import Enum

class LedgerEntryType(Enum):
    FUEL = 0
    TAKEOFF_FEE = 1
    LANDING_FEE = 2
    PLANE_RENTAL = 3
    TICKET_SALES = 4

class LedgerEntry:
    def __init__(self, type: LedgerEntryType, net_profit: Decimal):
        self.type = type
        self.net_profit = net_profit
        
    def __repr__(self) -> str:
        return f"[{self.type.name}] {self.net_profit}"

class Ledger:
    entries: list[LedgerEntry] = []