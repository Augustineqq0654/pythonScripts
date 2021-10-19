import socket

clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 9999
ADDR = (host, port)

while True:
	message = input('>>>')
	# sendto 的第1个参数是 消息，第2个参数是 地址
	clientsock.sendto(message.encode(), ADDR)
	if message == 'exit':
		break

clientsock.close()