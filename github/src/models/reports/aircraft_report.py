from __future__ import annotations
from typing import TYPE_CHECKING
import csv

from models.reports.report import Report

if TYPE_CHECKING:
    from singletons.simulation import Simulation
    from models.aircraft import Aircraft

class AircraftReport(Report):
    def __init__(self, filepath: str) -> None:
        self.outfile = open(filepath, "w", newline="")
        self.writer = csv.writer(self.outfile, delimiter=",")
        self.writer.writerow(["aircraft tail number", "flight number", "source airport", "destination airport", "departure time", "arrival time", "number of passengers"])
        
    def __del__(self) -> None:
        self.outfile.close()
        
    def log(self, aircraft: Aircraft) -> None:
        for flight in aircraft.flights_taken:
            self.writer.writerow([
                aircraft.tail_number,
                flight.flight_number,
                str(flight.route.source_airport),
                str(flight.route.destination_airport),
                flight.actual_departure_time if not flight.actual_departure_time is None else "null",
                flight.actual_arrival_time if not flight.actual_arrival_time is None else "null",
                str(len(flight.passengers))
            ])