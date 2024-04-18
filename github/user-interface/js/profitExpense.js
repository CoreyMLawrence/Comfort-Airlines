// Function to format number as US currency
function formatCurrency(amount) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
  }).format(amount);
}

// Function to display the table
function displayTable(divId, ledgerByLocation, totalProfits) {
  const div = document.getElementById(divId);

  // Clear the div before appending the new table
  div.innerHTML = '';

  // Calculate net profit for each location and sort by net profit (descending order)
  const sortedLocations = Object.keys(ledgerByLocation).sort((a, b) => {
    const netProfitA =
      ledgerByLocation[a].profits + ledgerByLocation[a].expenses;
    const netProfitB =
      ledgerByLocation[b].profits + ledgerByLocation[b].expenses;
    return netProfitB - netProfitA;
  });

  // Create table element
  const table = document.createElement('table');

  // Create table header row
  const headerRow = table.createTHead().insertRow();
  const headers = ['Location', 'Profits', 'Expenses', 'Net Profit'];
  headers.forEach((headerText, index) => {
    const th = document.createElement('th');
    th.textContent = headerText;
    th.style.fontWeight = 'bold';
    if (index === 0) {
      th.style.width = '30em';
    }
    headerRow.appendChild(th);
  });

  // Initialize totals
  let totalExpenses = 0;

  // Create table body
  sortedLocations.forEach((location) => {
    const row = table.insertRow();
    const cell1 = row.insertCell();
    const cell2 = row.insertCell();
    const cell3 = row.insertCell();
    const cell4 = row.insertCell();

    cell1.textContent = location;
    cell2.textContent = formatCurrency(ledgerByLocation[location].profits);
    cell3.textContent = formatCurrency(ledgerByLocation[location].expenses);

    // Calculate net profit
    const netProfit =
      ledgerByLocation[location].profits + ledgerByLocation[location].expenses;
    cell4.textContent = formatCurrency(netProfit);

    // Update totals
    totalExpenses += ledgerByLocation[location].expenses;
  });

  // Add row for totals
  const totalRow = table.insertRow();
  const totalCell1 = totalRow.insertCell();
  const totalCell2 = totalRow.insertCell();
  const totalCell3 = totalRow.insertCell();
  const totalCell4 = totalRow.insertCell();
  totalCell1.textContent = 'Total';
  totalCell2.textContent = formatCurrency(totalProfits);
  totalCell3.textContent = formatCurrency(totalExpenses);
  totalCell4.textContent = formatCurrency(totalProfits + totalExpenses);

  // Append table to the specified div
  div.appendChild(table);
}

// Display ledger by location with a time limit
async function displayLedgerByLocation(divId, timeLimit) {
  // Hardcoded CSV file path
  const url = '../github/reports/ledger.csv';

  // Initialize totalProfits variable
  let totalProfits = 0;
  let totalExpenses = 0;

  try {
    // Fetch the CSV file
    const response = await fetch(url);

    // Ensure the request was successful
    if (!response.ok) {
      throw new Error('Failed to fetch ledger data');
    }

    // Read the entire CSV file into memory as text
    const csvText = await response.text();

    // Parse the CSV text into an array of lines
    const lines = csvText.split('\n');

    // Initialize an associative array to store expenses and profits by location
    const ledgerByLocation = {};

    // Initialize a variable to store the running total of expenses for the "Aircraft Rental Fee" location
    let feeExpenses = 0;

    // Function to process each line
    function processLine(line) {
      // Split the line by comma
      const [item, netProfit, lineTime, location] = line.split(',');

      // Ensure all fields are present
      if (!item || !netProfit || !lineTime || !location) {
        return;
      }

      // Parse net profit as an integer
      const profit = parseInt(netProfit);
      const time = parseInt(lineTime);

      // Check if time is within the limit
      if (time > timeLimit) {
        return;
      }

      // If location is "null", set expense to the amount and location to "Fee"
      if (location.trim() === 'null') {
        // Add the profit to the running total of expenses for the "Fee" location
        feeExpenses += profit;
        totalProfits -= profit;
        return;
      }

      // Update totalProfits variable based on profit value
      if (profit > 0) {
        totalProfits += profit;
      } else {
        totalProfits -= profit;
      }

      // Check if the location is "Aircraft Rental Fee"
      if (location === 'Aircraft Rental Fee') {
        // Add the profit to the running total of expenses for the "Fee" location
        feeExpenses += profit;
        return;
      }

      // Check if the location already exists in the ledgerByLocation array
      if (location in ledgerByLocation) {
        // Add the profit to the existing location
        if (profit >= 0) {
          ledgerByLocation[location].profits += profit;
        } else {
          ledgerByLocation[location].expenses += profit;
          ledgerByLocation[location].profits -= profit;
        }
      } else {
        // Create a new object with the profit for the location
        ledgerByLocation[location] = {
          profits: 0,
          expenses: 0,
        };
      }
    }

    // Process each line of the CSV file, starting from index 1 (skipping the header row)
    for (let i = 1; i < lines.length; i++) {
      processLine(lines[i]);
    }

    // Set the running total of expenses for the "Fee" location
    ledgerByLocation['Aircraft Rental Fee'] = {
      profits: 0,
      expenses: feeExpenses,
    };

    // Display the ledger table
    displayTable(divId, ledgerByLocation, totalProfits);
  } catch (error) {
    console.error('Error displaying ledger:', error);
  }
}
