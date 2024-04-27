Param(
    [string]$Site = 'Reforma',
    [Parameter(Mandatory, HelpMessage = "Please provide a valid Name")]
    [string]$Name
)

$NewComputerName = $Site + '-' + $Name
Rename-Computer -NewName "$NewComputerName" -Restart