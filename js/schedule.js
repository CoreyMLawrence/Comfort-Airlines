class ScheduleManager {
  constructor() {
    // Define the structure of the schedule data
    this.schedule = {
      flightNumber: [],
      sourceAirport: [],
      destinationAirport: [],
      sourceCity: [],
      destinationCity: [],
      passengerCount: [],
      scheduledDepartureTime: [],
      scheduledArrivalTime: [],
      actualDepartureTime: [],
      actualArrivalTime: [],
      aircraftTailNumber: [],
      day: [], // Array to store the day of each flight
      date: [], // Array to store the date of each flight
      departureMinutes: [], // Array to store the scheduled departure time in minutes
      aircraft: [],
      gateNumber: [], // Array to store gate numbers
      seatNumber: [], // Array to store seat numbers
      flightTime: [], // Array to store flight times
    };

    // Set the simulation start date (4/22/2024 5:00am)
    this.simulationStartDate = new Date(2024, 3, 22, 5, 0);
    // Initialize the current date to the simulation start date
    this.currentDate = this.simulationStartDate;

    this.lastDestination = ''; // Store the last destination entered by the user
    this.lastSearchResults = []; // Store the last search results
  }

  // Method to parse CSV data and store it
  parseCSVAndStore(csvData) {
    // Check if schedule data already exists in session storage
    const storedSchedule = JSON.parse(sessionStorage.getItem('schedule'));

    // // If schedule data exists, return it without parsing the CSV
    // if (storedSchedule) {
    //   console.log('Using existing schedule data from session storage');
    //   this.schedule = storedSchedule;
    //   return this.schedule;
    // }

    const lines = csvData.split('\n'); // Split CSV data into lines
    const airports = JSON.parse(sessionStorage.getItem('airports')); // Retrieve airport data from session storage
    let currentDay = 1; // Start with day 1
    let previousDepartureTime = -1; // Initialize previous departure time

    // Loop through each line of the CSV data
    for (let i = 1; i < lines.length; i++) {
      const line = lines[i].trim(); // Trim whitespace from the line
      if (line !== '') {
        // Check if the line is not empty
        const values = line.split(','); // Split the line into values using comma as delimiter

        // Check if any value in the row is null
        if (
          values.some(
            (value) => value === 'null' || value === undefined || value === ''
          )
        ) {
          //console.error('Skipping row with null value:', values);
          continue; // Skip this row if any value is null
        }

        // Push data into the schedule object
        this.schedule.flightNumber.push(parseInt(values[0]));
        this.schedule.sourceAirport.push(values[1]);
        this.schedule.destinationAirport.push(values[2]);
        this.schedule.passengerCount.push(parseInt(values[3]));
        this.schedule.scheduledDepartureTime.push(
          this.convertMinutesToTime(parseInt(values[4]))
        );
        // Convert minutes offset to time format
        this.schedule.scheduledArrivalTime.push(
          this.convertMinutesToTime(parseInt(values[5]))
        );
        this.schedule.actualDepartureTime.push(
          this.convertMinutesToTime(parseInt(values[6]))
        );
        console.log('\n\n flight number: ', parseInt(values[0]));
        console.log('departure location: ', values[1]);
        console.log('departure Minutes:', parseInt(values[4]));
        console.log('time:', this.convertMinutesToTime(parseInt(values[6])));

        this.schedule.actualArrivalTime.push(
          this.convertMinutesToTime(parseInt(values[7]))
        );
        this.schedule.aircraftTailNumber.push(values[8]);

        // Calculate flight time and store it
        const departureTime = parseInt(values[6]);
        const arrivalTime = parseInt(values[5]);
        const diff = arrivalTime - departureTime;
        const hours = Math.floor(diff / 60);
        const minutes = diff % 60;
        this.schedule.flightTime.push(`${hours}H:${minutes}M`);

        // Find sourceCity and destinationCity from airports data
        const sourceAirportData = airports.find(
          (airport) => airport.name === values[1].trim()
        );
        const destinationAirportData = airports.find(
          (airport) => airport.name === values[2].trim()
        );

        this.schedule.aircraft.push(values[9]);

        // Add sourceCity and destinationCity to the schedule object
        if (sourceAirportData && destinationAirportData) {
          this.schedule.sourceCity.push(sourceAirportData.city);
          this.schedule.destinationCity.push(destinationAirportData.city);
        } else {
          console.error(
            `Airport not found for flight ${values[0]}: source ${values[1]}, destination ${values[2]}`
          );
        }
        // Function to generate a random gate number within a normal range
        function generateRandomGateNumber() {
          const gatePrefixes = ['A', 'B', 'C', 'D']; // Example gate prefixes
          const gateNumber = Math.floor(Math.random() * 30) + 1; // Random gate number between 1 and 30
          const randomPrefix =
            gatePrefixes[Math.floor(Math.random() * gatePrefixes.length)]; // Random prefix
          return randomPrefix + gateNumber;
        }

        // Function to generate a random seat number within a normal range
        function generateRandomSeatNumber() {
          const seatRows = [];
          for (let i = 1; i <= 32; i++) {
            seatRows.push(String(i));
          }
          const seatLetters = ['A', 'B', 'C', 'D', 'E', 'F'];
          const randomRow =
            seatRows[Math.floor(Math.random() * seatRows.length)]; // Random row
          const randomLetter =
            seatLetters[Math.floor(Math.random() * seatLetters.length)]; // Random letter
          return randomRow + randomLetter;
        }

        // Generate random gate and seat numbers
        this.schedule.gateNumber.push(generateRandomGateNumber());
        this.schedule.seatNumber.push(generateRandomSeatNumber());

        // Calculate flight date based on the current date and day count
        const flightDate = new Date(
          this.currentDate.getTime() + (currentDay - 1) * 86400000
        );
        this.schedule.date.push(
          `${
            flightDate.getMonth() + 1
          }/${flightDate.getDate()}/${flightDate.getFullYear()}`
        );

        // Calculate the change in days based on departure time
        const currentDepartureTime = parseInt(values[4]);

        currentDay = Math.floor(currentDepartureTime / 1440) + 1;
        // Store the current day and scheduled departure time in minutes
        this.schedule.day.push(currentDay);
        this.schedule.departureMinutes.push(currentDepartureTime);
        previousDepartureTime = currentDepartureTime;
      }
    }

    // Store the schedule object in session storage
    sessionStorage.setItem('schedule', JSON.stringify(this.schedule));
    return this.schedule;
  }

  convertMinutesToTime(offset) {
    // Calculations
    var offsetFromStartingDay = offset / 1440;
    var offsetFromCurrentDay =
      offsetFromStartingDay - Math.trunc(offsetFromStartingDay);
    var hoursAndFractionOfHours = 24 * offsetFromCurrentDay;
    var hours =
      Math.trunc(hoursAndFractionOfHours) > 12
        ? Math.trunc(hoursAndFractionOfHours) - 12
        : Math.trunc(hoursAndFractionOfHours);
    var minutes =
      (hoursAndFractionOfHours - Math.trunc(hoursAndFractionOfHours)) * 60;
    var amOrPm = Math.trunc(hoursAndFractionOfHours) > 12 ? 'PM' : 'AM';

    // Format hours
    hours = hours === 0 ? 12 : hours;

    // Output
    return `${hours}:${Math.floor(minutes)
      .toString()
      .padStart(2, '0')}${amOrPm}`;
  }

  // convertMinutesToTime(minutes) {
  //   const minutesInDay = minutes % 1440; // Total minutes in a day (24 * 60)
  //   const hours = Math.floor(minutesInDay / 60);
  //   const mins = minutesInDay % 60;
  //   let ampm = hours >= 12 ? 'pm' : 'am';
  //   let hourFormat = hours === 0 ? 12 : hours > 12 ? hours - 12 : hours;
  //   if (hourFormat === 12) {
  //     ampm = 'pm';
  //   }
  //   return `${hourFormat}:${mins.toString().padStart(2, '0')}${ampm}`;
  // }

  // convertMinutesToTime(minutes) {
  //   const minutesInDay = minutes % 1440; // Total minutes in a day (24 * 60)
  //   const hours = Math.floor(minutesInDay / 60);
  //   const mins = minutesInDay % 60;
  //   let ampm = hours >= 12 ? 'pm' : 'am';
  //   let hourFormat = hours === 0 ? 12 : hours > 12 ? hours - 12 : hours;
  //   if (hourFormat === 12) {
  //     ampm = 'pm';
  //   }
  //   return `${hourFormat}:${mins.toString().padStart(2, '0')}${ampm}`;
  // }

  // Method to generate a random gate number within a normal range
  generateRandomGateNumber() {
    const gatePrefixes = ['A', 'B', 'C', 'D']; // Example gate prefixes
    const gateNumber = Math.floor(Math.random() * 30) + 1; // Random gate number between 1 and 30
    const randomPrefix =
      gatePrefixes[Math.floor(Math.random() * gatePrefixes.length)]; // Random prefix
    return randomPrefix + gateNumber;
  }

  // Method to generate a random seat number within a normal range
  generateRandomSeatNumber() {
    const seatRows = [];
    for (let i = 1; i <= 32; i++) {
      seatRows.push(String(i));
    }
    const seatLetters = ['A', 'B', 'C', 'D', 'E', 'F'];
    const randomRow = seatRows[Math.floor(Math.random() * seatRows.length)]; // Random row
    const randomLetter =
      seatLetters[Math.floor(Math.random() * seatLetters.length)]; // Random letter
    return randomRow + randomLetter;
  }

  // Method to read CSV file
  readFile() {
    return new Promise((resolve, reject) => {
      const xhr = new XMLHttpRequest();
      xhr.onload = function () {
        if (xhr.status === 200) {
          resolve(xhr.responseText);
        } else {
          reject(new Error('Failed to load file'));
        }
      };
      xhr.onerror = function () {
        reject(new Error('Failed to load file'));
      };
      xhr.open('GET', '../github/reports/flights.csv');
      xhr.send();
    });
  }

  // Method to display schedule information
  displayScheduleInfo() {
    const scheduleDiv = document.getElementById('scheduleInfo');
    scheduleDiv.innerHTML = '';
    const table = document.createElement('table');
    table.border = '1';

    // Create table header
    const headerRow = table.insertRow();
    for (const key in this.schedule) {
      const headerCell = document.createElement('th');
      headerCell.textContent = key;
      headerRow.appendChild(headerCell);
    }

    // Create table rows for each flight
    for (let i = 0; i < this.schedule.flightNumber.length; i++) {
      const row = table.insertRow();
      for (const key in this.schedule) {
        const cell = row.insertCell();
        cell.textContent = this.schedule[key][i];
      }
    }

    // Append the table to the schedule div
    scheduleDiv.appendChild(table);
  }

  // Method to display schedule information with selected columns and custom header names
  displaySelectedColumns() {
    // Retrieve airports data from session storage
    const airports = JSON.parse(sessionStorage.getItem('airports'));

    // Function to get city name from airport code
    function getCityName(airportCode, airports) {
      const airport = airports.find((a) => a.name === airportCode);
      return airport ? airport.city : airportCode;
    }

    const scheduleDiv = document.getElementById('scheduleCustomer');
    scheduleDiv.innerHTML = '';
    const table = document.createElement('table');
    table.id = 'scheduleCustomer'; // Add ID to match CSS styling

    // Define the custom header names
    const headerNames = [
      'Flight Number',
      'Starting Location',
      'Destination Location',
      'Scheduled Departure Time',
      'Scheduled Arrival Time',
      'Date',
    ];

    // Create table header with custom header names
    const headerRow = table.createTHead().insertRow();
    headerNames.forEach((name) => {
      const headerCell = document.createElement('th');
      headerCell.textContent = name;
      headerCell.style.fontWeight = 'bold'; // Bold font weight
      headerCell.style.borderBottom = '2px solid purple'; // Purple border bottom
      headerRow.appendChild(headerCell);
    });

    // Create an array of objects to hold the data
    const scheduleData = [];
    for (let i = 0; i < this.schedule.flightNumber.length; i++) {
      const rowData = {
        flightNumber: this.schedule.flightNumber[i],
        sourceAirport: getCityName(this.schedule.sourceAirport[i], airports),
        destinationAirport: getCityName(
          this.schedule.destinationAirport[i],
          airports
        ),
        scheduledDepartureTime: this.schedule.scheduledDepartureTime[i],
        scheduledArrivalTime: this.schedule.scheduledArrivalTime[i],
        date: this.schedule.date[i],
      };
      scheduleData.push(rowData);
    }

    // Sort the scheduleData array first by source airport and then by date
    scheduleData.sort((a, b) => {
      if (a.sourceAirport === b.sourceAirport) {
        return new Date(a.date) - new Date(b.date);
      }
      return a.sourceAirport.localeCompare(b.sourceAirport);
    });

    // Create table rows for each flight
    scheduleData.forEach((row) => {
      const tableRow = table.insertRow();
      // Add data for selected columns
      Object.values(row).forEach((data) => {
        const cell = tableRow.insertCell();
        cell.textContent = data;
        cell.style.border = '1px solid #dddddd'; // Match border style
        cell.style.padding = '8px'; // Match padding
      });
    });

    // Append the table to the schedule div
    scheduleDiv.appendChild(table);
  }

  displaySelectedColumnsFiltered(sourceCity, destinationCity) {
    // Retrieve airports data from session storage
    const airports = JSON.parse(sessionStorage.getItem('airports'));

    // Function to get city name from airport code
    function getCityName(airportCode, airports) {
      const airport = airports.find((a) => a.name === airportCode);
      return airport ? airport.city : airportCode;
    }

    const scheduleDiv = document.getElementById('scheduleCustomer');
    scheduleDiv.innerHTML = ''; // Clear the content of the div

    const table = document.createElement('table');
    table.id = 'scheduleCustomer';

    // Define the custom header names
    const headerNames = [
      'Flight Number',
      'Starting Location',
      'Destination Location',
      'Scheduled Departure Time',
      'Scheduled Arrival Time',
      'Date',
    ];

    // Create table header with custom header names
    const headerRow = table.createTHead().insertRow();
    headerNames.forEach((name) => {
      const headerCell = document.createElement('th');
      headerCell.textContent = name;
      headerCell.style.fontWeight = 'bold'; // Bold font weight
      headerCell.style.borderBottom = '2px solid purple'; // Purple border bottom
      headerRow.appendChild(headerCell);
    });

    // Create an array of objects to hold the data
    const scheduleData = [];
    for (let i = 0; i < this.schedule.flightNumber.length; i++) {
      const rowData = {
        flightNumber: this.schedule.flightNumber[i],
        sourceAirport: getCityName(this.schedule.sourceAirport[i], airports),
        destinationAirport: getCityName(
          this.schedule.destinationAirport[i],
          airports
        ),
        scheduledDepartureTime: this.schedule.scheduledDepartureTime[i],
        scheduledArrivalTime: this.schedule.scheduledArrivalTime[i],
        date: this.schedule.date[i],
      };
      scheduleData.push(rowData);
    }

    // Filter the scheduleData array based on selected source and destination cities
    const filteredData = scheduleData.filter((row) => {
      return (
        (!sourceCity || row.sourceAirport === sourceCity) &&
        (!destinationCity || row.destinationAirport === destinationCity)
      );
    });

    // Sort the filteredData array first by source airport and then by date
    filteredData.sort((a, b) => {
      if (a.sourceAirport === b.sourceAirport) {
        return new Date(a.date) - new Date(b.date);
      }
      return a.sourceAirport.localeCompare(b.sourceAirport);
    });

    // Create table rows for each flight
    filteredData.forEach((row) => {
      const tableRow = table.insertRow();
      // Add data for selected columns
      Object.values(row).forEach((data) => {
        const cell = tableRow.insertCell();
        cell.textContent = data;
        cell.style.border = '1px solid #dddddd';
        cell.style.padding = '8px';
      });
    });

    scheduleDiv.appendChild(table);
  }

  // Method to initialize the schedule manager
  init() {
    document.addEventListener('DOMContentLoaded', () => {
      this.readFile()
        .then((csvData) => this.parseCSVAndStore(csvData))
        .then((schedule) => {
          console.log(
            'Schedule data parsed and stored successfully:',
            schedule
          );
          this.displaySelectedColumns(); // Display the selected columns
        })
        .catch((error) => console.error('Error:', error));
    });
  }
}

// Create an instance of ScheduleManager and initialize it
const scheduleManager = new ScheduleManager();
scheduleManager.init();

function filterCities(inputText) {
  const destinationList = document.getElementById('destinationList');
  destinationList.innerHTML = ''; // Clear previous results

  // Get the starting location from session storage
  const startingLocation = sessionStorage.getItem('startingLocation');

  // Create an array to hold filtered cities
  const filteredCities = [];

  // Filter cities based on input text and starting location
  scheduleManager.schedule.destinationCity.forEach((city, index) => {
    if (
      city.toLowerCase().includes(inputText.toLowerCase()) &&
      scheduleManager.schedule.sourceCity[index].toLowerCase() ===
        startingLocation.toLowerCase()
    ) {
      // Push the city details into the filteredCities array
      filteredCities.push({
        city: city,
        sourceCity: scheduleManager.schedule.sourceCity[index],
        departureTime: scheduleManager.schedule.scheduledDepartureTime[index],
        arrivalTime: scheduleManager.schedule.scheduledArrivalTime[index],
        date: scheduleManager.schedule.date[index],
        flightNumber: scheduleManager.schedule.flightNumber[index],
      });
    }
  });

  // Sort filteredCities by destination location, then by date
  filteredCities.sort((a, b) => {
    if (a.city < b.city) return -1;
    if (a.city > b.city) return 1;
    // If the cities are the same, compare by date
    return new Date(a.date) - new Date(b.date);
  });

  // Display sorted cities in the dropdown
  filteredCities.forEach((city) => {
    const li = document.createElement('li');
    li.textContent = `${city.city} - From: ${city.sourceCity}, Departure: ${city.departureTime}, Arrival: ${city.arrivalTime}, Date: ${city.date}`;
    li.onclick = function () {
      // Store the selected flight number in session storage
      sessionStorage.setItem('selectedFlight', city.flightNumber);
      console.log(
        'Selected Flight = ',
        sessionStorage.getItem('selectedFlight')
      );
      // Update the input field value with the selected city
      document.getElementById('destinationInput').value = city.city;
      // Close the dropdown
      destinationList.classList.remove('show');
    };
    destinationList.appendChild(li);
  });

  // Show the dropdown
  destinationList.classList.add('show');
}

// Event listener for input field
document
  .getElementById('destinationInput')
  .addEventListener('input', function (event) {
    const inputText = event.target.value;
    filterCities(inputText);
  });

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches('#destinationInput')) {
    const dropdowns = document.getElementsByClassName('dropdown-content');
    for (const dropdown of dropdowns) {
      if (dropdown.classList.contains('show')) {
        dropdown.classList.remove('show');
      }
    }
    updateBoardingPass();
    updateTicketCost();
  }
};

function updateBoardingPass() {
  // Retrieve the index position of the selected flight from session storage
  const selectedIndex = scheduleManager.schedule.flightNumber.indexOf(
    parseInt(sessionStorage.getItem('selectedFlight'))
  );
  console.log('selectedFlight = ', sessionStorage.getItem('selectedFlight'));
  console.log('selectedIndex = ', selectedIndex);

  // Retrieve the username from session storage
  const username = String(sessionStorage.getItem('username'))
    .slice(0, 15)
    .toUpperCase();

  // Function to format the date
  function getFormattedDate(dateString) {
    const months = [
      'JAN',
      'FEB',
      'MAR',
      'APR',
      'MAY',
      'JUN',
      'JUL',
      'AUG',
      'SEP',
      'OCT',
      'NOV',
      'DEC',
    ];

    const date = new Date(dateString);
    const day = date.getDate();
    const monthAbbreviation = months[date.getMonth()];

    return `${day}${monthAbbreviation.toUpperCase()}`;
  }

  // Check if selectedIndex is valid and within the range of flights
  if (
    selectedIndex !== null &&
    selectedIndex >= 0 &&
    selectedIndex < scheduleManager.schedule.flightNumber.length
  ) {
    // Get the flight information using the selectedIndex
    const index = parseInt(selectedIndex);
    const sourceCity = String(
      scheduleManager.schedule.sourceCity[index] || 'Unknown'
    )
      .slice(0, 15)
      .toUpperCase();
    const destinationCity = String(
      scheduleManager.schedule.destinationCity[index] || 'Unknown'
    )
      .slice(0, 15)
      .toUpperCase();
    sessionStorage.setItem(
      'destinationLocation',
      scheduleManager.schedule.destinationCity[index]
    );
    console.log(
      'destinationLocation: ',
      sessionStorage.getItem('destinationLocation')
    );
    const gateNumber = String(
      scheduleManager.schedule.gateNumber[index] || 'Unknown'
    );
    sessionStorage.setItem('gateNumber', gateNumber);
    const boardingTime = String(
      scheduleManager.schedule.scheduledDepartureTime[index] || 'Unknown'
    ).toUpperCase();
    sessionStorage.setItem('boardingTime', boardingTime);

    const flightNumber = String(
      scheduleManager.schedule.flightNumber[index] || 'Unknown'
    ).toUpperCase();
    sessionStorage.setItem('flightNumber', flightNumber);

    const flightDate = getFormattedDate(
      scheduleManager.schedule.date[index] || 'Unknown'
    );
    sessionStorage.setItem('flightDate', flightDate);

    const seatNumber = String(
      scheduleManager.schedule.seatNumber[index] || 'Unknown'
    );
    sessionStorage.setItem('seatNumber', seatNumber);

    sessionStorage.setItem(
      'flightTime',
      scheduleManager.schedule.flightTime[index] || 'Unknown'
    );
    sessionStorage.setItem(
      'departureTime',
      scheduleManager.schedule.scheduledDepartureTime[index] || 'Unknown'
    );
    sessionStorage.setItem(
      'arrivalTime',
      scheduleManager.schedule.scheduledArrivalTime[index] || 'Unknown'
    );
    sessionStorage.setItem(
      'sourceAirport',
      scheduleManager.schedule.sourceAirport[index] || 'Unknown'
    );
    sessionStorage.setItem(
      'destinationAirport',
      scheduleManager.schedule.destinationAirport[index] || 'Unknown'
    );

    // Populate the boarding pass with the retrieved flight information and username
    document.getElementById('boardingPass').innerHTML = `
        <div id="passHeader">
          <div class="headerSection">
            <img src="../images/logo.png" id="passLogo" />
            <h1>BOARDING PASS</h1>
          </div>
          <div class="headerSection">
            <div id="smallHeader">BOARDING <br> PASS</div>
          </div>
        </div>
        <div id="passInfo">
          <div class="column1">
            <h2 style="white-space: nowrap">PASSENGER NAME</h2>
            <h2>FROM</h2>
            <h2>TO</h2>
            <h2 style="margin-top: 2em">GATE</h2>
            <h2 class="gateNum">${gateNumber}</h2>
          </div>
          <div class="column1">
            <h3 style="white-space: nowrap; margin-right: -.5em;">${username}</h3>
            <h3>${sourceCity}</h3>
            <h3>${destinationCity}</h3>
            <h2 style="margin-top: 2em">BOARDING TIME</h2>
            <h3 class="gateNum">${boardingTime}</h3>
          </div>
          <div class="column1">
            <h3 style="opacity: 0;">BLANK</h3>
            <h2>FLIGHT</h2>
            <h2>DATE</h2>
            <h2 style="margin-top: 2em">SEAT</h2>
            <h3 class="gateNum">${seatNumber}</h3>
          </div>
          <div class="column1">
            <h3 style="opacity: 0;">BLANK</h3>
            <h3>${flightNumber}</h3>
            <h3>${flightDate}</h3>
          </div>
          <div id="barcode">
            <img style="height: 10em;" src="../images/barcode.png">
          </div>
          <div id="dottedLine"></div>
          <div class="column1">
            <h3 style="opacity: 0;">BLANK</h3>
            <h2 class="condensedH2">NAME</h2>
            <h2 class="condensedH2">FROM</h2>
            <h2 class="condensedH2">TO</h2>
            <h2 class="condensedH2">FLIGHT</h2>
            <h2 class="condensedH2">DATE</h2>
          </div>
          <div class="column1" style="margin-left:-1em">
            <h3 style="opacity: 0;">BLANK</h3>
            <h3 class="condensedH3">${username}</h3>
            <h3 class="condensedH3">${sourceCity}</h3>
            <h3 class="condensedH3">${destinationCity}</h3>
            <h3 class="condensedH3">${flightNumber}</h3>
            <h3 class="condensedH3">${flightDate}</h3>
          </div>
        </div>
        <p id="bordingStatement">Bording gate closes 15 minutes prior to departure time</p>
        <div id="smallPassBottom">
          <div class="smallItem">
            <h2 class="condensedH2" style="margin-top: 2em">GATE</h2>
            <h3 class="condensedH3 gateNum">${gateNumber}</h3>
          </div>
          <div class="smallItem">
            <h2 class="condensedH2" style="margin-top: 2em">BORDING TIME</h2>
            <h3 class="condensedH3 gateNum">${boardingTime}</h3>
          </div>
          <div class="smallItem">
            <h2 class="condensedH2" style="margin-top: 2em">SEAT</h2>
            <h3 class="condensedH3 gateNum">${seatNumber}</h3>
          </div>
        </div>
      `;
  } else {
    console.error('Invalid or missing selected flight index.');
  }
}

// Function to update ticket cost in a specific div if it exists
function updateTicketCost() {
  try {
    // Retrieve all flights from session storage
    const allFlights = JSON.parse(sessionStorage.getItem('allFlights'));

    // Check if allFlights is valid
    if (!allFlights) {
      throw new Error('All flights data not found');
    }

    const selectedIndex = scheduleManager.schedule.flightNumber.indexOf(
      parseInt(sessionStorage.getItem('selectedFlight'))
    );
    let sourceAirport = scheduleManager.schedule.sourceAirport[selectedIndex];
    let destinationAirport =
      scheduleManager.schedule.destinationAirport[selectedIndex];
    let planeType = scheduleManager.schedule.aircraft[selectedIndex];

    // Check if sourceAirport and destinationAirport exist in allFlights
    if (
      !allFlights[sourceAirport] ||
      !allFlights[sourceAirport][destinationAirport]
    ) {
      throw new Error('Flight information not found');
    }

    // Get the flights for the given source and destination airports
    const flights = allFlights[sourceAirport][destinationAirport];
    console.log(flights);

    // Find the flight with the specified plane type
    let matchingFlight = null;
    for (let i = 0; i < flights.length; i++) {
      if (flights[i].planeType === planeType) {
        matchingFlight = flights[i];
        break;
      }
    }

    console.log('Matching Flight: ', matchingFlight);

    // If matching flight is found, update the content of the div with its ticket cost
    if (matchingFlight) {
      // Convert ticket cost to float
      const ticketCostFloat = parseFloat(matchingFlight.ticketCost);

      // Store float value in session storage
      sessionStorage.setItem('ticketCostFloat', ticketCostFloat);

      const ticketCost = matchingFlight.ticketCost.toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD',
      });
      const ticketCostDisplay = document.getElementById('ticketCostDisplay');
      if (ticketCostDisplay) {
        ticketCostDisplay.textContent = `${ticketCost}`;
      } else {
        console.warn('Div with ID "ticketCostDisplay" not found.');
      }
    } else {
      throw new Error('Flight with specified plane type not found');
    }
  } catch (error) {
    console.error('Error getting ticket cost:', error);
  }
}

function filterSourceCities(inputText) {
  const sourceList = document.getElementById('sourceList');
  sourceList.innerHTML = ''; // Clear previous results

  // Create an array to hold filtered source cities
  const filteredSourceCities = [];

  // Filter source cities based on input text
  scheduleManager.schedule.sourceCity.forEach((city, index) => {
    if (city.toLowerCase().includes(inputText.toLowerCase())) {
      // Push the city details into the filteredSourceCities array
      filteredSourceCities.push({
        city: city,
        destinationCity: scheduleManager.schedule.destinationCity[index],
        departureTime: scheduleManager.schedule.scheduledDepartureTime[index],
        arrivalTime: scheduleManager.schedule.scheduledArrivalTime[index],
        date: scheduleManager.schedule.date[index],
        flightNumber: scheduleManager.schedule.flightNumber[index],
      });
    }
  });

  // Sort filteredSourceCities by source location, then by date
  filteredSourceCities.sort((a, b) => {
    if (a.city < b.city) return -1;
    if (a.city > b.city) return 1;
    // If the cities are the same, compare by date
    return new Date(a.date) - new Date(b.date);
  });

  // Display sorted source cities in the dropdown
  filteredSourceCities.forEach((city) => {
    const li = document.createElement('li');
    li.textContent = `${city.city} - To: ${city.destinationCity}, Departure: ${city.departureTime}, Arrival: ${city.arrivalTime}, Date: ${city.date}`;
    li.onclick = function () {
      // Store the selected flight number in session storage
      sessionStorage.setItem('selectedFlight', city.flightNumber);
      console.log(
        'Selected Flight = ',
        sessionStorage.getItem('selectedFlight')
      );
      // Update the input field value with the selected city
      document.getElementById('sourceInput').value = city.city;
      // Close the dropdown
      sourceList.classList.remove('show');
    };
    sourceList.appendChild(li);
  });

  // Show the dropdown
  sourceList.classList.add('show');
}
