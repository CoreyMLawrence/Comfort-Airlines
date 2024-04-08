from __future__ import annotations
from typing import TYPE_CHECKING
import csv

from singletons.reports.report import Report

if TYPE_CHECKING:
    from simulation import Simulation

class AircraftReport(Report):
    @staticmethod
    def generate(filepath: str, simulation: Simulation) -> None:
        with open(filepath, "w", newline="") as outfile:
            writer = csv.writer(outfile, delimiter=",")
            
            writer.writerow(["aircraft tail number", "flight number", "source airport", "destination airport", "departure time", "arrival time", "number of passengers"])
            for aircraft in simulation.aircrafts:
                for flight in aircraft.flights_taken:
                    writer.writerow([
                        aircraft.tail_number,
                        flight.flight_number,
                        str(flight.route.source_airport),
                        str(flight.route.destination_airport),
                        flight.actual_departure_time if not flight.actual_departure_time is None else "null",
                        flight.actual_arrival_time if not flight.actual_arrival_time is None else "null",
                        str(len(flight.passengers))
                    ])
        