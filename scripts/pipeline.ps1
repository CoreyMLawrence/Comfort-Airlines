$root_directory = "scripts";

$scripts = @(
    # airports.csv - manually created
    "flight_weighted_distances.py",
    "flight_demand.py",             # update to use weighted distance
    "flight_fuel_capacity.py",      # update to use weighted distance
    "flight_combine.py",            # update to use weighted distance
    "flight_profit_or_loss.py"      # update to use weighted distance
);

foreach ($script in $scripts) {
    $script_path = Join-Path -Path $root_directory -ChildPath $script;
    python3 $script_path;
}