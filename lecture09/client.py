# coding=utf-8
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1145))  # IP地址跟端口号必须跟服务器一致

# 循环执行操作

while True:
    info = client.recv(1024)  # 数据接收 （客户端接收来自服务器的）
    print('服务器说：', info.decode('utf-8'))

    data = input('你对服务器说:')  # 传输数据
    client.send(data.encode('utf-8'))  # 编码解析数据


