# TimeTable
It has been determined that the problem space for generating a timetable with 31 airports is too large to calculate
all possible timetables using a backtracking approach. So, a heuristic approach is necessary. Based on current research,
a genetic algorithm is suitable for timetable generation.


# Task Description
### Summary
Create a timetable that complies with the constaints and specifications below

### Constraints
- The timetable should be maintained in a database
- Include at least the arrival and departure times of each flight, the source and destination airports, the passenger capacity on that flight, the ticket cost, and the unique flight number
- Each flight must have a unique flight number (e.g. `CA1234`)
- Each plane should have a unique [tail number](https://blueskypit.com/2022/11/license-plates-for-planes-how-to-understand-tail-numbers/#:~:text=Aircraft%20registration%20numbers%2C%20or%20tail,license%20plate%20on%20a%20car)
- A printed version of the timetable must also be available
- An interface for a passenger to look for a flight from airport A to airport B must also be provided (project part 2)

### Specifications
- Passengers can fly from any airport to any other airport
- Airplanes may start at any airport
- Account for flights that are non-stop or have multiple stops between the source and destination airports
- Planes must start the next day at the same airport they ended at the previous day

### Examples of Airport Timetables
- [FlightAware](https://www.flightaware.com/live/airport/KORD)
- [FlightRader24](https://www.flightradar24.com/data/airports/pnq)
- [Hong Kong Airport](https://www.hongkongairport.com/en/flights/departures/passenger.page)
- [JFK Airport](https://www.airport-jfk.com/departures.php)

### Genetic Algorithms
- [The Knapsack Problem](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1228/section/section4/Knapsack%20Problem%20(Optional%20Section%20Slides).pdf)
- [Genetic Algorithms](https://en.wikipedia.org/wiki/Genetic_algorithm)
- [Monte Carlo Method](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- [Mastering Python Genetic Algorithms](https://www.pythonpool.com/python-genetic-algorithm/)

### Genetic Algorithms Libraries
- [PyGAD: open-source Python 3 library for building genetic algorithms](https://pypi.org/project/pygad/)
- [Pandas: provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive](https://pypi.org/project/pandas/)

### Automatic Timetable Generation using Genetic Algorithms
- [Automatic Timetable Generation using Genetic Algorithm](https://www.researchgate.net/publication/332154069_ISSN_2249-0868_Foundation_of_Computer_Science_FCS)
- [Automated Timetable Generation using Genetic Algorithm](https://www.ijert.org/research/automated-timetable-generation-using-genetic-algorithm-IJERTV9IS070568.pdf)
- [Automatic Timetable Generator Using Genetic Algorithm](https://www.jetir.org/papers/JETIR2305D85.pdf)
- [Automatic Timetable Generator Using Genetic Algorithm](https://www.jetir.org/papers/JETIR2305B98.pdf)

### Group Questions
Foobar.