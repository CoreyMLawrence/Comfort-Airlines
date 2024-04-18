// Function to populate the city dropdown
function populateCityDropdown(airportsData) {
  const cityDropdown = document.getElementById('city');

  // Get unique cities from airports data
  const cities = airportsData.reduce((acc, airport) => {
    if (!acc.includes(airport.city)) {
      acc.push(airport.city);
    }
    return acc;
  }, []);

  // Populate the dropdown with cities
  cities.forEach((city) => {
    const option = document.createElement('option');
    option.value = city;
    option.textContent = city;
    cityDropdown.appendChild(option);
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
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const selectedCity = document.getElementById('city').value;
    console.log('Username:', username);
    console.log('Password:', password);
    console.log('Selected City:', selectedCity);
    // Add logic to handle login authentication
  });
}

// Initialize the login form when DOM content is loaded
document.addEventListener('DOMContentLoaded', initLoginForm);

document.addEventListener('DOMContentLoaded', function () {
  const usernameInput = document.getElementById('username');
  const cityDropdown = document.getElementById('city');

  // Event listener for username input
  usernameInput.addEventListener('input', function () {
    const username = usernameInput.value;
    sessionStorage.setItem('username', username);
    console.log('Username saved:', username);
  });

  // Event listener for city dropdown
  cityDropdown.addEventListener('change', function () {
    const startingLocation = cityDropdown.value;
    sessionStorage.setItem('startingLocation', startingLocation);
    console.log('Starting location saved:', startingLocation);
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const loginForm = document.getElementById('loginForm');

  loginForm.addEventListener('submit', function (event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    window.location.href = './tickets';
  });
});

// Listen for the event indicating airports data is loaded
document.addEventListener('airportsLoaded', function () {
  // Initialize the login form
  initLoginForm();
});
