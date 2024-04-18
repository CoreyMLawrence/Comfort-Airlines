from __future__ import annotations
from typing import TYPE_CHECKING, Union
import random
import math

from models.aircraft import Aircraft, AircraftStatus

if TYPE_CHECKING:
    from models.flight import Flight
    from models.route import Route

'''
If were to be implemented: 
 - need a minutes_delayed attribute somewhere (plane or route); below uses a placeholder minutes_delayed tied to the aircraft
 - update actual departure/landing times to be different that expected
 - doublecheck math for #3 Im sure Corey/whoever did flight_weighted_distance or time has a better idea than me
 - not sure if to make status in maintence or in maintnence quee, or if we have a tag for needs maintenence, all for #5
 - needs to be able to "cancel" a flight for #6
 - needs a place to call the functions

    match get_book(&book_name) {
        Some(book) => 
    }
'''

# Delay 1: 25% of all flights encounter bad weather and the flight time is extended for a random amount of time between 1 minute and 15% of the flight time.
def delay_1(flight: Flight) -> Union[None,int]:
    DELAY_CHANCE = 0.25
    
    if random.random() < DELAY_CHANCE:
        delay = random.randint(1, math.floor(0.15 * flight.route.expected_time))

        flight.aircraft.status = AircraftStatus.DELAYED
        flight.aircraft.wait_timer = delay

# Delay 2: 20% of all flights originating above 40° N are delayed on the ground (not at the gate) due to icing for a random amount of time between 10 minutes and 45 minutes.
def delay_2(flight: Flight):
    if flight.aircraft.location.latitude > 40:  # Flights originating above 40° N
        if random.random() < 0.20:  # 20% chance of delay
            delay = random.randint(10, 45)
            
            flight.aircraft.status = AircraftStatus.DELAYED
            flight.aircraft.wait_timer = delay

# Delay 3: There is a strong jet stream and flights travelling due East have flight times extended by 12%, flights travelling due West have flights shortened by 12%. All other flights have flight times impacted accordingly based on the initial heading of the flight.
def delay_3(flight: Flight):
    def calculate_direction_percentage(lat1, lon1, lat2, lon2):
        # Convert latitude and longitude from degrees to radians
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        # Calculate change in coordinates
        dlon = lon2 - lon1

        # Calculate bearing (angle)
        x = math.sin(dlon) * math.cos(lat2)
        y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
        bearing = math.atan2(x, y)

        # Convert bearing to degrees
        bearing = math.degrees(bearing)

        # Normalize bearing to be within 0 to 360
        bearing = (bearing + 360) % 360

        # Calculate east/west percentages
        if bearing < 180:
            east_percent = bearing / 180 * 100
            west_percent = 100 - east_percent
        else:
            west_percent = (bearing - 180) / 180 * 100
            east_percent = 100 - west_percent

        # Scale percentages to the range [0, 12]
        east_percent = east_percent / 100 * 12
        west_percent = west_percent / 100 * 12

        return east_percent, west_percent
    east, west = calculate_direction_percentage(
                    flight.route.source_airport.latitude, flight.route.source_airport.longitude, 
                    flight.route.destination_airport.latitude, flight.route.destination_airport.longitude
                )
    
    if east > west:
        delay = flight.route.expected_arrival_time * east
        
        flight.aircraft.status = AircraftStatus.DELAYED
        flight.aircraft.wait_timer = delay
    else:
        delay = flight.route.expected_arrival_time * -west
    


# Delay 4: 5% of flights are delayed at the gate by a random amount of time ranging from 5 minutes to 90 minutes.
def delay_4(flight: Flight):
    if random.random() < 0.05:  # 5% chance of delay
        delay = random.randint(5, 90)

        flight.aircraft.status = AircraftStatus.DELAYED
        flight.aircraft.wait_timer = delay

# Delay 5: You suffer an aircraft failure at one of the major Comfort Airline hubs. The aircraft is taken out of commission for the entire day. The aircraft is towed away from the gate for unscheduled maintenance.
def delay_5(flight: Flight):
    if flight.aircraft.location.is_hub():  # Check if the airport is a hub
        flight.aircraft.set_status(AircraftStatus.IN_MAINTENANCE)
        
# Delay 6: 8% of all flights originating west of 103° W are cancelled. Passengers must be put of other flights in order to reach their destination.
def delay_6(flight):
    if flight.aircraft.location.longitude >= 103 and random.random() < 0.08: #if west of 103 and 8% chance
        #flight cancelled
        pass
        

DAILY_DELAY = [
    None,
    None,
    delay_1,
    None,
    delay_2,
    None,
    delay_3,
    None,
    delay_4,
    None,
    delay_5,
    None,
    delay_6,
    None
]