# ----- An example UDP client in Python that uses recvfrom() method -----

import socket

target_host = "127.0.0.1"
target_port = 80


# Create an UDP based server socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);

# send some data
client.sendto("AAABBBCCC",(target_host,target_port))


# receive some data
data, addr = client.recvfrom(4096)

print(data);
