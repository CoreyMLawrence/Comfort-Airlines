# Database
The database is a 6-table Boyce-Codd normal form database diagrammed using [draw.io](https://app.diagrams.net/). If you do
not have the draw.io VSCode extension installed, you can use the online version linked above. The database stores the
following information:

- For each flight, record: flight number, data of flight, departure airport, destination airport, number of passengers, scheduled, departure time, actual departure time, scheduled arrival time, actual arrival time, aircraft tail number.
- For every passenger: source airport, destination airport, flights taken (flight number, source airport, destination airport, scheduled departure time, actual departure time, scheduled arrival time, actual arrival time).
- For each airport: arrival time of each aircraft, flight number as arriving aircraft, number of arriving passengers, departure time of each aircraft, flight number as departing aircraft, number of departing passengers, gate used, aircraft tail number.
- For each aircraft: aircraft tail number, for each flight: date of flight, flight number, departure airport,
destination airport, departure time, arrival time, number of passengers.

# Task Description

### Summary
Using [draw.io](https://app.diagrams.net/) create an [ERD diagram](https://www.databasestar.com/entity-relationship-diagram/) 
of the MariaDB database called `database.drawio` that satisfies the requirements in `Project.pdf`. Put the diagram in the
`diagrams` folder on the Google Drive. The diagram should should be in 
[3.5 normal form](https://en.wikipedia.org/wiki/Boyce%E2%80%93Codd_normal_form) (Boyce-Codd normal form), including 
primary keys for each table, foreign keys for references to other tables, and no data stored redundantly. You will also 
need to choose suitable [MariaDB datatypes](https://mariadb.com/kb/en/data-types/) for all data stored. Remember to use 
the [DECIMAL](https://mariadb.com/kb/en/decimal/) datatype for money.