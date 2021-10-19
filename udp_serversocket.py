import socket

serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 9999
ADDR = (host, port)
serversock.bind(ADDR)

while True:
	# recvfrom 的返回值，第一个是 消息，第二个是地址
	message, address = serversock.recvfrom(1024)
	print('client message:', message.decode()) 
	if message.decode() == 'exit':
		break

serversock.close()
