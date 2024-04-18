// Function to read CSV file
function readFlightsFile() {
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

// Function to parse CSV data and store it in an array
function parseFlightsCSV(csvData) {
  // Split CSV into lines
  const lines = csvData.split('\n');

  // Initialize object to store flights data by tail number
  const flightsByTailNumber = {};

  // Retrieve airports data from session storage
  const airports = JSON.parse(sessionStorage.getItem('airports'));

  // Iterate over each line (excluding header)
  for (let i = 1; i < lines.length; i++) {
    const line = lines[i].trim();
    if (line !== '') {
      // Split each line into values
      const values = line.split(',');

      // Construct object for each flight
      const flight = {
        number: parseInt(values[0]),
        source: getCityName(values[1], airports),
        destination: getCityName(values[2], airports),
        passengers: parseInt(values[3]),
        scheduledDepartureTime: parseInt(values[4]),
        scheduledArrivalTime: parseInt(values[5]),
        actualDepartureTime: parseInt(values[6]),
        actualArrivalTime: parseInt(values[7]),
        aircraftTailNumber: values[8],
        aircraftType: values[9],
      };

      // Update flightsByTailNumber object
      if (!flightsByTailNumber[flight.aircraftTailNumber]) {
        flightsByTailNumber[flight.aircraftTailNumber] = [];
      }
      flightsByTailNumber[flight.aircraftTailNumber].push(flight);
    }
  }

  return flightsByTailNumber;
}

// Function to get city name from airport code
function getCityName(airportCode, airports) {
  const airport = airports.find((a) => a.name === airportCode);
  return airport ? airport.city : airportCode;
}
// Function to update planeBox divs
function updatePlaneBoxes(flightsByTailNumber, maxTime) {
  const planeStatusContainer = document.getElementById('simulator');
  if (planeStatusContainer) {
    // Clear the existing content
    planeStatusContainer.innerHTML = '';

    // Create variable to hold HTML for all plane boxes
    let planeBoxesHTML = '';

    // Iterate over flights by tail number
    Object.keys(flightsByTailNumber).forEach((tailNumber) => {
      const flights = flightsByTailNumber[tailNumber];

      // Sort flights by scheduled departure time in descending order
      flights.sort(
        (a, b) => b.scheduledDepartureTime - a.scheduledDepartureTime
      );

      // Filter flights based on maxTime
      const filteredFlights = flights.filter(
        (flight) => flight.scheduledDepartureTime <= maxTime
      );

      // Get the latest flight
      const latestFlight = filteredFlights[0];

      if (latestFlight) {
        // Convert scheduled departure time and arrival time to time format
        const departureTime = convertMinutesToTime(
          latestFlight.actualDepartureTime
        );
        let arrivalTime = convertMinutesToTime(latestFlight.actualArrivalTime);
        if (isNaN(parseInt(arrivalTime))) {
          arrivalTime = 'Finished';
        }

        const width =
          ((maxTime - latestFlight.actualDepartureTime) /
            (latestFlight.actualArrivalTime -
              latestFlight.actualDepartureTime)) *
          105;

        const planeBoxHTML = `
          <div class="planeBox">
            <div class="plane">
              <div class="planeRow">
                <div class="pair">
                  <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-plane" width="32" height="32" viewBox="0 0 24 24" stroke-width="1.5" stroke="#ffffff" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                    <path d="M16 10h4a2 2 0 0 1 0 4h-4l-4 7h-3l2 -7h-4l-2 2h-3l2 -4l-2 -4h3l2 2h4l-2 -7h3z" />
                  </svg>
                  <h3 class="lighter" id="tailNumberValue">${latestFlight.aircraftTailNumber}</h3>
                </div>
                <div class="pair">
                  <h3 class="lighter" id="flightNumber">Flight:</h3>
                  <h3 class="lighter" id="flightNumberValue">${latestFlight.number}</h3>
                </div>
              </div>
              <div class="separator"></div>
              <table>
                <tr>
                  <th id="Origin">From:</th>
                  <td id="OriginValue">${latestFlight.source}</td>
                </tr>
                <tr>
                  <th id="destination">To:</th>
                  <td id="destinationValue">${latestFlight.destination}</td>
                </tr>
                <tr>
                  <th id="passengers">Passengers:</th>
                  <td id="passengersValue">${latestFlight.passengers}</td>
                </tr>
                <tr>
                  <th id="departure">Departure:</th>
                  <td id="departureValue">${departureTime}</td>
                </tr>
                <tr>
                  <th id="arrival">Arrival:</th>
                  <td id="arrivalValue">${arrivalTime}</td>
                </tr>
              </table>
            </div>
            <div class="loading-bar-container">
            <div class="loading-bar" id="loadingBar${latestFlight.number}" style="width: ${width}%"></div>
            </div>
          </div>
        `;

        // Append planeBox HTML to planeBoxesHTML
        planeBoxesHTML += planeBoxHTML;
      }
    });

    // Append planeBoxesHTML to planeStatusContainer
    simulator.innerHTML = planeBoxesHTML;
  }
}
