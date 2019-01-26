import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HostPort = ('127.0.0.1',8898)
s.bind(HostPort)  #绑定地址端口
s.listen(5)  #监听最多5个连接请求
while True:
    print('server socket waiting...')
    c,addr = s.accept()  #阻塞等待链接，创建套接字c链接和地址信息addr
    print('客户端地址:',addr)
    print('\r\n')
    print(c)
    while True:
        try:
            client_date = c.recv(1024) #接收客户端数据
            if str(client_date,'utf8') == 'quit':
                c.close()
                break
        except Exception:
            break
        c.send(client_date)  #发送数据给客户端
        print('clientINFO:',str(client_date, 'utf8')) #打印数据，默认接收数据为bytes，需转换成stra
