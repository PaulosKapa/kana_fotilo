import socket
HOST = input("PC ip: ")
PORT = 65432
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
try:
	while True:
		data = client_socket.recv(1024).decode()
		print(data)
except KeyboardInterrupt:
	print("shutdown")
finally:
	client_socket.close()
