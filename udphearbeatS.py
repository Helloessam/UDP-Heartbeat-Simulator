# We will need the following module to generate randomized lost packets
import random
import time
from socket import *
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverIP = "127.0.0.1"
serverPort = 12345
count = 1
# Assign IP address and port number to socket
serverSocket.bind((serverIP, serverPort))
while True:
    # Receive the client packet along with the address it is coming from
    try:
	serverSocket.settimeout(2)
        message, address = serverSocket.recvfrom(1024)
        timeleft = message.decode('utf-8')
        timeleft = float(timeleft)
        # Calculating time difference
        timeDiff = (time.time() / 1000) - timeleft;
        print("Time Difference of packet number " + str(count)+ " : " + str(timeDiff) + " ms")
	print time.ctime()
        count += 1
    except timeout:
	print (".....    .....")
        print("Lost Packet")
	print ("......   .....")