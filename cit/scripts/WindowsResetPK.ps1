Param(
    [string]$PK
)

nslookup -type=srv _vlmcs._tcp >%temp%\kms.txt
If (-Not $PK -eq '' ) {
    slmgr /ipk $($PK)
    Write-Host "[+] Added Product Key $PK"
}

net stop sppsvc
Write-Host "[+] Network Security Service Stoped"
net start sppsvc
Write-Host "[+] Network Security Service Started"
slmgr /dli
Write-Host "[+] Key Product status"