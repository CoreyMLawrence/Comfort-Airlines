$root_directory = "scripts";

$scripts = @(
    "combine.py"
);

foreach ($script in $scripts) {
    Write-Host $script;
}