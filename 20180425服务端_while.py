
# import socket
from socket import *
ip_port = ('127.0.0.1',8080)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)
print('服务端开始运行了：----')
conn, addr = tcp_server.accept()
print('双向链接是：',conn)
print('客户端地址是：',addr)

while True:
    print('服务端开始接收了：----')
    data = conn.recv(buffer_size)
    print('客户端发来的消息是：', data.decode('utf-8'))
    conn.send(data.upper())

conn.close()
tcp_server.close()

# phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# phone.bind(('127.0.0.1',8000))
# phone.listen(log_size)
# print('---->')
# conn,addr = phone.accept()
#
# msg=conn.recv(buffer_size)   #收消息
# print('客户端发来的消息是：',msg)
#
# conn.send(msg.upper())   #发消息
#
# conn.close()
# phone.close()






















# import socket

# phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
# phone.bind(('127.0.1.11',8000)) #绑定手机卡
# phone.listen(5) #开机
# print('---->')
# conn,addr=phone.accept() #等电话

# msg=conn.recv(1024) #收消息
# print('客户端发来的消息是: ',msg)
# conn.send(msg.upper())#发消息

# conn.close()
# phone.close()




