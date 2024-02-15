# Working Definitions
- "aircraft needs maintenance": an aircraft with 200+ flight hours since last maintenance
- "available aircraft": an aircraft that is not in flight or undergoing maintenance (implies deboarded and waiting at a gate)
- "available flight": a flight with remaining demand that can be flown by the given aircraft type with sufficient maximum fuel, leaving within the operating hours of the source airport and arriving within the operating hours of the destination airport
- "available gate": a gate that is not currently being used by an aircraft nor scheduled to be used by an aircraft
- "hub": "airport destignated as central location with 11 gates; one of {"O'Hare", "Denver Intl.", "Dallas Fort Worth", "Hartsfield-Jackson Atlandta Intl."}
- "in flight": in the air, waiting on the tarmac, or at a gate preparing to arrive or leave
- "operating hours": 5 AM to 1 AM (exclusive)

# Program Input
- `flights.csv`
- `aircraft.csv`
- `airports.csv`

# Program Output
- `simulation/timetable.csv`
- `simulation/passenger.csv`
- `simulation/aircraft.csv`
- `simulation/ledger.csv`

# Aircraft Status
- Available (no time)
- In Maintenance (2160m)
- Waiting at tarmac (null time)
- Boarding without refueling (25m)
- Boarding with refueling (35m)
- Deboarding (15m)
- In flight (variable)

# Ledger Entries
- Fuel (expense)
- Landing and takeoff fees (expense)
- Aircraft rentals (expense)
- Ticket sales (profit)

# Algorithm

## ROUTINE: Main()

#### 1. Import flight data from CSVs
- Read flight data from `flights.csv`
- Read aircraft data from `aircraft.csv`
- Read airport data from `airports.csv`

#### 2. Pre-simulation Setup
- Sort flights by profit per hour (so each flight scheduled is the most profitable possible)
- Sort aircraft by passenger capacity (so each flight carries as many passengers as possible)
- Set starting airport for each aircraft based on most profitable flight for given aircraft type (non-overlapping, if multiple candidate aircraft, choose largest passenger capacity)

#### 3. Simulation
- Until 2 weeks time in minutes has passed:
    - For each aircraft:
        - If the aircraft is available:
            - If the aircraft needs maintenance:
                - Reserve maintenance spot for aircraft at airport performing maintenance
                - `[Subroutine::Schedule]` Schedule the aircraft for the flight to the hub with the shortest wait time (if equal wait times, maximize profit) that can be made during operating hours (if any)
            - Else
                - `[Subroutine::Schedule]` Schedule the aircraft for the most profitable, available flight that can be made within operating hours (if any)
        - Else
            - If aircraft is in the air and flight wait time has elapsed:
                - `[Subroutine::Flight::Arrive]` Land the aircraft
            - If aircraft is in maintenance and has maintenance wait time (36h or 2160m) has elapsed:
                - Set aircraft status to available
                - Reset flight hours to 0m
                - If there is an available gate
                    - Assign the aircraft to the gate
                - Else
                    - Set the aircraft status to waiting at tarmac
                    - Append the aircraft to the tarmac queue
            - If waiting to depart and departure wait time (25m default, 35m if refueling) has elapsed
                - Set flight status to in flight
            - If waiting to deboard and deboarding time (15m) has elapsed:
                - If aircraft needs maintenance and aircraft is at hub airport:
                    - Set aircraft status to in maintenance (unavailable)
                    - Start timer for maintenance wait time (36h or 2160m)
                    - Deassign the aircraft from current gate
                    - If there are any aircraft waiting on the tarmac:
                        - Assign newly available gate to first aircraft in tarmac
                        - Set first aircraft in tarmac's status to deboarding
                        - Start deboarding timer for first aircraft
                        - Remove first aircraft from tarmac queue
                    - Else
                        - Mark gate as available 
                - Else
                    - Set aircraft status to available

    - Increment the timer by 1 minute

#### 4. Dump simulation results to CSVs
- Serialize scheduler records as `simulation/timetable.csv`
- Serialize passengers as `simulation/passenger.csv`
- Serialize aircraft as `simulation/aircraft.csv`
- Serialize ledger as `simulation/ledger.csv`

## SUBROUTINE: Schedule(aircraft, flight)
- Set aircraft status to scheduled (unavailable)
- Decrease the demand for the flight by the minimum of the passenger capacity of the aircraft and the remaining demand
- Append entry to scheduler including flight number, data of flight, departure airport, destination airport, number of
passengers, scheduled, departure time, scheduled arrival time, aircraft tail number
- `[Subroutine::Flight::Depart]` Begin preparations for departure and depart

## SUBROUTINE: Flight::Depart(aircraft, flight, ledger)
- `[Subroutine::Ledger::Append]` Add takeoff fee to ledger
- Record actual flight departure time in scheduler flight entry
- Increase aircraft flight hours by flight duration
- If the aircraft needs to refuel:
    - Refuel the aircraft with the required fuel for the trip
    - `[Subroutine::Ledger::Append]` Add fuel costs to ledger
    - Start timer for boarding wait time with extra refuel time (35m)
- Else
    - Start timer for boarding wait time without refueling (25m)
- Set plane location to null
- Start timer for flight time (flight-dependent)
- If there are any aircraft waiting on the tarmac:
    - Assign newly available gate to first aircraft in tarmac
    - Set first aircraft in tarmac's status to deboarding
    - Start deboarding timer for first aircraft
    - Remove first aircraft from tarmac queue 

## SUBROUTINE: Flight::Arrive(aircraft, flight, ledger)
- `[Subroutine::Ledger::Append]` Add landing fee to ledger
- Record actual flight arrival time in scheduler flight entry
- Set plane location to destination airport
- Decrease the aircraft fuel amount by fuel used
- If there is any available gate, assign the gate to the aircraft
    - Set aircraft status to deboarding
    - Start timer for deboarding wait time (15m)
- Else
    - Set aircraft status to waiting at tarmac (unavailable)
    - Append the aircraft to the tarmac queue

## SUBROUTINE: Ledger::Append(description: enum LedgerEntryType, cost: decimal)
- Append the transaction to the ledger (type: `LedgerEntry`), including its description, the net cost, the current date, time,
and location