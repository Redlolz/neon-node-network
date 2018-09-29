import sys
import os
import subprocess

# Install the dependencies needed
def install_debian():
    # The dependencies for create_ap
    subprocess.check_call(['sudo', 'apt', 'update'])
    packages = ['sudo', 'apt', 'install', 'util-linux', 'procps', 'hostapd', 'iproute2', 'iw', 'haveged', 'dnsmasq', 'iptables', 'openssl', 'git']
    subprocess.check_call(packages)

    # Install create_ap
    try:
        subprocess.check_call(['git', 'clone', 'https://github.com/oblique/create_ap'])
    except:
        print("create_ap couldn't be installed, maybe because it is already installed?")

# Install for Arch based systems
def install_arch():
    packages = ['sudo', 'pacman', '-S', 'util-linux', 'procps-ng', 'hostapd', 'iproute2', 'iw', 'haveged', 'dnsmasq', 'iptables', 'openssl', 'git', 'python-pip', 'wireless_tools']
    subprocess.check_call(packages)
    subprocess.check_call(['python', '-m', 'pip', 'install', 'wget', '--user'])

    # Install create_ap
    try:
        subprocess.check_call(['git', 'clone', 'https://github.com/oblique/create_ap'])
    except:
        print("create_ap couldn't be installed, maybe because it is already installed?")
install_arch()