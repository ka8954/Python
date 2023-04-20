import socket
hostname = socket.gethostname()
IpAddress = socket.gethostbyname(hostname)
print('\nYour IP Address is : ', IpAddress)
