# Software Requirements Specification (SRS)
This software requirements specification completely defines the aircraft simulation software project contracted by 
Comfort Airlines on 2024-01-07. All project requirements are defined within this source-of-truth specification document.

# 0. Table of Contents
The table of contents provide quick-access to the major sections of the document.

0. [Table of Contents](#0-table-of-contents)
1. [Introduction](#1-introduction)
2. [Functional Requirements](#2-functional-requirements)
3. [Non-functional Requirements](#3-non-functional-requirements)
4. [Deliverables](#4-deliverables)
5. [Unattempted Functionality](#5-unattempted-functionality)
6. [Assurance](#6-assurance)
7. [Appendix](#6-appendix)

# 1. Introduction

## 1.1 Executive Summary
The fundamental purpose of the simulation is to assess the robustness of business plan developed by Comfort Airlines.
The simulation should be sufficiently realistic to generate approximations of the net profit for a two week period,
assuming a 2% market share.

## 1.2 Scope
The scope of the project is to develop a standard schedule (colq. "timetable") for the set of 55 airplanes rented by
Comfort Airlines and then use the timetable to simulate two weeks of flight time. The simulation will be used to generate 
a report of business profits, expenses, and general business statistics.The standard schedule developed
will be based on chapters 2 and 3 of the IATA Standard Schedules Information Manual: "*Information Required for Standard
Schedules (Data Requirements, Data Representation, Data Elements and Data Element Identifiers)*" and "*Standard Print
Layouts for Schedules Information (Data Elements Required, Code Sharing Flights, Plan Change, Examples)*".

## 1.3 Document Conventions
This document uses Markdown formatting. The document is divided into major sections denoted by
sections headers declared with a single `#` character and minor sections denoted by section header declared
with two consecutive `#` characters. Markdown is traditionally compiled and rendered as HTML, but can also
be rendered in other formats such as PDF for flexibility. For more information about Markdown's features,
visit the the Markdown standard, RFC 7763.

## 1.4 Intended Audiences
The intended audience of this document is the client company that contracted the work, Comfort Airlines,
and technical and non-technical team members working on the project, including but not limited to the 
project manager, product owner, and software developers. Knowledge of technical jargon used in software development
and project management is assumed.

## 1.5 External References
- [Databases: 3.5 Normal Form](https://www.relationaldbdesign.com/database-analysis/module4/four-important-rules.php)
- [FAA: Aircraft Registration Guidelines](https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/forming_nnumber)
- [IATA  Standard Schedules Information Manual (SSIM)](https://www.iata.org/en/publications/store/standard-schedules-information/)
- [IEEE: Markdown Standard - RFC 7763](https://datatracker.ietf.org/doc/html/rfc7763)
- [ISO 8601: Date and Time Standardization](https://www.iso.org/iso-8601-date-and-time-format.html)
- [MariaDB: Overview](https://mariadb.org/about/)
- [DockerHub: Official MariaDB Image](https://hub.docker.com/_/mariadb)
- [DockerHub: Official Python 3 Image](https://hub.docker.com/_/python)
- [Pep 8: Official Python Style Guide](https://pep8.org/)
- [PyTest: Overview](https://docs.pytest.org/en/8.0.x/)
- [Wikipedia: Charles de Gaulle Airport](https://en.wikipedia.org/wiki/Charles_de_Gaulle_Airport)
- [Wikipedia: Top 30 Busiest Airports in the United States](https://en.wikipedia.org/wiki/List_of_the_busiest_airports_in_the_United_States)
- [Wikipedia: Universal Coordinated Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)

# 2. Functional Requirements

## 2.1 Requirements Overview
- Review project requirements
- Pre-research Research and Data Collection
    - Functional Specification:
        Prior to the simulation, static data about the aircraft, airports, and simulation must be collected.
        - Collect all the information needed to model an aircraft, including the name, passenger capacity, cruise speed, fuel capacity, fuel efficiency, and maximum range
        - Aircraft tail numbers will comply with FAA aircraft registration guidelines (format: `N00000`)
        - Collect all the information needed to model an airport, including the name, IATA code, city, state, metro population, the number of available gates, the coordinates (latitude and longitude), gas price, and takeoff/landing fees
        - Calculate the cartesian product of the airports and the aircraft to derive all possible flights
        - Calculate all attributes of each flight for each aircraft, including the fuel required, flight duration, and net profit
        - Sort the flights by profitability
    - Tasks
        - Research shortest path algorithms (assigned to: Zach, due: 2024-01-18)
        - Research ideal hub attributes (assigned to: Dylan and Will, due: 2024-01-18)
        - Aggregate airport attributes from Wikipedia into CSV file (assigned to: Anthony, due: 2024-01-18)
        - Aggregate aircraft attributes from flight manuals into CSV file (assigned to: Corey, due: 2024-01-18)
        - Determine ideal hubs (assigned to: Dylan, due: 2024-02-01)
        - Calculate the cartesian product of airports and aircraft to derive all possible flights (assigned to: Corey, due: 2024-01-18)
        - Filter out flights between airports 150 mi or closer (assigned to: Corey, due: 2024-01-18)
        - Determine which airports share a metro population (assigned to: Anthony, due: 2024-01-18)
        - Calculate the demand for each flight based on metro populations (assigned to: Corey, due: 2024-02-01)
        - Calculate fuel capacity for each plane (assigned to: Dylan, due: 2024-02-01)
        - Calculate flight time for each flight (assigned to: Corey, due: 2024-02-09)
        - Calculate net profit for each flight (assigned to: Parker, due: 2024-02-09)
        - Calculate net profit per hour for each flight (assigned to: Corey, due: 2024-02-23)
        - Review project requirements and project status with client (assigned to: Everyone, due: 2024-02-23)
- Timetable Development
    - Functional Specification
        - The application should be containerized and deployed in official Python docker container, version 3.10
        - The timetable will consist of a list of flights, sorted by date and time in ascending order
        - Each flight in the timetable will consist of the light number, data of flight, departure airport, destination airport, number of passengers, scheduled, departure time, actual departure time, scheduled arrival time, actual arrival time, aircraft tail number
        - The timetable will prioritize profit, always flying the most profitable flights first, unless maintenance is required
        - If maintentance is required, a flight will be scheduled from the source airport to the nearest hub with available spots. When the flight is scheduled, a maintenance spot is reserved at the destination airport for the aircraft
        - Flights will only be scheduled between airports if there is remaining demand, the aircraft is available, has sufficient fuel capacity, can leave within the operating hours of the source airport, and can land within the operating hours of the destination airport
        - Flight numbers will be universally unique and generated by an autoincrementing counter
        - All profit and expeneses will be recorded in a ledger that includes the description, date, time, and amount
        - The ledger will be queriable to support monthly expense report generation for Paris
        - If a database is used, the database must use the official MaraiDB docker container (version 11) and be persistant (mapped to a local volume)
        - The software will run on at least a Macbook Pro with 32 GB of RAM. The OS used is MacOS Sonoma 14.3. The machine utilizes the M1 processor and has a 16 inch (3456 x 2234) monitor. 120Gb of disk space is available. 
        - The build system will such that the entire system can be started up and shut down with `docker compose up --build` and shutdown with `docker compose down`
    - Tasks
        - Containerize application into bridge-connected containers with Docker (assigned to: Anthony, due: 2024-01-18)
        - Map the database to a local volume to ensure persistence (assigned to: Anthony, due: 2024-01-25)
        - Model the MariaDB database using ERD (assigned to: Parker and Zach, due: 2024-01-25)
        - Implement the database model with SQLAlchemy (assigned to: Dylan and Will, due: 2024-01-25)
        - Develop greedy algorithm to generate timetable (assigned to: Anthony and Corey, due: 2024-02-16)
        - Unify greedy algorithm models (assigned to: Everyone, due: 2024-02-25)
        - Diagram classes used by algorithm as UML diagrams (assigned to: Everyone, due: 2024-02-16)
        - Standardize logging structure (assigned to: Anthony, due: 2024-02-25)
    - Implement diagrammed classes (assigned to: Everyone, due: 2024-02-25)
- Simulation Development
    - Outlining and planning (assigned to: Everyone, due: 2024-02-29)
    - Development the simulation (assigned to: Everyone, due: 2024-02-29)
    - Assure the simulation meets client requirements (assigned to: Everyone, due: 2024-04-04)
    - Review project requirements and project status with client (assigned to: Everyone, due: 2024-04-11)
    - Implement feedback (assigned to: Everyone, due: 2024-04-18)
- Turn in complete project to client

## 2.2 External Interface Requirements
There are no external interface requirements because there are no external systems.

## 2.3 Deployment Requirements
All deliverables must be operating-system independent for systems with a 64-bit CPU with at least 8 GB of RAM.
The simulation will be provided as a two-part app-and-database system. Each part of the application -- 
the app and the database -- will be self-contained and connected to an internal bridge container network. 

## 2.4 Database Requirements
- If used, the database must be MariaDB
- The database must be mapped to a local volume to achieve persistence
- The database must be in 3.5 normal form
- The database must support CRUD operations from remote applications

# 3. Non-functional Requirements

## 3.1 Reliability Requirements
- All deployable software components (e.g containers) must have a healthcheck that is checked at least once per minute
- All deployable software components must automatically restart when failure is detected
- All deployable software components must be fully recovered within 5 minutes of detecting failure
- All errors must clearly indicate the cause and location of the error

## 3.2 Security Requirements
- The project may not include any external software projects nor packages that have known vulnerabilities.
- Simulation data is considered company confidential and must remain local; online transmission requires encryption.
- The docker containers be isolated over the network, using an internal bridge network and not exposing any ports

## 3.3 Scalability Requirements
- The simulation should be scalable such that it can simulate profits for any percent market share or change in airports, aircraft, or other simulation components; at a minimum, the simulation must be scalable from a 2% to 5% market share.

## 3.4 Maintainability Requirements
- All Python code must comply with Pep 8, the official Python style guide
- All code files must be prefaced with the name of the development team, the members of the development team, the date
the file was created, the date the file was last updated, a summary of the purpose of the file, and all preconditions and
postconditions
- All Python modules, functions, and classes (i.e. major structural components) must have Python docstrings that
describe their general function, precondition(s), and postcondition(s)
- All code should be modular, connected over boundaries through well-typed and well-defined contracts to promote agility
and testability
- Codebase must be stored remotely on GitHub and managed with the Git version control system
- All packages must use LTS releases if available

## 3.5 Standardization Requirements
- All units should be scientific units
- Time should be stored in UTC in ISO 8601-compliant formats

# 4. Deliverables
The following subsections will all be delivered to the client. 

## 4.1 Data 
A suite of .csv data files that are used by the scripts. The following list details the name of the file and its contents.
1. `aircraft` -- aircraft name, passenger capacity, max speed (in km/h), max fuel (gallons), max range (km), and miles per galon.
2. `airports` -- rank (based on most popular), airport name, IATA code, city, state, metropolitan area, metropolitan population, latitude, longitude.
3. `flight_fuel_capacity` -- source airport, destination airport, fuel for Boeing 737-600 (gallons), fuel for Boeing 767-800 (gallons), fuel for Airbus A200-100 (gallons), fuel for Airbus A220-300 (gallons).
4. `flight_master_record` -- source airport, destination airport, distance (weighted km), fuel, number of passengers, aircraft type, expected time, ticket cost, net profit. This is a merge of tmp other scripts.

## 4.2 Scripts
A suite of Python scripts that helped us create, edit, or merge data files. The following list details the name of the script and what it does. All scripts create a .csv data file.
1. `flight_combine` -- creates an aggregated list of: source airport, destination airport, distance, number of passengers.
2. `flight_demand` -- creates a list of flights between each airport and the number of passengers (based on 0.5% of the source airport's metropolitan population) that want to take that flight (for a 2% market share) each day.
3. `flight_fuel_capacity` -- creates a list of flights between each airport and the amount of fuel required for it.
4. `flight_master_record` -- creates an aggregated list of: source airport, destination airport, distance, fuel required, number of passengers, profit.
5. `flight_profit_or_loss` -- creates a list of all possible flight combinations between the 4 planes and over 800 routes. Note: this script creates two .csv files: one for profitable flights and one for unprofitable flights. This script is purely a monetary calculation, and does not account for max fuel capacity, refuel, etc. It only accounts for a generic takeoff and landing fee, and gas price.
6. `flight_profit_per_hour` -- identical to `flight_profit_or_loss`, but determines the profit or loss by the hour.
7. `flight_times` -- creates a list of the estimated flight times between pairs of airports.
8. `flight_weighted_distances` -- creates a list of the weighted distances between pairs of airports. 
9. `overlapping_airports` -- creates a filtered mapping of metropolitan areas to airports where the airports share the same metropolitan area.
10. `pipline.ps1` -- powershell script to run the following scripts in order: `flight_weighted_distances`, `flight_demand`, `flight_fuel_capacity`, `flight_combine`, `flight_profit_or_loss`.

## 4.3 Models
A suite of Python classes that serve as the fundamental objects. All are Python scripts. The following list details the name of the module and what it contains.
1. `aircraft`:
    - the baseline aircraft class containing aircraft name, model type, status, location, tail number, passenger capacity, cruise speed, fuel level, feul capacity, fuel efficiency, max range, and a wait timer for its status.
    - an enumerated aircraft type class for determining the model aircraft.
    - an enumerated aircraft status class for determing what the aircraft is currently doing.
    - an aircraft factory class (for determining the next tail number and initialize an aircraft) that contains the following functions:
        - `__next_tail_number` -- calculates the plane's tail number.
        - `create_aircraft` -- creates an aircraft object and initializes it with appropriate values.
    - a dictionary of wait timers.
2. `airport`:
    - the baseline airport class containing the airport name, IATA code, city, state, metropolitan population, if the airport is a hub, available gates, latitude, longitude, gas price, takeoff fee, landing fee, and a tarmac queue.
    - an enumerated airport type class for determining if the airport is a hub or not.
3. `flight`:
    - the baseline flight class containing the flight number, scheduled time, aircraft type, flight path (route), and number of passengers.
4. `passenger`:
    - the baseline passenger class containing the source airport of the passenger, location of the passenger, the passenger's destination, number of flights taken, and a unique passenger ID.
    - `expected_departure_time` -- return the passenger's expected departure time.
    - `actual_departure_time` -- return the passenger's actual departure time.
    - `expected_arrival_time` -- return the passenger's expected arrival time.
    - `actual_arrival_time` -- return the passenger's actual arrival time.
5. `route`:
    - the baseline route class containing the type of aircraft flying said route, the source airport, destination airport, flight path distance, daily passengers, estimated flight time, and fuel requirement.
The following modules are helper or main modules.
6. `reference_wrapper` -- class used to pass primitive types by reference in Python.
7. `processors` -- defines several functions in a function pipeline that transforms a log event.
8. `simulation` -- tmp class that contains details about the simulation.
9. `constants` -- holds all constant values used.
10. `main` -- entry point to the program, and takes care of all pre-program initialization before starting.

## 4.4 Documentation
These documents detail the thought process as well as specifics about the execution. As stated before, all documentation follows the Markdown format.
1. `algorithm` -- contains definitions of phrases used, progam input and output, aircraft statuses, ledger entries, and pseudocode for the main algorithm.
2. `docker` -- notes on how to use the docker, with links to official docker documentation.
3. `logging` -- details on the usage and implementation of logging information.
4. `requirements` -- software requirements specification (this document).
5. `testing` -- details types of testing, and the method of testing.
The following directories contain multiple documents about their topics.
1. `diagrams` -- contains outlines of modules and an Entity Relational Diagram (ERD) of the database.
2. `meeting minutes` -- notes about what the group discussed in group meetings.
3. `process` -- a rough introduction to the process, if one were to re-create this project.
4. `standards` -- project specifications for code, documentation, and the general project. 
5. `timeline` -- a rough timeline of production.

## 4.5 Database
The client will receive a database that contains tmp

# 5. Unattempted Functionality
n/a.

# 6. Assurance

## 6.1 Client Feedback
The development team must meet with the client at least once per week to update the client on their progress and 
present their development plans for the following week for approval. The presentation should include the team' s
understanding of the functional and non-functional requirements to be planned or implemented that week. By the end
of the meeting with the client, the development team must have a clear requirements specification.

## 6.2 Software Testing
All software should be rigorously tested to ensure the developed software complies with client requirements. Application
code should be tested with PyTest for a minimum of 50% code coverage. These tests must include unit, integration, and 
system tests. Software tests will be integrated into the development workflow to ensure any commit does not inadvertently
break previous code.

# 7. Appendix

## 7.1 Glossary
| Term | Definition |
| ---- | ---------- |
| Client | Comfort Airlines, the contracting company |
| Company confidential | Proprietary; owned by Comfort Airlines |
| Timetable | A standard schedule as defined by the IATA |

## 7.2 Revision History
| Date | Added | Updated | Removed |
| ---- | ----- | ------- | ------- |
| 2024-02-15 | SRS 5 major sections and major section content | nil | nil |
| 2024-02-21 | Added more description functional requirements | nil | nil |
| 2024-03-19 | Added Deliverables and Unattempted Functionality sections | nil | nil |