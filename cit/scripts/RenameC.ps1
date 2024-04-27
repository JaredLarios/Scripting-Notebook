Param(
    [string]$Site = 'Reforma',
    [Parameter(Mandatory, HelpMessage = "Please provide a valid Name")]
    [string]$WorkStation
)

$NewComputerName = $Site + '-' + $WorkStation
Rename-Computer -NewName "$NewComputerName" -Restart