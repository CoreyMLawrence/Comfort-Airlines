from __future__ import annotations
from typing import TYPE_CHECKING
import csv

from singletons.scheduler import Scheduler
from singletons.reports.report import Report
from helpers.default import default

if TYPE_CHECKING:
    from simulation import Simulation

class FlightReport(Report):
    @staticmethod
    def generate(filepath: str, simulation: Simulation) -> None:
        with open(filepath, "w", newline="") as outfile:
            writer = csv.writer(outfile, delimiter=",")
            writer.writerow([
                "flight number", "source airport", "destination airport", 
                "number of passengers", "scheduled departure time", "scheduled arrival time", 
                "actual departure time", "actual arrival time", "aircraft tail number"
            ])
            
            for flight in Scheduler.flights:
                writer.writerow([
                    flight.flight_number, flight.route.source_airport, flight.route.destination_airport,
                    len(flight.passengers), flight.expected_departure_time, flight.expected_arrival_time,
                    default(flight.actual_departure_time, "null"), default(flight.actual_arrival_time, "null"), flight.aircraft.tail_number
                ])