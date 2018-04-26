from socket import *
ip_port = ('127.0.0.1',8080)
buffer_size = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    msg=input('>>:').strip()
    tcp_client.send(msg.encode('utf-8'))
    print('客户端已经发送消息。')
    data=tcp_client.recv(buffer_size)
    print('收到服务端发来的消息：',data.decode('utf-8'))

tcp_client.close()





















# import  socket

# phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# phone.connect(('192.168.12.222',8001)) #拨通电话

# phone.send('hello'.encode('utf-8')) #发消息
# data=phone.recv(1024)
# print('收到服务端的发来的消息：',data)