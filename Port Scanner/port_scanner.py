
import pyfiglet
import sys
import socket
import threading
from datetime import datetime


ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)


# Defining a target
if len(sys.argv) == 2:
	
	# translate hostname to IPv4
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of Argument")

# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

def portScanner(startport, endport):

	try:

	
		# will scan ports between 1 to 65,535
		for port in range(startport, endport):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
		
			# returns an error indicator
			result = s.connect_ex((target,port))
			if result ==0:
				print("Port {} is open".format(port))
			s.close()
			#print("Port {} is closed".format(port))	

	except KeyboardInterrupt:
			print("\n Exiting Program !!!!")
			sys.exit()
	except socket.gaierror:
			print("\n Hostname Could Not Be Resolved !!!!")
			sys.exit()
	except socket.error:
			print("\ Server not responding !!!!")
			sys.exit()

#ourThread = threading.Thread(target = portScanner , args = (1,))
#myThread = threading.Thread(target = portScanner, args = (1000,))

#ourThread.start()
#myThread.start()

threading.Thread(target = portScanner , args = (1, 50, )).start()

counter = 1
while counter < 1310:
	threading.Thread(target = portScanner , args = (counter * 50,(counter * 50) + 50, )).start()
	counter += 1

threading.Thread(target = portScanner , args = (65500, 65535, )).start()

