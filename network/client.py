import socket
hostport = ('127.0.0.1',8898)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建TCP socket
s.connect(hostport)  #链接套接字

while True:
    user_input = input('>>>:').strip()
    s.send(bytes(user_input,'utf8')) #发送数据到套接字
    if not len(user_input):continue
    if user_input == 'quit':
        s.close()
        break
    server_reply = s.recv(1024) #接收套接字数据

    print(str(server_reply, 'utf8'))  #打印输出
