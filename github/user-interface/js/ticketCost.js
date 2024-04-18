// Function to read CSV file
function readCSVFile(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();

    reader.onload = () => {
      resolve(reader.result);
    };

    reader.onerror = reject;

    reader.readAsText(file);
  });
}

// Function to store all flights
async function storeAllFlights() {
  try {
    // Fetch the CSV file
    const fileResponse = await fetch('../github/data/flight_master_record.csv');
    if (!fileResponse.ok) {
      throw new Error('Failed to fetch the CSV file');
    }
    const csvData = await fileResponse.text();

    // Check if CSV data is empty
    if (!csvData.trim()) {
      throw new Error('CSV file is empty');
    }

    // Parse the CSV data and split by lines
    const flights = csvData.trim().split('\n');

    // Initialize an object to store all flights
    const allFlights = {};

    // Loop through each flight data
    flights.forEach((flight) => {
      const flightDetails = flight.split(',');

      // Extract relevant information
      const sourceAirport = flightDetails[0].trim();
      //console.log(sourceAirport);
      const destinationAirport = flightDetails[1].trim();
      //console.log(destinationAirport);
      const planeType = flightDetails[5].trim();
      //console.log(planeType);
      const ticketCost = parseFloat(flightDetails[7]);
      //console.log(ticketCost);

      // Use sourceAirport and destinationAirport as keys in the object
      if (!allFlights[sourceAirport]) {
        allFlights[sourceAirport] = {};
      }
      if (!allFlights[sourceAirport][destinationAirport]) {
        allFlights[sourceAirport][destinationAirport] = [];
      }
      // Push flight details including plane type
      allFlights[sourceAirport][destinationAirport].push({
        planeType,
        ticketCost,
      });
    });

    console.log(allFlights);

    // Store all flights data in session storage
    sessionStorage.setItem('allFlights', JSON.stringify(allFlights));

    // Return the allFlights object
    return allFlights;
  } catch (error) {
    console.error('An error occurred:', error);
    throw error;
  }
}

// Method to initialize the schedule manager
function init() {
  document.addEventListener('DOMContentLoaded', async () => {
    try {
      const allFlights = await storeAllFlights();
      console.log('All flights:', allFlights);
      console.log('Initialization completed.');
      // Call any other initialization functions here if needed
    } catch (error) {
      console.error('Initialization error:', error);
    }
  });
}

// Method to display ticket cost data in the ticketCost div
function displayTicketCost() {
  console.log('display ticket cost');
  // Retrieve all flights data from sessionStorage
  const allFlights = JSON.parse(sessionStorage.getItem('allFlights'));

  // Reference to the ticketCost div
  const ticketCostDiv = document.getElementById('ticketCost');

  // Check if the div exists and all flights data is available
  if (ticketCostDiv && allFlights) {
    let htmlContent = '<h2>Ticket Costs</h2>';

    // Loop through all flights data
    for (const sourceAirport in allFlights) {
      for (const destinationAirport in allFlights[sourceAirport]) {
        const flights = allFlights[sourceAirport][destinationAirport];
        htmlContent += `<h3>From ${sourceAirport} to ${destinationAirport}</h3>`;
        htmlContent += '<ul>';
        flights.forEach((flight, index) => {
          htmlContent += `<li>Flight ${index + 1}: Ticket Cost $${
            flight.ticketCost
          }</li>`;
        });
        htmlContent += '</ul>';
      }
    }

    // Set the HTML content of the ticketCost div
    ticketCostDiv.innerHTML = htmlContent;
  }
}

init();
