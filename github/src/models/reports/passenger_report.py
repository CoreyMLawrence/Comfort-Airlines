from __future__ import annotations
from typing import TYPE_CHECKING
import csv

from models.reports.report import Report

if TYPE_CHECKING:
    from models.passenger import Passenger

if TYPE_CHECKING:
    from singletons.simulation import Simulation

class PassengerReport(Report):
    def __init__(self, filepath: str) -> None:
        self.outfile = open(filepath, "w", newline="")
        self.writer = csv.writer(self.outfile, delimiter=",")
        self.writer.writerow(["uuid", "location", "source airport", "destination airport", "expected departure time", "expected arrival time", "actual departure time", "actual arrival time", "flights taken"])
        
    def __del__(self) -> None:
        self.outfile.close()
        
    def log(self, passenger: Passenger):
        self.writer.writerow([
            str(passenger.uuid),
            str(passenger.location) if not passenger.location is None else "null",
            str(passenger.source_airport),
            str(passenger.destination),
            passenger.expected_departure_time if passenger.flights_taken else "null",
            passenger.expected_arrival_time if passenger.flights_taken else "null",
            passenger.actual_departure_time if not passenger.location is None and passenger.location != passenger.source_airport else "null",
            passenger.actual_arrival_time if passenger.location == passenger.destination else "null",
            ";".join(map(lambda flight: str(flight.flight_number), passenger.flights_taken)) if passenger.flights_taken else "null"
        ])