$ErrorActionPreference = [System.Management.Automation.ActionPreference]::Stop

$PIPELINE = "./scripts/pipeline.ps1"
$DEPENDENCIES = "requirements.txt"
$MAIN = "./src/main.py"

Write-Host "[INFO: 1/3] Executing script pipeline: generating static data from ./data"
powershell $PIPELINE

Write-Host "[INFO: 2/3] Installing dependecies using pip3"
pip3 install -r $DEPENDENCIES

Write-Host -NoNewline "[INFO: 3/3] Running simulation!"
python3 $MAIN