from __future__ import annotations
from typing import TYPE_CHECKING
import csv

from singletons.reports.report import Report

if TYPE_CHECKING:
    from simulation import Simulation

class PassengerReport(Report):
    @staticmethod
    def generate(filepath: str, simulation: Simulation) -> None:
        with open(filepath, "w", newline="") as outfile:
            writer = csv.writer(outfile, delimiter=",")
            
            writer.writerow(["uuid", "location", "source airport", "destination airport", "expected departure time", "expected arrival time", "actual departure time", "actual arrival time", "flights taken"])
            for passenger in simulation.passengers:
                writer.writerow([
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
        