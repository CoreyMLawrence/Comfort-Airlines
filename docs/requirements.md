# Software Requirements Specification (SRS)
This software requirements specification completely defines the aircraft simulation software project contracted by 
Comfort Airlines on 2024-01-07. All project requirements are defined within this source-of-truth specification document.

# 0. Table of Contents
The table of contents provide quick-access to the major sections of the document.

0. [Table of Contents](#0-table-of-contents)
1. [Introduction](#1-introduction)
2. [Functional Requirements](#2-functional-requirements)
3. [Non-functional Requirements](#3-non-functional-requirements)
4. [Assurance](#4-assurance)
5. [Appendix](#5-appendix)

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
        - Collect all the information needed to model an aircraft, including the name, passenger capacity, cruise speed, fuel capacity, fuel efficiency, and maximum range.
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

# 4. Assurance

## 4.1 Client Feedback
The development team must meet with the client at least once per week to update the client on their progress and 
present their development plans for the following week for approval. The presentation should include the team' s
understanding of the functional and non-functional requirements to be planned or implemented that week. By the end
of the meeting with the client, the development team must have a clear requirements specification.

## 4.2 Software Testing
All software should be rigorously tested to ensure the developed software complies with client requirements. Application
code should be tested with PyTest for a minimum of 50% code coverage. These tests must include unit, integration, and 
system tests. Software tests will be integrated into the development workflow to ensure any commit does not inadvertently
break previous code.

# 5. Appendix

## 5.1 Glossary
| Term | Definition |
| ---- | ---------- |
| Client | Comfort Airlines, the contracting company |
| Company confidential | Proprietary; owned by Comfort Airlines |
| Timetable | A standard schedule as defined by the IATA |

## 5.2 Revision History
| Date | Added | Updated | Removed |
| ---- | ----- | ------- | ------- |
| 2024-02-15 | SRS 5 major sections and major section content | nil | nil |
| 2024-02-21 | Added more description functional requirements | nil | nil |