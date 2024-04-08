from __future__ import annotations
from typing import TYPE_CHECKING
import csv

from singletons.reports.report import Report
from helpers.default import default

if TYPE_CHECKING:
    from simulation import Simulation

class AirportReport(Report):
    @staticmethod
    def generate(filepath: str, simulation: Simulation) -> None:
        ARRIVAL: str = "arrival"
        DEPARTURE: str = "departure"
        
        with open(filepath, "w", newline="") as outfile:
            writer = csv.writer(outfile, delimiter=",")
            
            writer.writerow(["type (arrival/departure)", "airport", "arrival/departure time", "aircraft flight number", "number of passengers", "aircraft tail number"])
            for aircraft in simulation.aircrafts:
                for flight in aircraft.flights_taken:
                    writer.writerow([
                        DEPARTURE, str(flight.route.source_airport), default(flight.actual_departure_time, "null"), 
                        str(flight.flight_number), str(len(flight.passengers)), aircraft.tail_number 
                    ])
                    
                    writer.writerow([
                        ARRIVAL, str(flight.route.destination_airport), default(flight.actual_arrival_time, "null"), str(flight.flight_number), 
                        str(len(flight.passengers)), aircraft.tail_number 
                    ])
        