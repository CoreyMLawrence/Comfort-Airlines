# Working Definitions
- "available aircraft": an aircraft that is not in flight or undergoing maintenance
- "in flight": in the air, waiting on the tarmac, or at a gate preparing to arrive or leave
- "needs main

# External Data
- flights.csv
- aircraft_specs.csv
- airports.csv

# Algorithm

## ROUTINE: Main()

### Steps
- Read flight data from `flights.csv`
- Read aircraft data from `aircraft_specs.csv`
- Read airport data from `airports.csv`
- Sort flights by profit per hour
- Sort aircraft from passenger capacity
- Set starting airport for each aircraft based on `FIXME`
- Until 2 weeks time in minutes has passed:
    - For each aircraft:
        - If the aircraft is available
            - If the 