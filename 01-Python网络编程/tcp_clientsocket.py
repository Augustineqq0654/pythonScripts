import socket

# 创建套接字
clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
# print('clienthost:',host)
host ='42.193.123.102'
port = 9999

# 连接服务端
clientsock.connect((host, port))

while True:
	send_message = input('>>>')
	clientsock.send(send_message.encode())
	if send_message.lower() == 'exit':
		break
	accept_message = clientsock.recv(1024).decode()
	print('server message:',accept_message)
	if accept_message.lower() == 'exit':
		break

clientsock.close()

