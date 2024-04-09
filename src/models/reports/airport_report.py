from __future__ import annotations
from typing import TYPE_CHECKING
import csv

from models.reports.report import Report
from helpers.default import default

if TYPE_CHECKING:
    from singletons.simulation import Simulation
    from models.aircraft import Aircraft

class AirportReport(Report):
    def __init__(self, filepath: str) -> None:
        self.outfile = open(filepath, "w", newline="")
        self.writer = csv.writer(self.outfile, delimiter=",")
        self.writer.writerow(["type (arrival/departure)", "airport", "arrival/departure time", "aircraft flight number", "number of passengers", "aircraft tail number"])
        
    def __del__(self) -> None:
        self.outfile.close()
        
        
    def log(self, aircraft: Aircraft) -> None:
        ARRIVAL: str = "arrival"
        DEPARTURE: str = "departure"

        for flight in aircraft.flights_taken:
            self.writer.writerow([
                DEPARTURE, str(flight.route.source_airport), default(flight.actual_departure_time, "null"), 
                str(flight.flight_number), str(len(flight.passengers)), aircraft.tail_number 
            ])
            
            self.writer.writerow([
                ARRIVAL, str(flight.route.destination_airport), default(flight.actual_arrival_time, "null"), str(flight.flight_number), 
                str(len(flight.passengers)), aircraft.tail_number 
            ])