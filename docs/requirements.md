# Requirements
In accordance with the descriptions provided by the client in the preliminary contract and in-person meetings, 
the goal of this project is to determine the financial viability of starting a new airline named Comfort Airlines. 
The primary deliverable is an interactive simulation of two weeks of airport activity for Comfort Airlines. 
The simulation is based on the primary subdeliverable, a two-week flight timetable that includes all flight, airport, 
aircraft, and passenger data. The simulation will be delivered as a Docker stack composed of a Python 3.10 application 
service and a MariaDB 11.2 service, which communicate over an internal bridge network. All dependencies and configurations 
will be self-contained within the Docker containers, allowing them to be run in any environment.

# Primary Deliverable: Two-week Flight Simulation
The simulation will be a platform-independent graphic user interface (GUI) using [PyQt6](https://pypi.org/project/PyQt6/). 
The simulation will allow the client to view the timetable graphically as well as interact with it 
directly by booking flights between airports. After the simulation, a report containing the number 
of passengers transported, operating costs, revenue raised, and net profit will be generated.

# Primary Subdeliverable: Two-week Flight Timetable
Since calculating every possible timetable to find the perfect timetable is computationally infeasible, 
we will use a genetic algorithm (via [PyGAD](https://pypi.org/project/pygad/)) to iteratively generate 
successively better timetables until a suitable timetable has been found. After which point, a member 
of the team will manually resolve any of the remaining minor problems. This timetable will be stored 
in the MariaDB database and made available to the Python simulation application and to the client in 
printed form.