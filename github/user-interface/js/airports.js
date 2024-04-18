// Function to read CSV file
function readFile() {
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
    xhr.open('GET', './github/data/airports.csv');
    xhr.send();
  });
}

// Function to parse CSV data and store it in session storage
function parseCSVAndStore(csvData) {
  // Split CSV into lines
  const lines = csvData.split('\n');

  // Initialize array to store airport data
  const airports = [];

  // Iterate over each line (excluding header)
  for (let i = 1; i < lines.length; i++) {
    const line = lines[i].trim();
    if (line !== '') {
      // Split each line into values
      const values = line.split(',');

      // Construct object for each airport
      const airport = {
        rank: parseInt(values[0]),
        name: values[1],
        iataCode: values[2],
        city: values[3],
        state: values[4],
        metroArea: values[5],
        metroPopulation: parseInt(values[6]),
        latitude: parseFloat(values[7]),
        longitude: parseFloat(values[8]),
      };

      // Push the airport object into the array
      airports.push(airport);
    }
  }

  // Store the airports array in session storage
  sessionStorage.setItem('airports', JSON.stringify(airports));

  // Display top flights after parsing and storing data
  displayTopFlights(airports);

  // Dispatch event indicating airports data is loaded
  const airportsLoadedEvent = new CustomEvent('airportsLoaded');
  document.dispatchEvent(airportsLoadedEvent);
}

// Call readFile and parseCSVAndStore
readFile()
  .then(parseCSVAndStore)
  .then(() => {
    console.log(
      'CSV data parsed, stored, and top flights displayed successfully.'
    );
  })
  .catch((error) => console.error('Error:', error));

sessionStorage.setItem('currentMinute', 0);
