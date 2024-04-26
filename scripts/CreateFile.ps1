# CreateFile.ps1
Param(
    $Path
)
New-Item $Path # creates a new file at $Path
Write-Host "File $Path was created"