$ErrorActionPreference = [System.Management.Automation.ActionPreference]::Stop

$PIPELINE = "./scripts/pipeline.ps1"
$DEPENDENCIES = "requirements.txt"
$SIMULATION = "./src/main.py"
$GUI = "../webdriver.py"
$STEPS = 4

Write-Host "[INFO: 1/$STEPS] Executing script pipeline: generating static data from ./data"
powershell $PIPELINE

Write-Host "[INFO: 2/$STEPS] Installing dependecies using pip3"
pip3 install -r $DEPENDENCIES

Write-Host "[INFO: 3/$STEPS] Running simulation!"
python3 $SIMULATION

Write-Host "[INFO: 4/$STEPS] Running GUI"
python3 $GUI