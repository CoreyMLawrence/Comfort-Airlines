# Working Definitions
- "available aircraft": an aircraft that is not in flight or undergoing maintenance
- "aircraft needs maintenance": an aircraft with 200+ flight hours since last maintenance
- "available gate": a gate that is not currently being used by an aircraft nor scheduled to be used by an aircraft
- "in flight": in the air, waiting on the tarmac, or at a gate preparing to arrive or leave

# External Data
- flights.csv
- aircraft.csv
- airports.csv

# Algorithm

## ROUTINE: Main()
- BEGIN
- Read flight data from `flights.csv`
- Read aircraft data from `aircraft.csv`
- Read airport data from `airports.csv`
- Sort flights by profit per hour
- Sort aircraft from passenger capacity
- Set starting airport for each aircraft based on manually predetermined starting points
- Until 2 weeks time in minutes has passed:
    - For each aircraft:
        - If the aircraft is available:
            - If the aircraft needs maintenance:
                - `[Subroutine::Schedule]` Schedule the aircraft for the flight to the hub with the shortest wait time (if equal wait times, maximize profit)
            - Else
                - `[Subroutine::Schedule]` Schedule the aircraft for the most profitable flight
        - Else
            - If flight time for aircraft has elapsed:
                - `[Subroutine::Flight::Arrive]` Land the aircraft
            - If maintenance time (36hr) have passed:
                - Mark the aircraft as available again
                - Reset flight hours to 0
            - If waiting to depart: FOO

        - For each airport:
            - Assign as many aircraft as possible from the queue to a gate
            - Wait 15 minutes to deboard plane
            - Mark the aircraft as available
    - Increment the timer by 1 minute
- Serialize scheduler records as `simulation/timetable.csv`
- Serialize passengers as `simulation/passenger.csv`
- Serialize aircraft as `simulation/aircraft.csv`
- Serialize ledger as `simulation/leger.csv`
- STOP


## ROUTINE: Schedule(aircraft, flight)
- Mark the aircraft as unavailable
- Decrease the demand for the flight by the minimum of the passenger capacity of the aircraft and the remaining demand
- Append entry to scheduler including all flight information and expected departure and arrival
- `[Subroutine::Flight::Depart]` Begin preparations for departure and depart

## ROUTINE: Flight::Depart(aircraft, flight, ledger)
- Wait for 25 minutes for cleaning, boarding, et cetera
- `[Subroutine::Ledger::Append]` Add takeoff fee to ledger
- If the aircraft needs to refuel:
    - Refuel the aircraft with the required fuel for the trip + 33% (or just the whole tank? to be discussed.)
    - `[Subroutine::Ledger::Append]` Add fuel costs to ledger
    - Wait 10 minutes to departure wait time

## ROUTINE: Flight::Arrive(aircraft, flight, ledger)
- `[Subroutine::Ledger::Append]` Add landing fee to ledger
- Append the aircraft to the tarmac queue

## ROUTINE: Ledger::Append(description: enum LedgerEntryType, cost: decimal)
- Append the transaction to the ledger (type: `LedgerEntry`), including its description, the net cost, the current date, time,
and location