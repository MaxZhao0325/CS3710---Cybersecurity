import socket
from datetime import datetime

# let the user input the target address
address = input("Enter a target to scan: ")
target = socket.gethostbyname(address)

# let the user input port range
print("please enter the range of ports you would like to scan on the target")
startport = int(input("Enter a start port: "))
endport = int(input("Enter a end port: "))

# print out the scanning start time and scanning target
print("Scanning started at: " + str(datetime.now()))
print("Please wait, scanning target now: " + address)

for port in range (startport, endport):
    # open the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # set timeout for connection attempt
    socket.setdefaulttimeout(5)   

    # connect the socket to the external target
    result = sock.connect_ex((target, port))

    # print out whether the port is open or not
    if result == 0:
        print("port " + str(port) + ":         Open")
    else:
        print("port " + str(port) + ":         Closed")

    # close the sock
    sock.close()

# scanning complete
print("Port Scanning Completed")
