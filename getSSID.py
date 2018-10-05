import subprocess

checkWifi = subprocess.check_output('nmcli -t -f active,ssid dev wifi', shell=True)
checkWifi = checkWifi.decode().split('''\n''')

print(checkWifi)

if 'yes:Neon-Node' in checkWifi:
    print('Already connected')
else:
    print('Nothing to do')