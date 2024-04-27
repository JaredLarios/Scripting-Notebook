Param(
    [string]$PK,
    [string]$RemovePK = "y"
)

nslookup -type=srv _vlmcs._tcp >%temp%\kms.txt
If (-Not $RemovePK -eq 'n') {
    cscript /NoLogo "c:\Windows\system32\slmgr.vbs" /upk
    Write-Host "[+] Product Key Removed"
}
If (-Not $PK -eq '' ) {
    cscript /NoLogo "c:\Windows\system32\slmgr.vbs" /ipk $($PK)
    Write-Host "[+] Added Product Key $PK"
}

net stop sppsvc
net start sppsvc

cscript /NoLogo "c:\Windows\system32\slmgr.vbs" /dli
Write-Host "[+] Key Product status"