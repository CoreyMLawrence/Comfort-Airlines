# Timetable Algorithm

## Variables
CONSTANT VARIABLE MINUTES_PER_HOUR = 60 minutes
CONSTANT VARIABLE HOURS_PER_WEEK = 168 hours
CONSTANT VARIABLE SIMULATION_DURATION = 2 hours * $HOURS_PER_WEEK * $MINUTES_PER_HOUR
CONSTANT VARIABLE MAXIMUM_FLIGHT_HOURS = 200 hours
CONSTANT VARIABLE MAINTENANCE_DURATION = 36 hours * $MINUTES_PER_HOUR

CONSTANT VARIABLE OPERATING_HOURS_START = 5 AM [exclusive]
CONSTANT VARIABLE OPERATING_HOURS_END = 1 AM [exclusive]

VARIABLE time = 0 minutes

## Working Definitions
DEFINE "available flight" as "a flight with matching aircraft type, remaining daily demand, departs within operating hours
        of source airport, and lands within operating hours of destination airport"

DEFINE "most profitable flight" as "the flight from the current source airport to any destination airport with the 
        highest profit per hour"

DEFINE "available aircraft" as "an aircraft that is not in maintenance nor in flight (in the air or waiting a gate)"

DEFINE "available gate" as "a gate that is not occupied by an aircraft"

DEFINE "tarmac" as "a queue of aircraft waiting on the runway for a gate"

DEFINE "hub" as "airport destignated as central location with 11 gates; one of {"O'Hare", "Denver Intl.", 
       "Dallas Fort Worth", "Hartsfield-Jackson Atlandta Intl."}

## Algorithm

### Routine MAIN
ROUTINE MAIN
{
    CONDITION_IF(time is greater than $SIMULATION_DURATION)
    {
        LOOP (for each aircraft)
        {
            CONDITION_IF(aircraft is available)
            {
                CONDITION_IF(aircraft.flight_hours is greater than $MAXIMUM_FLIGHT_HOURS)
                {
                    - schedule most profitable flight to hub with shortest wait (ideally open, otherwise shorted queue)
                    - decrease daily demand by minimum of aircraft capacity and remaining daily demand
                    - increase flight hours of aircraft by flight duration
                    - update plane location from source airport to destination airport
                    - reserve maintenance spot for aircraft at airport performing maintenance
                    - mark aircraft in use for flight duration + maintenance time (36 hours)
                    
                    CONDITION_IF(any gate available at destination airport)
                    {
                        - reserve 
                    }
                }
                CONDITION_ELSE
                {
                    - schedule aircraft for most profitable flight from current source airport to destination airport
                    - decrease daily demand by minimum of aircraft capacity and remaining daily demand
                    - increase flight hours of aircraft by flight duration
                    - update plane location from source airport to destination airport
                    - mark aircraft in use for flight duration
                }
            }
        }
        
        increment time by one minute
    }

    serialize timetable as CSV
}

### Routine SCHEDULE
SUBROUTINE SCHEDULE(aircraft = [type: class Aircraft], source_airport = [type: class Airport], destination_airport = [type: class Airport], )
{
    
}