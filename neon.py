from wifi import Cell, Scheme

import subprocess
import os
import http.server
import ssl
import _thread
# Checking if packages are installed, since these are both pip packages
try:
    import wget
except ModuleNotFoundError:
    print("wget couldn't be imported, maybe it needs to be installed?")
    print("Exiting program...")
try:
    import netifaces
except ModuleNotFoundError:
    print("netifaces couldn't be imported, maybe it needs to be installed?")
    print("Exiting program...")

# Get the wireless network card
def getNetworkInterface():
    interface = netifaces.interfaces()
    return interface[len(interface) - 1]

# Create an acces point
def createAP():
    #  os.chdir('create_ap')
    ipAddress = '192.168.10.1'
    subprocess.call(['./create_ap/create_ap', '-g', ipAddress, '-n', getNetworkInterface(), 'Neon-Node'])

# Connect to a network (mostly other nodes)
def connectToNetwork():
    subprocess.check_call(['ifconfig', getNetworkInterface(), 'down'])
    subprocess.check_call(['ifconfig', getNetworkInterface(), 'up'])
    subprocess.check_call(['iwconfig', getNetworkInterface(), 'essid', 'Neon-Node'])
    subprocess.check_call(['dhclient', getNetworkInterface()])

def connectToNodesRoutine():
    while True:
        try:
            connectToNetwork('Neon-Node')
        except:
            print("Couldn't find and/or connect to another node")
            sleep(60)

# Create an SSL certificate (PROBABLY BORKED)
def createSSLCert():
    # openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
    subprocess.check_call(['openssl', 'reg', '-new', '-x509', '-keyout', 'server.pem', '-out', 'server.pem', '-days', '365', '-nodes'])

# Start an HTTPS server
def startHTTPSServer():
    try:
        server_address = ('0.0.0.0', 443)
        httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket,
                                         server_side=True,
                                         certfile='server.pem',
                                         ssl_version=ssl.PROTOCOL_TLSv1)
        os.chdir('htdocs')
        httpd.serve_forever()
    except Exception:
        httpd.shutdown()
#createAP()

#_thread.start_new_thread( createAP, () )
#_thread.start_new_thread( startHTTPSServer, () )

#connectToNodesRoutine()
connectToNetwork()

#while 1:
#    pass