import subprocess

sites = ['Reforma', 'Portales']


def verify_wdinows():
    cmds = ['slmgr /dli', 'slmgr /upk','slmgr /cpky']
    for cmd in cmds:
        print('[+] Comand run: \t', cmd)
        subprocess.call(cmd, shell=True)

def rename_windows():
    subprocess.call('powershell', shell=True)
    cmd = "powershell Invoke-Expression -Command 'hostname'"
    output = subprocess.check_output(cmd, shell=True)
    print('[+] Desktop Old Name: \t', output.decode('utf-8'))

    print('--- \t Renaming Computer \t---')
    site_opt = input('Enter the Site Number: \n\t1) Reforma \n\t2) Portales \n\t3) Exit \n--> ')
    work_station_number = input('Enter the Work Station Name: ')
    try:
        site_opt = int( site_opt ) - 1
        work_station_number = int( work_station_number )
        name = f'{sites[site_opt]}-{work_station_number}'
        cmd = f'Rename-Computer -NewName "{name}" -Restart'

    except:
        print('[x] Error: \tComputer not Renamed')

verify_wdinows()
rename_windows()