console.log('in weather.js');
var cityMap = {
  Atlanta: {
    href: 'https://forecast7.com/en/33d75n84d39/atlanta/?unit=us',
    label_1: 'ATLANTA',
  },
  'Dallas;Fort Worth': {
    href: 'https://forecast7.com/en/32d78n96d80/dallas/?unit=us',
    label_1: 'DALLAS',
  },
  Denver: {
    href: 'https://forecast7.com/en/39d74n104d99/denver/?unit=us',
    label_1: 'DENVER',
  },
  Chicago: {
    href: 'https://forecast7.com/en/41d88n87d63/chicago/?unit=us',
    label_1: 'CHICAGO',
  },
  'Los Angeles': {
    href: 'https://forecast7.com/en/34d05n118d24/los-angeles/?unit=us',
    label_1: 'LOS ANGELES',
  },
  'New York City': {
    href: 'https://forecast7.com/en/40d71n74d01/new-york/?unit=us',
    label_1: 'NEW YORK CITY',
  },
  'Las Vegas': {
    href: 'https://forecast7.com/en/36d17n115d14/las-vegas/?unit=us',
    label_1: 'LAS VEGAS',
  },
  Orlando: {
    href: 'https://forecast7.com/en/28d54n81d38/orlando/?unit=us',
    label_1: 'ORLANDO',
  },
  Miami: {
    href: 'https://forecast7.com/en/25d76n80d19/miami/?unit=us',
    label_1: 'MIAMI',
  },
  Charlotte: {
    href: 'https://forecast7.com/en/35d23n80d84/charlotte/?unit=us',
    label_1: 'CHARLOTTE',
  },
  Seattle: {
    href: 'https://forecast7.com/en/47d61n122d33/seattle/?unit=us',
    label_1: 'SEATTLE',
  },
  Pheonix: {
    href: 'https://forecast7.com/en/33d45n112d07/phoenix/?unit=us',
    label_1: 'PHOENIX',
  },
  Newark: {
    href: 'https://forecast7.com/en/40d74n74d17/newark/?unit=us',
    label_1: 'NEWARK',
  },
  'San Francisco': {
    href: 'https://forecast7.com/en/37d77n122d42/san-francisco/?unit=us',
    label_1: 'SAN FRANCISCO',
  },
  Houston: {
    href: 'https://forecast7.com/en/29d76n95d37/houston/?unit=us',
    label_1: 'HOUSTON',
  },
  Boston: {
    href: 'https://forecast7.com/en/42d36n71d06/boston/?unit=us',
    label_1: 'BOSTON',
  },
  'Fort Lauderdale;Hollywood': {
    href: 'https://forecast7.com/en/26d12n80d14/fort-lauderdale/?unit=us',
    label_1: 'FORT LAUDERDALE',
  },
  'Minneapolis;Saint Paul': {
    href: 'https://forecast7.com/en/44d98n93d27/minneapolis/?unit=us',
    label_1: 'MINNEAPOLIS',
  },
  Detroit: {
    href: 'https://forecast7.com/en/42d33n83d05/detroit/?unit=us',
    label_1: 'DETROIT',
  },
  Philadelphia: {
    href: 'https://forecast7.com/en/39d95n75d17/philadelphia/?unit=us',
    label_1: 'PHILADELPHIA',
  },
  'Salt Lake City': {
    href: 'https://forecast7.com/en/40d76n111d89/salt-lake-city/?unit=us',
    label_1: 'SALT LAKE CITY',
  },
  'Washington D.C.;Arlington': {
    href: 'https://forecast7.com/en/38d91n77d04/washington/?unit=us',
    label_1: 'WASHINGTON D. C.',
  },
  'San Diego': {
    href: 'https://forecast7.com/en/32d72n117d16/san-diego/?unit=us',
    label_1: 'SAN DIEGO',
  },
  'Baltimore;Washington D.C.': {
    href: 'https://forecast7.com/en/39d29n76d61/baltimore/?unit=us',
    label_1: 'BALTIMORE',
  },
  Tampa: {
    href: 'https://forecast7.com/en/27d95n82d46/tampa/?unit=us',
    label_1: 'TAMPA',
  },
  Austin: {
    href: 'https://forecast7.com/en/30d27n97d74/austin/?unit=us',
    label_1: 'AUSTIN',
  },
  Nashville: {
    href: 'https://forecast7.com/en/36d16n86d78/nashville/?unit=us',
    label_1: 'NASHVILLE',
  },
  Paris: {
    href: 'https://forecast7.com/en/48d862d35/paris/?unit=us',
    label_1: 'PARIS',
  },
};

// Function to update the weather anchor tag based on the city
function updateWeather(city) {
  // Get the weather box div
  var weatherBox = document.getElementById('startWeather');

  // Check if the city exists in the cityMap
  if (cityMap.hasOwnProperty(city)) {
    // Extract data from cityMap
    var { href, label_1 } = cityMap[city];

    // Create a template literal with the data
    var weatherHTML = `
        <a
          class="weatherwidget-io"
          href="${href}"
          data-label_1="${label_1}"
          data-font="SF Pro"
          data-theme="original"
          data-days="7"
          data-basecolor="rgba(245, 245, 245, 0)"
          data-textcolor="#000000"
          data-highcolor="#000000"
          data-lowcolor="#000000"
          data-mooncolor="#c8c8c8"
          data-cloudcolor="#c8c8c8"
        >
          ${label_1.toUpperCase()} WEATHER
        </a>
        <script>
          !(function (d, s, id) {
            var js,
              fjs = d.getElementsByTagName(s)[0];
            if (!d.getElementById(id)) {
              js = d.createElement(s);
              js.id = id;
              js.src = "https://weatherwidget.io/js/widget.min.js";
              fjs.parentNode.insertBefore(js, fjs);
            }
          })(document, 'script', 'weatherwidget-io-js');
        </script>
      `;

    // Set the HTML content of weatherBox
    weatherBox.innerHTML = weatherHTML;
  } else {
    console.error('City not found in cityMap.');
  }
}

// Function to update the weather anchor tag based on the city
function updateWeather2(city) {
  // Get the weather box div
  var weatherBox = document.getElementById('destWeather');

  // Check if the city exists in the cityMap
  if (cityMap.hasOwnProperty(city)) {
    // Extract data from cityMap
    var { href, label_1 } = cityMap[city];

    // Create a template literal with the data
    var weatherHTML = `
            <a
              class="weatherwidget-io"
              href="${href}"
              data-label_1="${label_1}"
              data-font="SF Pro"
              data-theme="original"
              data-days="7"
              data-basecolor="rgba(245, 245, 245, 0)"
              data-textcolor="#000000"
              data-highcolor="#000000"
              data-lowcolor="#000000"
              data-mooncolor="#c8c8c8"
              data-cloudcolor="#c8c8c8"
            >
              ${label_1.toUpperCase()} WEATHER
            </a>
          `;

    // Set the HTML content of weatherBox
    weatherBox.innerHTML = weatherHTML;

    // Function to insert the script element into the DOM and execute it
    function insertScript() {
      // Remove any existing script element
      var existingScript = document.getElementById('weatherwidget-io-js');
      if (existingScript) {
        existingScript.parentNode.removeChild(existingScript);
      }

      // Create and insert the new script element
      var script = document.createElement('script');
      script.id = 'weatherwidget-io-js';
      script.src = '../js/widget.js';
      document.body.appendChild(script);
    }

    // Call the insertScript function
    insertScript();
  } else {
    console.error('City not found in cityMap.');
  }
}

// Function to run when the page loads
function onPageLoad() {
  // Retrieve the starting location from session storage
  const startingLocation = sessionStorage.getItem('startingLocation');

  // Check if startingLocation is not null or undefined
  if (startingLocation) {
    // Call the updateWeather function with the retrieved startingLocation
    updateWeather(startingLocation);
  } else {
    console.error('Starting location not found in session storage.');
  }
}

// Run the onPageLoad function when the window has fully loaded
window.onload = onPageLoad;
