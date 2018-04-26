import socket
buffer_size = 1024
log_size = 5

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8000))
phone.listen(log_size)
print('---->')
conn,addr = phone.accept()

msg=conn.recv(buffer_size)   #收消息
print('客户端发来的消息是：',msg)  

conn.send(msg.upper())   #发消息

conn.close()
phone.close()






















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




