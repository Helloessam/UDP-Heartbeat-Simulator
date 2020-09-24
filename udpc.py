from socket import *
import time
serverName = '127.0.0.1'
serverPort = 12345
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(10);   #setting timeout of socket
count = 1
message = 0
Seqnum =1
while(count < 10):
    count += 1
    Seqnum +=1
    message = str(message).encode('utf-8')
    if(Seqnum ==3 | Seqnum ==7):
	print "blah"
        time.sleep(2)
	continue
    clientSocket.sendto(message,(serverName, serverPort))   #sending of the message
    time.sleep(1)
Seqnum=1