import subprocess, sys, os

# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

def powershell_script(cmd: str):
    p = subprocess.Popen(["powershell.exe", cmd],
                        stdout=sys.stdout)
    p.communicate()

root = os.path.join('.', 'scripts')
pk_reset_path = os.path.join(root, 'WindowsResetPK.ps1')
rename_c_path = os.path.join(root, 'RenameC.ps1')

opt = input('Do you want to reset PK? (y/n) \t')
pk = input('Enter Prod Key if you have one? (Hit enter if not) \t')

if opt == 'yes' or opt == 'y':
    cmd = f'-PK {pk}' if pk != '' else ''
    powershell_script(cmd)

opt = input('Do you want to renamethe pc? (y/n) \t')
site = input('Enter site name: (Default Site: Reforma) \t')
w_station = input('Enter workstation name: (Example: C1) \t')

if opt == 'yes' or opt == 'y':
    cmd = f'-Site {site} -WorkStation {w_station}' if site != '' else f'-WorkStation {w_station}'
    powershell_script(cmd)