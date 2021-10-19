import socket

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

# 创建套接字
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
# print('serverhost:',host)
host = get_host_ip()
print('ip:',host)
port = 9999

# 绑定地址及监听
ADDR = (host, port)
serversock.bind(ADDR)
serversock.listen()

# 等待连接
print('等待客户端连接......')
sock,ip = serversock.accept()
print('已连接')

while True:
	accept_message = sock.recv(1024).decode()
	print('client message:',accept_message)
	if accept_message.lower() == 'exit':
		break
	send_message = input('>>>:')
	sock.send(send_message.encode())
	if send_message.lower() == 'exit':
		break

sock.close()
serversock.close()