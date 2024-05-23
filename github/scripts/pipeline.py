import os
import subprocess

ROOT_DIRECTORY = "scripts"

scripts = [
    "flight_weighted_distances.py",
    "flight_demand.py",
    "flight_fuel_capacity.py",
    "flight_combine.py",
    "flight_profit_or_loss.py",
    "flight_times.py",
    "flight_master_record.py"
]

for script in scripts:
    script_path = os.path.join(ROOT_DIRECTORY, script)
    subprocess.run(["python3", script_path], check=True)
