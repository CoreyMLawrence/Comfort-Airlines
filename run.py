import subprocess
import os

# Change directory to "./github"
os.chdir("./github")

PIPELINE = "./scripts/pipeline.ps1"
DEPENDENCIES = "requirements.txt"
SIMULATION = "./src/main.py"
GUI = "../webdriver.py"
STEPS = 4

# Execute script pipeline
print("[INFO: 1/{0}] Executing script pipeline: generating static data from ./data".format(STEPS))
subprocess.run(["powershell", PIPELINE], check=True)

# Install dependencies using pip3
print("[INFO: 2/{0}] Installing dependencies using pip3".format(STEPS))
subprocess.run(["pip3", "install", "-r", DEPENDENCIES], check=True)

# Run simulation
print("[INFO: 3/{0}] Running simulation!".format(STEPS))
subprocess.run(["python3", SIMULATION], check=True)

# Run GUI
print("[INFO: 4/{0}] Running GUI".format(STEPS))
subprocess.run(["python3", GUI], check=True)
