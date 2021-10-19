#!/usr/bin/env python
# coding:utf8
import socket
HOST='服务器IP'
PORT=9999
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
s.connect((HOST,PORT))       #要连接的IP与端口
while 1:
    try:
        cmd = input('请输入一个命令>>>')
        s.send(cmd.encode('utf-8'))
        #因为服务器是windows，执行的命令是GBK格式，所以传回来后需要进行解码，解码为GBK格式
        result = s.recv(102400).decode('gbk')
        print(result)
    except Exception as e:
        print("client received's data exception occurred: %s" % e)
s.close()
