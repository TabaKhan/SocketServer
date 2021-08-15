import socket

target_host = "23.88.63.176"
target_port = 4364

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"GET / HTTP/1.1\r\nHost:23.88.63.176\r\n\r\n")

response = client.recv(4096)
print(response.decode())
client.close()