from __future__ import annotations
from typing import TYPE_CHECKING
import csv

from singletons.scheduler import Scheduler
from models.reports.report import Report
from helpers.default import default

if TYPE_CHECKING:
    from singletons.simulation import Simulation
    from models.flight import Flight

class FlightReport(Report):
    def __init__(self, filepath: str) -> None:
        self.outfile = open(filepath, "w", newline="")
        self.writer = csv.writer(self.outfile, delimiter=",")
        self.writer.writerow([
            "flight number", "source airport", "destination airport", 
            "number of passengers", "scheduled departure time", "scheduled arrival time", 
            "actual departure time", "actual arrival time", "aircraft tail number"
        ])
        
    def __del__(self) -> None:
        self.outfile.close()
        
        
    def log(self, flight: Flight) -> None:
        self.writer.writerow([
            flight.flight_number, flight.route.source_airport, flight.route.destination_airport,
            len(flight.passengers), flight.expected_departure_time, flight.expected_arrival_time,
            default(flight.actual_departure_time, "null"), default(flight.actual_arrival_time, "null"), flight.aircraft.tail_number
        ])