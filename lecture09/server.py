# coding=utf-8
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1145))
server.listen(10)

print('socket连接成功')

# 等待连接 服务器挂起状态，等待客户端唤起
clientSocket, clirentAddress = server.accept()
print(f"来自{clirentAddress}的连接")
clientSocket.send('服务器连接成功'.encode('utf-8'))
while True:
    # 接收的数据 来自客户端
    data = clientSocket.recv(1024)  # 这里填写1024即可，就是一kb，最大值
    print('客户端:', data.decode('utf-8'))
    if data:
        backData = input('请回复客户端:')
        clientSocket.send(backData.encode('utf-8'))

# server.close()  因为是长连接，close操作待定