# Comfort Airlines
Summary of the contents of this project. All content and code is copyrighted by Comfort Airlines, 2024. Note that `archive` files are for internal development purposes only and should not be 
considered a part of the project.

# Automatically Running the Project
The process of generating the simulation input data with the script pipeline,
installing project dependencies, running the simulation, and loading the GUI
are all automated by the script `run.ps1` in the `github` directory.
1. Change to the `github` directory
2. As adminstrator, bypass the powershell remote execution policy with `Set-ExecutionPolicy Bypass`
3. Run the main script `powershell ./run.ps1`

# Manually Running the Project
If for some reason the automatic Powershell script fails, you can also manually run the program.
First, change to the `github` subdirectory. Then, install all project dependencies using `pip3 install -r requirements.txt`. Then, run the project with `python3 src/main.py`. 
If you do not have Python 3.10+ installed, you will need to install it from the [Official Python Downloads](https://www.python.org/downloads/) page.
After the program finishes, there will be 5 reports generated in the `reports` folder. See the table below for contents

|     Report     |                           Contents                             |
| -------------- | -------------------------------------------------------------- |
| aircrafts.csv  | a list of all flights made by each aircraft, including aircraft tail number, flight number, source airport, destination airport, departure time, arrival time, number of passengers |
| airports.csv   | a list of all flights that arrived or departed at each airport, including the type (arrival/departure),airport,arrival/departure time,aircraft flight number,number of passengers,aircraft tail number |
| flights.csv    | a 2 week timetable. includes each flight's flight number,source airport,destination airport,number of passengers,scheduled departure time,scheduled arrival time,actual departure time,actual arrival time,aircraft tail number |
| ledger.csv     | a list of all profits and expenses for the timetable including the item,net profit,time,location |
| passengers.csv | a list of all passengers ordered by actual arrival time, including the passenger uuid, location,source airport,destination airport,expected departure time,expected arrival time,actual departure time,actual arrival time,flights taken |

# Project Contents Overview

| File / Folder    | Description |
| ---------------- | ----------- |
| data             | contains static data related to project, such a airport names, locations, and coordinates              |
| db               | obsolete. contains database volume used by docker infrastructure                                       |
| docs             | contains project and module documentation, including coding conventions and standards                  |
| scripts          | contains one-time scripts, mostly for data analysis. these are not a part of the main application      |
| src              | contains the source code for the project, written in Python 3.10. install all requirements first       |
| tests            | contains unit, integration, and system tests that use the Python pytest testing framwork		        |
| .dockerignore    | contains a list of files for docker to ignore when copying application to the application container    |
| .gitignore       | contains a list of files for Git to ignore (e.g when pushing or pulling code)                          |
| compose.yaml     | contains configurations for docker services (application and database containers)                      |
| Dockerfile       | contains docker commands for initializing the application container                                    |
| README.md        | contains a list of descriptions of all major files and folder                                          |
| requirements.txt | contains all the packages and  their versions. install locally with `pip3 install -r requirements.txt` |
