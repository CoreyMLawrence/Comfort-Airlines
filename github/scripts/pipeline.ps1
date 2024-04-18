$ROOT_DIRECTORY = "scripts";
$ErrorActionPreference = [System.Management.Automation.ActionPreference]::Stop

$scripts = @(
    # starting point: airports.csv - manually created
    "flight_weighted_distances.py",
    "flight_demand.py",
    "flight_fuel_capacity.py",
    "flight_combine.py",
    "flight_profit_or_loss.py",
    "flight_times.py",
    "flight_master_record.py"
);

foreach ($script in $scripts) {
    $script_path = Join-Path -Path $ROOT_DIRECTORY -ChildPath $script;
    python3 $script_path;
}