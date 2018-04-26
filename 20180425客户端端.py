import socket

buffer_size = 1024

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8000))

phone.send('hello'.encode('utf-8'))


data = phone.recv(buffer_size)
print('收到服务端发来的消息:',data)
phone.close()
























# import  socket

# phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# phone.connect(('192.168.12.222',8001)) #拨通电话

# phone.send('hello'.encode('utf-8')) #发消息
# data=phone.recv(1024)
# print('收到服务端的发来的消息：',data)