// Function to populate the city dropdown
function populateCityDropdown(airportsData) {
  const source = document.getElementById('source');
  const destination = document.getElementById('destination');

  // Get unique cities from airports data
  const cities = airportsData.reduce((acc, airport) => {
    if (!acc.includes(airport.city)) {
      acc.push(airport.city);
    }
    return acc;
  }, []);

  // Populate the dropdown with cities for source
  cities.forEach((city) => {
    const option = document.createElement('option');
    option.value = city;
    option.textContent = city;
    source.appendChild(option);
  });

  // Populate the dropdown with cities for destination
  cities.forEach((city) => {
    const option = document.createElement('option');
    option.value = city;
    option.textContent = city;
    destination.appendChild(option);
  });
}

// Initialize the login form
function initLoginForm() {
  // Read airports data from session storage
  const airportsData = JSON.parse(sessionStorage.getItem('airports'));

  // Populate the city dropdown
  if (airportsData) {
    populateCityDropdown(airportsData);
  } else {
    console.error('No airports data found in session storage.');
  }

  // Add event listener to the login form
  const loginForm = document.getElementById('loginForm');
  loginForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const selectedCity = document.getElementById('city').value;
    console.log('Selected City:', selectedCity);
  });
}

document.addEventListener('DOMContentLoaded', function () {
  const loginForm = document.getElementById('loginForm');

  loginForm.addEventListener('submit', function (event) {
    event.preventDefault();

    window.location.href = './tickets';
  });
});

// Listen for the event indicating airports data is loaded
document.addEventListener('airportsLoaded', function () {
  // Initialize the login form
  initLoginForm();
});

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
    xhr.open('GET', '../github/data/airports.csv');
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
