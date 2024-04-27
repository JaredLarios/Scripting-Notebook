Param(
    [string]$Path = './app',
    [string]$DestinationPath = './'
)
$date = Get-Date -format "yyyy-MM-dd"
Write-Host  "Created backup at $($date) - path $($Path + ' ' + $DestinationPath)"